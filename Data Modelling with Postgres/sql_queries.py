# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays
(songplay_id serial PRIMARY KEY NOT NULL, 
start_time timestamp NOT NULL, 
user_id text NOT NULL, 
song_id text NOT NULL, 
artist_id text, 
level text, 
session_id text,  
location text, 
user_agent text)
""")

user_table_create = ("""
CREATE TABLE users
(user_id int PRIMARY KEY NOT NULL, 
first_name varchar, 
last_name varchar,
gender varchar,
level text)
""")

song_table_create = ("""
CREATE TABLE songs
(song_id varchar PRIMARY KEY NOT NULL, 
title text, 
artist_id varchar,
year int, 
duration float)
""")

artist_table_create = ("""
CREATE TABLE artist
(artist_id text PRIMARY KEY,
name varchar, 
location text, 
latitude float,
longitude float)
""")

time_table_create = ("""
CREATE TABLE time_table
(start_time timestamp NOT NULL, 
hour int, 
day int,
week int, 
month int, 
year int, 
weekday text)
""")

# INSERT RECORDS

songplay_table_insert = (""" 
INSERT INTO songplays
(start_time, user_id, song_id, artist_id, session_id, level, location, user_agent)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s) 
""")

user_table_insert = ("""
INSERT INTO users
(user_id, first_name, last_name, gender, level)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level || 'free';
""")

song_table_insert = ("""
INSERT INTO songs
(song_id, title, artist_id, year, duration)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artist
(artist_id, name, location, latitude, longitude)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time_table
(start_time, hour, day, week, month, year, weekday)
VALUES(%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id FROM songs s, artist a
WHERE s.artist_id = a.artist_id  
    AND s.title = %s
    AND a.name = %s
    AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]