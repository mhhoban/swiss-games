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


CREATE VIEW winners AS
SELECT a.player_id, a.player_name, COUNT(b.winner) as wins
FROM player_registry as a LEFT JOIN tournament_matches as b
ON a.player_id = b.winner
group by player_id;

CREATE VIEW matches AS
SELECT a.player_id, a.player_name, COUNT(b.winner) AS match_num
FROM player_registry AS a LEFT JOIN tournament_matches AS b
ON a.player_id = b.winner OR a.player_id = b.loser
GROUP BY player_id;

CREATE VIEW standings AS
SELECT a.player_id, a.player_name, a.wins, b.match_num
FROM matches AS b LEFT JOIN winners AS a
on a.player_id = b.player_id
ORDER BY wins DESC;

