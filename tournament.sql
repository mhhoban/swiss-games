-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

CREATE TABLE player_registry (
    player_id serial PRIMARY KEY,
    player_name varchar(80)
);

CREATE TABLE tournament_matches (
    match_id serial PRIMARY KEY,
    winner int REFERENCES player_registry(player_id),
    loser int REFERENCES player_registry(player_id)
);


