#Swiss Games: Functions For Tracking a Swiss Style Tournament

Swiss Games includes methods for conducting and tracking a Swiss
style tournament in a PostgreSQL database.

##Requirements:

Swiss Games requires a PostgreSQL database server,
was written for PostgreSQL 9.6 and requires Python 2.7 to run
locally.

##Setup

First, run your environment's PostgreSQL server. It is highly
recommended, but not required, to run the setup file and work
with Swiss Games within a virtual environment. Finish the setup
by running the setup script:

```
python setup.py
```

##Using Swiss Games:

Swiss Games uses the following methods:

connect() - returns a connection to the tournament's database table
and is not called directly by the user.

deletePlayers() - deletes all players and all of their match records
from the tournament database

countPlayers() - returns an integer for how many players are registered
in the tournament

registerPlayer(name) - registers a player with string 'name' for the tournament
and creates associated match and win records for the new player.

playerStandings() - returns a list of touples, each of with the format
(player-id, player-name, player-wins, player-matches) ranked in order of
the player's present standings.

reportMatch(winner_id, loser_id) - reports the result of a match between
two players where the winner's player id, not name, is passed as winner_id and
the loser's player id as loser_id. This will in turn update the appropriate database
entries.

swissPairings() - returns a list of touples of the format (player1 id, player1 name,
player2 id, player2 name) where each touple is the appropriate pairings for the next
round of tournament competition. This method assumes an even number of players are
registered for the tournament.

##License:
Project is freely open source under the terms of the
[MIT License](http://choosealicense.com/licenses/mit/)