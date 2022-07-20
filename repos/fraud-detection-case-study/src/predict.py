import _pickle as pickle
from datacleanup import data
import psycopg2
import os
import requests
import pandas as pd

#heroku stuff
# DATABASE_URL = os.environ['http://galvanize-case-study-on-fraud.herokuapp.com/data_point']
URL = 'http://galvanize-case-study-on-fraud.herokuapp.com/data_point'
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

r = requests.get(url=URL)
d = r.json()
data = pd.Series(d)

# with open('model.pkl') as f_un:
#     model_unpickled = pickle.load(f_un)

# lab = model_unpickled.predict(data)
#     labelprobability = model_unpickled.predictproba(data)

try:
    conn = psycopg2.connect(user = 'postgres',
                            host = 'localhost',
                            password='password',
                            port = '5432',
                            dbname='predictions')
    cur = conn.cursor()
    create_table_query = '''CREATE TABLE predictions
                            (ID INT PRIMARY KEY NOT NULL,
                            DATA TEXT NOT NULL,
                            LABEL TEXT NOT NULL);'''
    cur.execute(create_table_query)
    conn.commit()
    print('Table created successfully in PostgreSQL')
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn:
        cur.close()
        conn.close()

# def insert_sql(datapoint, lab)
#     sql = ''' INSERT INTO predictions(data)
#                 VALUES(%s) RETURNING label;'''
#     conn = None
#     label = None
#     try:
#         params = config()
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         cur.execute(sql, (datapoint,))
#         label = lab 
#         conn.commit()
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#     return label

# insert_sql(data, lab)

print(data)