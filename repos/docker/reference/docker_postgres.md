# Using Postgres with Docker
courtesy DSI Lead Instructor Moses Marsh  

Note: in the following instructions, `$` means your terminal shell prompt. `#` means the root shell prompt of the docker container, `=#` means the postgres shell prompt, where you can run SQL queries, and `>>>` means the python prompt.

## Starting the postgres server in a container

Let's create & start up a container with the official postgres image. Here I've named the container `pgserv`, but you can call it anything. 
```
$ docker run --name pgserv -d -p 5432:5432 -v "$PWD":/home/data -e POSTGRES_PASSWORD='password' postgres
```
- the `-d` flag means "run this container in the background"
- `-p 5432:5432` means "connect port 5432 from this computer (localhost) to the container's port 5432". This will allow us to connect to the Postgres server (which is inside the container) from services running outside of the container (such as python, as we'll see later).
  - Most services expect to find Postgres running on port 5432. If you have any previous installations of Postgres installed you may want to change this to 5435. If you do you will have to remember to specify what port to connect to working from your system.    
- the `-v` flag connects the filesystem in the container to your computer's filesystem. See the documentation for [docker volumes](https://docs.docker.com/storage/volumes/). 
  - Here, the container's folder `/home/data` will be mapped to whichever folder you ran the `docker run` command from (`$PWD`). If you want to make your entire home folder visible to the docker container, navigate to `~` before running the above command. If you only want the container to see, say, a folder you cloned from github, navigate to `/path/to/repo_folder` first. Any changes made to files in this folder are immediately visible to the container and your native file system. 
- the `-e` is setting up an enviroment variable which is the default password for postgres.  You most likely want to choose something better than the default `password` above.

In the future, you can start this container by using the `docker start` command
```bash
$ docker start pgserv
```

## Accessing the postgres terminal, [psql](http://postgresguide.com/utilities/psql.html)

`psql` is the command to open up a postgres terminal, and we need to run this command on inside the container. `docker exec` is the way to execute commands in a running container. See the documentation [here](https://docs.docker.com/engine/reference/commandline/exec/)
```
$ docker exec -it pgserv psql -U postgres
=# CREATE DATABASE yeah;
=# CREATE TABLE whatever ... ;
=# SELECT * FROM whatever
=# \q
$ 
```
- The `-it` option means we are executing the command `psql -U postgres` in "interactive mode", meaning we get to keep typing.

### If you already have psql on your machine

If you happen to have a postgres client already installed on your computer (and you'd probably know it if you did), you can treat the container as if it were  hosting a remote server, and connect to it from your terminal with
```
$ psql -U postgres -h localhost -p 5432
```

## Loading data into the server from a local file

Say we have a database dump on our machine called `really_important.sql`, and we'd like to load it into our containerized postgres server and run some queries on it. 

First, make sure the data file is in the folder that was mounted as a volume when you created the `pgserv` container. For example, if you ran the `docker run` command from `~`, make sure that `really_important.sql` is in some sub-folder of `~`. 

Suppose the data is in `~/path/to/data_dump/really_important.sql`. We can access it from the container as follows:
```
$ docker exec -it pgserv bash
# cd /home/data/path/to/data_dump/
# psql -U postgres
=# CREATE DATABASE new_database;
=# \q
# psql -U postgres new_database < really_important.sql;
# psql -U postgres new_database
=# \d
=# SELECT * FROM critical_table LIMIT 13;
```
Cool! Now you can explore your data using SQL. 

Composing queries in the terminal is awful, though. Use a text editor to compose your queries, then paste them into the terminal. Or set up [pgAdmin](https://www.pgadmin.org/download/) for an integrated browser experience.


## Accessing the Postgres Server with Python
You probably didn't love writing SQL queries in the psql shell. You longed for the days when you could just write a `for` loop in python and index into a tuple. Well now you can!

First install the python package [Psycopg2](http://initd.org/psycopg/docs/)
```
$ conda install psycopg2
```
The following code connects to the database and executes a query. Detailed explanations follow.
```
$ ipython
> import psycopg2 as pg2
> conn = pg2.connect(dbname='db_name', user='postgres', host='localhost', port='5432')
> cur = conn.cursor()
> query = '''SELECT * 
            FROM table_name 
            LIMIT 10;'''
> cur.execute(query)
> for row in cur:
    print(row)
> query_two =  '''SELECT * FROM other_table LIMIT 10;'''
> cur.execute(query_two)
> results = list(cur)
> conn.close()
> exit
$
```
- first we create a `connection` object, which requires the login information: the database name, the user name, the host (address) of the database, and the port to access it.
- the `connection` object has a `cursor` object associated with it. You can think of the `cursor` as the object carrying input & output between the server and the python client
- the `cursor` object has an `execute` method that sends queries to the server. 
- queries must be strings. it is helpful to use the three-single-quote string delimiter `'''`, as it allows for line breaks within the string.
- after a query has been executed, the `cursor` is a generator. Iterating over it will return one row of the result of the query at a time. 
- You can either iterate over the cursor, or, if you know the data is small enough, dump the entire generator into a list.
- At the end of your session (or script), you should close the connection with `conn.close()`

See more examples of how to use psycopg2 in [these notes](https://github.com/gSchool/DSI_Lectures/blob/master/sql-python/ivan_corneillet/sql_python_lecture_soln.ipynb)
