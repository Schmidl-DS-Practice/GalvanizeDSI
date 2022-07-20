## Week 3 Review Answers

1. Estimate the run-time complexity (O(N) notation) of the following code:
  ```python
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
  ```
  Write another function with the same functionality that works more efficiently. Use timeit to see how well you can do!

  (Hint: you could use something like
  ```np.random.randint(0, 100, 50)```
  to create random lists to practice with)

Runtime complexity for the original function is O(n*m) where n amd m are the length of the lists. To avoid the double for loop, use the set datatype! Sets use hashing for lookup and so the lookup is one step instead of n steps. Using sets is ~2 orders of magnitude faster for a list of length 500.

  ```python
  # create random lists of numbers
  lsta = np.random.randint(0, 500, 500).tolist()
  lstb = np.random.randint(0, 500, 500).tolist()

  # new function using sets
  def find_duplicates_fast(l1, l2):
    setb = set(l2)
    dedup = setb - setb.intersection(set(l1))
    return l1, list(dedup)

  In [236]: timeit find_duplicates(lsta.copy(), lstb.copy())
  100 loops, best of 3: 7.59 ms per loop

  In [237]: timeit find_duplicates_fast(lsta.copy(), lstb.copy())
  10000 loops, best of 3: 42.6 µs per loop
  ```

2. Docker has become a common way to deploy applications.  Why is that?  Let's 
   say you have an application you wish to deploy. What steps would you go through
   to make your application deployable with Docker?  

   Docker allows application "containers" that are guaranteed to work the same 
   way on other operating systems and in different environments assuming that
   that Docker is installed and the container is running on the Docker engine.  

   To make a deployable application with Docker, you'd start with a text file
   called a Dockerfile that contains instructions for how to build the environment.
   You'd use Docker to build that Dockerfile into a Docker image, and you'd push
   the image to Docker Hub.  Then, wherever you wanted the application to run 
   you would first install Docker, then pull the image from Docker Hub.  You
   would then run the image to make a container containing your application,
   and it should work!

3. As you pair program, your partner puts this in your script:

```python
   import boto3
   boto3_connection = boto3.resource('s3')

   AWS_ACCESS_KEY_ID=ZYBGIZH66RA468VYYPCQ
   AWS_SECRET_ACCESS_KEY=gV97XiVqsSH5YhGAx18m0b/gxJdyH-yXS

   def print_s3_contents_boto3(connection):
       for bucket in connection.buckets.all():
           for key in bucket.objects.all():
               print(key.key)

   print_s3_contents_boto3(boto3_connection)
```

   The code works, but you can't shake a feeling of impending doom.  Why?  What would
   you do to allow the code to work but prevent financial ruin?

   NEVER put keys to services in your code.  Especially in the case of AWS, bots
   are constantly searching for keys in repos, and will use them to automatically
   spin up services that you will be charged for.

   In this case, access key could have been exported to the environment in the 
   `.bashrc/.bash_profile` and then Python `os` module could have used, e.g.
   `os.environ['AWS_ACCESS_KEY_ID']`, to bring the values for the keys
   into the Python script.


4. Use datatable 'customers' (example rows below), write a SQL query to....

| cust_id | cust_name | current_city | hometown |
|:----------:|:------------:|:----------:|:-----------:|
| 1 | Amanda | Atlanta | Raleigh |
| 2 | Brittany | Denver | New York |
| 3 | Charles | Paris | Raleigh |
| 4 | David | San Diego | Los Angeles |
| 5 | Elizabeth | Atlanta | London |
| 6 | Greg | Denver | Atlanta |
| 7 | Maria | Raleigh | New York |
| 8 | Sarah | New York | Raleigh |
| 9 | Thomas | Atlanta | Raleigh |

  **Assume that everyone has moved**

  A) Return the city with the highest population growth. (Highest net of people who currently live there minus people who used to live there)

  ```SQL
  CREATE TABLE inward_migration AS
  (SELECT current_city, COUNT(*) AS net_in
  FROM customers
  GROUP BY current_city)

  CREATE TABLE outward_migration AS
  (SELECT hometown, COUNT(*) AS net_out
  FROM customers
  GROUP BY hometown)

  SELECT a.current_city AS city,
    a.net_in - b.net_out AS net_immigration
  FROM inward_migration a
  JOIN outward_migration b
  ON a.current_city = b.hometown
  ORDER BY net_immigration DESC
  LIMIT 1
  ```
  
  B) Return pairs of "friends" (can be two columns or a tuple) that have both the same hometown and current city. Remove duplicates!  

  ```SQL
  SELECT a.cust_id AS friend1, b.cust_id AS friend2
  FROM customers a
  JOIN customers b
  ON a.hometown = b.hometown
  AND a.current_city = b.current_city
  WHERE a.cust_id < b.cust_id
  ```

5. Compare/contrast SQL and noSQL databases.  
  * What is one major organizational difference between the two? 
  * What type of data are ideal for each?  
  * In SQL, you have tables, rows, and columns.  What are analogous in MongoDB? 


  SQL and NoSQL are similar in that they store information.  However, SQL 
  databases are relational, meaning that there are relationships between entities
  in separate tables, while in NoSQL data of multiple types are stored in documents
  that are not related.  As SQL databases are more structured they require a schema:
  a defined relation between tables and columns in tables - before data can be
  stored in them, while in NoSQL databases this is not the case.  

  Ideal data types:  
  SQL - structured, "clean", unchanging  
  NoSQL - unstructured, changing with time

  Collections, documents, and fields in MondoDB are analogous to tables, rows, and 
  columns in SQL.

6. What is big data?  Big data are often referred to by 3Vs.  What are they?  

   Big data are data too large to fit on one computer (high Volume), often 
   of a mixture of formats(high Variety, like simultaneous images and text),
   and sometimes at high speed(high Velocity, like 500,000 tweets per day).

7. Explain the concept of MapReduce in terms a 5th grader would understand. 
   Provide an illustrative example.

   Say there is an Easter egg hunt and you want to count the number of colored
   eggs in the front and back yards.  You know there are red, green, blue, and
   purple hidden colored eggs.  You get 8 kids, and assign 2 kids to counting
   each color, with one kid searching the front yard and the other kid searching
   the back yard.  You do that for all the colors.  Then you ask the kids to
   bring their count to you at the end, so you can add up the results.

   In this example, the "Map" function was each kid going to the data in a 
   data partition (the front of back yard) and counting the number of eggs
   of a certain color, and then you performed the "Reduce" function when you
   added the results for each color together at the end.

8. What differentiates a Spark RDD from data stored in a single file (e.g. a .csv)?  

   The major difference is that a Spark RDD is a Resilient Distributed Database,
   where the data are backed up (Resilient) and split into distributed partitions
   (Distributed).

9. What is the difference between a Spark RDD and a Spark Dataframe?  
   
   A dataframe has a schema.

10. Let's say one computer in you Spark cluster fails, but you still get results.
    How did Spark do this?!?  Your answer should include terms **RDD**, **Partition**, 
    **immutable**, **DAG**, **Lazy Evaluation**, **Spark Context**, 
    **Cluster Manager**, and **Worker Node**.  

    Data in Spark are stored in RDDs, where RDDs are multiple, redundant partitions
    of the data split up into discrete blocks.  The data in each partition is immutable,
    meaning that it's unchanging. 

    When you interact with Spark, you work with a Spark Context to set up a series of
    transformations of your data. This forms a graphical mathematical construct called
    a Directed Acyclic Graph (DAG). Nothing happens to the data as you set up the DAG
    (called Lazy Evaluation), so if there are errors in your transformations you won't
    know until you call an action to get resuls.

    In the case of recovering from an error processing a part of the RDD on one of the
    Worker Nodes, the Cluster Manager will get notification that there is an error and
    then spin up another worker node to process the block of the RDD that was present 
    on the defective worker node.  Because the data are immutable, the same DAG can
    be applied to process that partition and return results.
