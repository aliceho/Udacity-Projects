Project1:Data Modelling with Postgres

This project helps us practice the following concepts:
•	Data modeling with Postgres
•	Creating Databases 
•	Creating a ETL pipeline using python

Context:
Sparkify is a music streaming startup that wants to analyze the collection of songs and user activity on their app.

Challenge:
Currently they do not have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app as well as a directory with JSON metadata on the songs in their app.

Data:
•	Song datasets: all json files are nested in subdirectories under /data/song_data. 
•	Log datasets: all json files are nested in subdirectories under /data/log_data.

Database Schema:
We use STAR SCHEMA for this project: there is one main fact table containing all the measures associated to each event and 4 dimentional tables. We are designing with star schema because in a star schema, only single join creates the relationship between the fact table and any dimension tables and also because the amount of data we need to analyze is not big enough to require big data related solutions.

Fact Table:
Songplays: songplay_id, start_time, user_id, song_id, artist_id, level, session_id, location, user_agent

Dimension Tables:
users – user_id, first_name, last_name, gender, level
songs – song_id, title, artist_id, year, duration
artist – artist_id, name, location, latitude, longitude
time – start_time, hour, day, week, month, year, weekday
Project structure
Files used on the project:
1.	Data: needed jsons reside.
2.	sql_queries.py: use to write sql queries to drop, create and insert into a table.
3.	create_tables.py: drops and creates tables. 
4.	test.ipynb: displays the first few rows of each table.
5.	etl.ipynb:  a guided path which helps us to read and process a single file from song_data and log_data and load the data into your tables.
6.	etl.py: writing the code from etl.ipynb and executing it.
7.	README.md: documentation for the project.
Steps followed:
1.	Write DROP, CREATE and INSERT query statements in sql_queries.py
2.	Run in console: python create_tables.py
3.	Follow the instructions and complete etl.ipynb Notebook to create the blueprint of the pipeline to process and insert all data into the tables.
4.	Once verified that base steps were correct by checking with test.ipynb, filled in etl.py program.
5.	Run etl in console, and verify results: python etl.py
ETL pipeline
Prerequisites:
•	Database and tables created

1.	We load the file as a dataframe using a pandas function called read_json().
2.	For each row in the dataframe we select the fields we are interested in: song_data = [song_id, title, artist_id, year, duration] and  artist_data = [artist_id, artist_name, artist_location, artist_longitude, artist_latitude] And finally we insert this data into their respective databases.
3.	Once all files from song_data are read and processed, we move on processing log_data.
4.	We repeat step 2, but this time we send our files to function process_log_file.We load our data as a dataframe same way as with songs data.We select rows where page = 'NextSong'.We convert ts column where we have our start_time as timestamp in millisencs to datetime format. We obtain the parameters we need from this date (day, hour, week, etc), and insert everythin into our time dimentional table.
5.	Next we load user data into our user table
6.	Finally we lookup song and artist id from their tables by song name, artist name and song duration that we have on our song play data. The last step is inserting everything we need into our songplay fact table.

