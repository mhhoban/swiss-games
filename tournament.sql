-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE names_table (
    player_id serial PRIMARY KEY,
    player_name varchar(80)
);

CREATE TABLE wins_table (
    player_id integer PRIMARY KEY,
    wins integer
);

CREATE TABLE matches_table (
    player_id integer PRIMARY KEY,
    matches integer
);

