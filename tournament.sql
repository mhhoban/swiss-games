-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE player_registry (
    player_id serial PRIMARY KEY,
    player_name varchar(80)
);

CREATE TABLE player_wins (
    player_id serial PRIMARY KEY,
    wins integer
);

CREATE TABLE player_matches (
    player_id serial PRIMARY KEY,
    matches integer
);

