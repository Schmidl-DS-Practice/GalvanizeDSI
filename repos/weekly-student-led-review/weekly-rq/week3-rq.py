##1
#O(n**2)
import numpy as np
from time import time 


def timeit(fn):
    def timed(*args, **kw):
        ts = time() 
        fn(*args, **kw) 
        te = time()

        return te - ts 

    return timed

@timeit
def find_duplicates(l1, l2):
  '''
  searches through lists 1 and 2 and eliminates duplicate entries from list 2
  '''
  for item1 in l1:
    for item2 in l2:
      if item2 == item1:
        # removes item from list
        l2.remove(item2)
  return l1, l2

#print(find_duplicates(l1=list(np.random.randint(0, 100, 50)), l2=list(np.random.randint(0, 100, 50))))

@timeit
def find_dups(l1, l2):
    return [set(l1 + l2)]

#print(find_dups(l1=np.random.randint(0, 100, 50), l2=np.random.randint(0, 100, 50)))

##2
'''It provides cross platform useability.
   Bypass having to install dependencies that might conflict between operationg systems.
   Make an image that has requirments installed for application and send to docker'''

##3
'''The access key and secret access key are in the script and
   can be sent around the world'''

##4

query = 
    '''WITH temp_table AS (
    '''
   
'''SELECT city, cust_id
   FROM customers
   WHERE 
   GROUP BY cust_id
'''

##5
'''
SQL has a schema
NOSQL has no schema. Bunch of dictionaries with key, values
'''
##6
'''velocity, volume, variety
'''

##7
'''
Grouping and removing duplicates
'''

##8
'''RDDs are immutable. Transformation is not performed until actions is done.
   Creates a new RDD.'''

##9
'''RDD is immutable.
'''
##10
'''Cluster manager uses partitioning to create multiple RDDs.
   Transformation sits in lazy eval. DAG decides who to send it too(a map).
   Cluster manager utillizes the DAG and direct worker nodes(machines that do work in case one breaks).
'''