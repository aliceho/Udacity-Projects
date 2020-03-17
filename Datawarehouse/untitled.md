# **Project 3: Data Warehouse**

## OBJECTIVE: 
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

## SCHEMA DEFINITION:
We have used Star Schema for the project because it loads the dimension tables without dependency between dimensions and so the ETL job is simpler and can achieve higher parallelism.
Below is the ERD diagram:
![Star Schema](https://r766469c826419xjupyterlr5tapor7.udacity-student-workspaces.com/files/star%20schema/image.png?_xsrf=2%7C3a81c7c5%7Cf50930d294ab9196f52a66362beed832%7C1575213746)
We have one fact table: 
1. songplays

and four dimension tables:
1. time
2. users
3. artists
4. song

We also have two staging tables:
1. staging_songs: item in song data JSON from S3 bucket
2. staging_events: item in log data JSON from S3 bucket

![Staging tables](https://r766469c826419xjupyterlr5tapor7.udacity-student-workspaces.com/files/star%20schema/image%20(1).png?_xsrf=2%7C3a81c7c5%7Cf50930d294ab9196f52a66362beed832%7C1575213746)

## STEPS INVOLVED TO RUN THE ETL PIPELINE:
1. Create a IAM role in aws with AmazonS3ReadOnlyAccess permission. Get the ARN and copy it in **dwh.cfg** file.
2. Create a Redshift cluster in aws. Get the endpoint, db name, port, username and password and copy it in **dwh.cfg** file.
3. Open the **sql_queries.py** file. This file reads the data in **dwh.cfg** file. In this file you will write code for:
    1. Dropping the tables if they exist.
    2. Creating the fact table, dimension tables and staging tables.
    3. Inserting the values into the fact table and dimension tables from the staging tables.
4. Now run the **create_tables.py** file. This is where you'll create your fact and dimension tables for the star schema in Redshift.
5. Check the table schemas in your redshift database. You can use Query Editor in the AWS Redshift console for this.
6. Run the **etl.py** file. This is where you'll load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.