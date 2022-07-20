# Docker  

## Introduction

Docker often makes installing and using applications easier than installing them natively on your laptop.  In this assignment you will use Docker to install and run
* Spark
* Postgres  
* MongoDB

which you will use later in the course.

In the `reference` folder you will find guides for installing and running each of these applications using Docker.

## Basic 

### Part 1: Installation and container setup
If you have not installed docker refer to the [setup guide here](reference/docker_setup.md) and the links in the readme to get it loaded on your system. 

Getting docker containers of the tools we will use in this course.  Take the time to read through the guides and understanding what each command is doing before starting to run commands on your computer. 

Note:  All guides below are written for Mac and Linux users and modifications to the instructions will need to be made for anyone running windows.
    
 * Follow [these instructions](reference/docker_spark.md) to get a Pyspark Jupyter Notebook container running.     
     
 
 * Follow [these instructions](reference/docker_postgres.md) to get a Postgres database running and import the `housing.sql` file.  You will know you have succeeded if you see output like below.    


    ```
    SET
    SET
    SET
    SET
    SET
    SET
    SET
    CREATE EXTENSION
    COMMENT
    SET
    SET
    SET
    CREATE TABLE
    CREATE TABLE
    COPY 775
    COPY 4884
    REVOKE
    REVOKE
    GRANT
    GRANT
    ```
    
   
 * Follow [these instructions](reference/docker_mongodb.md) to get a Mongo database running connect to it and load the `coffee-tweets.json` file.  You will know you succeeded when you get the below message.    
    ```
    2019-12-12T21:42:23.903+0000	connected to: mongodb://localhost/    
    2019-12-12T21:42:23.958+0000	122 document(s) imported successfully. 0 document(s) failed to import.
    ```

## Advanced

### Part 2: Tutorials
Docker has made some beginner tutorials on Github at [https://github.com/docker/labs/tree/master/beginner](https://github.com/docker/labs/tree/master/beginner).
Your assignment is to complete Tutorials 1 and 2:  
* 1 [Running your first container](https://github.com/docker/labs/blob/master/beginner/chapters/alpine.md)
* 2 [Webapps with Docker](https://github.com/docker/labs/blob/master/beginner/chapters/webapps.md)

## Extra credit

### Part 3: Creating an image
Create a Docker Image that you can use to re-create your current Python data science environment.  At a minimum, you'll probably want to specify an Operating System and Anaconda's distribution of Python 3.  Look for resources on Docker Hub.  

