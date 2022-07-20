## Psycopg2 install guide for Ubuntu (16.04)

0) Make sure your system is up-to-date.
    ```bash
    $ sudo apt-get update
    $ sudo apt-get upgrade
    ```
1) Install Psycopg2, a Python wrapper for interfacing with Postgres SQL.
    
    a) Use conda to install psycopg2.
    ```bash
    $ conda install psycopg2
    ```
    b) Determine your host (where postgres is looking for a connection).
    ```bash
    $ sudo -u postgres psql -c "SHOW unix_socket_directories;"
    ```
    For me it was `/var/run/postgresql`.
    
    c) In another tab in your terminal, open your psql database.
    ```bash
    $ psql readychef
    ```
    d) In yet another tab in your terminal, start ipython.
    ```bash
    $ ipython
    ```
    e) In ipython, try to import psycopg2.
    ```bash
    In [1]: import psycopg2
    ```
    f) Within ipython, establish a connection with the `readychef` database.
    ```bash
    In [2]: conn = psycopg2.connect(dbname='readychef', user='frank', host = '/var/run/postgresql')
    ```
    Obviously your 'user' and 'host' may be different.
    
    g) Establish a cursor to your connection within ipython.
    ```bash
    In [3]: c = conn.cursor()
    ```
    
    h) To test, write a query:
    ```bash
    In [4]: query_example = '''SELECT * FROM events LIMIT 10;'''
    ```
    
    i) Execute the query.
    ```bash
    In [5]: c.execute(query_example)
    ```
    
    j) Save the query results to a variable within ipython.
    ```bash
    In [6]: results_q1 = c.fetchall()
    ```
    k) Print the results.
    ```bash
    In [7]: print results_q1
    ```
    l) Finally - important! - close your cursor.
    ```bash
    In [8]: c.close()
    ```

