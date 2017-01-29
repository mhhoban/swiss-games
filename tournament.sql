-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--DROP DATABASE IF EXISTS tournament;
--CREATE DATABASE tournament;
--\c tournament

CREATE TABLE player_registry (
    player_id serial PRIMARY KEY,
    player_name varchar(80)
);

CREATE TABLE tournament_matches (
    match_id serial PRIMARY KEY,
    winner int REFERENCES player_registry(player_id),
    loser int REFERENCES player_registry(player_id)
);

CREATE VIEW winners as
SELECT a.player_id, a.player_name, COUNT(b.winner) as wins
FROM player_registry AS a, tournament_matches AS b
WHERE a.player_id = b.winner
GROUP BY player_id
ORDER BY wins DESC;

CREATE VIEW matches as
SELECT a.player_id, a.player_name, COUNT(b.winner) as match_num
FROM player_registry AS a, tournament_matches AS b
WHERE a.player_id = b.winner or a.player_id = b.loser
GROUP BY player_id;

CREATE VIEW standings as
SELECT a.player_id, a.player_name, b.wins, c.match_num
FROM player_registry AS a, winners AS b, matches AS c
WHERE a.player_id = b.player_id and b.player_id = c.player_id
ORDER BY wins DESC;