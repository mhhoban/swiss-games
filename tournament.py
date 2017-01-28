#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""

    DB = connect()
    cursor = DB.cursor()

    cursor.execute("UPDATE player_matches SET matches = 0")
    cursor.execute("UPDATE player_wins SET wins = 0")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""

    deleteMatches()

    DB = connect()
    cursor = DB.cursor()
    cursor.execute("DELETE FROM player_registry *")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""

    # establish db connection
    DB = connect()
    cursor = DB.cursor()

    # fetch number of players registered
    cursor.execute("SELECT count(*) from player_registry")
    player_count = cursor.fetchall()[0][0]
    DB.close()

    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    # establish db connection
    DB = connect()
    cursor = DB.cursor()

    cursor.execute("INSERT INTO player_registry (player_name) VALUES "
                   "(%s)", (name,))

    # get id assigned to player:
    cursor.execute("SELECT MAX(player_id) from player_registry")
    player_id = cursor.fetchall()[0][0]

    # register player in wins and matches tables:
    cursor.execute("INSERT INTO player_wins (player_id, wins) VALUES (%s, 0)",
                   (player_id,))
    cursor.execute("INSERT INTO player_matches (player_id, matches) "
                   "VALUES (%s, 0)", (player_id,))

    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    DB = connect()
    cursor = DB.cursor()

    cursor.execute("select a.player_id, a.player_name, b.wins, c.matches "
                   "from player_registry as a, player_wins as b, "
                   "player_matches as c where a.player_id = b.player_id and"
                   " b.player_id = c.player_id ORDER BY wins DESC, "
                   "matches DESC")

    standings = [(row[0], row[1], row[2], row[3]) for row in cursor.fetchall()]

    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    # increment winner wins:

    DB = connect()
    cursor = DB.cursor()

    cursor.execute("SELECT wins FROM player_wins WHERE player_id = %s",
                   (winner,))

    new_wins = (cursor.fetchall()[0][0]) + 1
    cursor.execute("UPDATE player_wins SET wins = %s WHERE player_id = %s",
                   (new_wins, winner))

    # increment winner matches:

    cursor.execute("SELECT matches FROM player_matches WHERE player_id = %s",
                   (winner,))
    new_matches = (cursor.fetchall()[0][0]) + 1
    cursor.execute("UPDATE player_matches SET matches = %s WHERE player_id = %s",
                   (new_matches, winner))

    # increment loser matches:

    cursor.execute("SELECT matches FROM player_matches WHERE player_id = %s",
                   (loser,))
    new_matches = (cursor.fetchall()[0][0]) + 1
    cursor.execute("UPDATE player_matches SET matches = %s WHERE player_id = %s",
                   (new_matches, loser))

    # commit changes, close connection
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    # fetch current standings:

    standings = playerStandings()
    players = len(standings)

    pairs = [(standings[x][0], standings[x][1],
              standings[x+1][0], standings[x+1][1])
             for x in range(players) if x % 2 == 0]

    return pairs


