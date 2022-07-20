## SQL breakout database creation guide

You need to import the data in the `degrees_data.csv`, `student_data.csv`, and `term_gpa_data.csv` into PostgreSQL.  These csvs are located in the `data` folder.  A script that contains a schema has been provided (`make_db_script.sql`) to help you do this.  Make a PostgreSQL database called `sql_for_ds` using this script and the directions below.

Your database creation instructions depend on your operating system.

### Linux

1) From terminal in the same directory as this file, start postgres:  
   ```bash
   $ sudo -i -u postgres
   ```
2) Make the `sql_for_ds` database:  
   ```bash
   $ createdb sql_for_ds
   ```
3) Exit postgres:  
   ```bash
   $ exit
   ```
4) Open the `make_db_script.sql` file with a text editor and inspect the contents.  Note how the schemas are created.  Find the paths to the `degrees_data.csv`, `student_data.csv`, and `term_gpa_data.csv` and change them to what they are on your machine. Save the file and close it.

5) Use the `make_db_script.sql` file to import data into the `sql_for_ds` database that you made.
   ```bash
   $ psql sql_for_ds < make_db_script.sql
   ```  
   At this point you should see a list of commands go by:  `BEGIN SET CREATE TABLE etc`  
6) Open the database you just made:  
   ```bash
   $ psql sql_for_ds
   ```
7) Try out some of the psql cheatsheet commands in `psql_commands.png`  

8) Try writing queries to answer the questions contained in `queries.sql`

### MacOS


1) Go to the Dock, click on the Applications folder, find the Postgres.app icon (big blue elephant) and click it.  
2) In the window that pops up, click on *Open psql*.  My version of psql is 9.6.1.  Newer versions of postgreSQL may start up differently.  Just find a way to see the psql terminal referenced below. 
3) In the psql terminal, type:  
   ```bash
   # CREATE DATABASE sql_for_ds; 
   ```
   **The ending semicolon is very important!**  
4) In terminal navigate to where the `make_db_script.sql` file is (it's in the same folder as this document) and open it with a text editor. Inspect the contents.  Note how the schemas are created.  Find the paths to the `degrees_data.csv`, `student_data.csv`, and `term_gpa_data.csv` and change them to what they are on your machine. Save the file and close it.

5) Use the `make_db_script.sql` file to import data into the `sql_for_ds` database that you made.
   ```bash
   $ psql sql_for_ds < make_db_script.sql
   ```  
   At this point you should see a list of commands go by:  `BEGIN SET CREATE TABLE etc`  
6) Open the database you just made:  
   ```bash
   $ psql sql_for_ds
   ```
7) Try out some of the psql cheatsheet commands in `psql_commands.png`  

8) Try writing queries to answer the questions contained in `queries.sql`



