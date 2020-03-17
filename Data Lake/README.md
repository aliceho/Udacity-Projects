# Project 4 : Data Lake with Apache Spark

## OBJECTIVE:
A music streaming startup, Sparkify, has grown their user base and song database even more and want to move their data warehouse to a data lake. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables. This will allow their analytics team to continue finding insights in what songs their users are listening to.

## Project Datasets
You'll be working with two datasets that reside in S3. Here are the S3 links for each:

>Song data: s3://udacity-dend/song_data

>Log data: s3://udacity-dend/log_data

## Schema for Song Play Analysis
Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

Fact Table:

>songplays - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Dimension Tables:

>users - user_id, first_name, last_name, gender, level

>songs - song_id, title, artist_id, year, duration

>artists - artist_id, name, location, lattitude, longitude

>time - start_time, hour, day, week, month, year, weekday

![ERD](https://r766469c826427xjupyterlx8knk8rj.udacity-student-workspaces.com/files/star%20schema/star_schema.png?_xsrf=2%7Cd7a6bfaa%7C69fa01002d686693cca75e3eaa9407c4%7C1575418212)

## Steps to Follow:
1. Fill in your AWS Credentials in dl.cfg
2. In etl.py we will read data from S3 (song data and log data), 