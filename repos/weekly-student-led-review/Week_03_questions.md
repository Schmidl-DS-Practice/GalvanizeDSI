## Week 3 Review Questions

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


2. Docker has become a common way to deploy applications.  Why is that?  Let's 
   say you have an application you wish to deploy. What steps would you go through
   to make your application deployable with Docker?  


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

  B) Return pairs of "friends" (can be two columns or a tuple) that have both the same hometown and current city. Remove duplicates!  

5. Compare/contrast SQL and noSQL databases.  
  * What is one major organizational difference between the two?  
  * What type of data are ideal for each?  
  * In SQL, you have tables, rows, and columns.  What are analogous in MongoDB? 

6. What is big data?  Big data are often referred to by 3Vs.  What are they?

7. Explain the concept of MapReduce in terms a 5th grader would understand. 
   Provide an illustrative example.

8. What differentiates a Spark RDD from data stored in a single file (e.g. a .csv)?  

9. What is the difference between a Spark RDD and a Spark Dataframe?  

10. Let's say one computer in you Spark cluster fails, but you still get results.
    How did Spark do this?!?  Your answer should include terms **RDD**, **Partition**, 
    **immutable**, **DAG**, **Lazy Evaluation**, **Spark Context**, 
    **Cluster Manager**, and **Worker Node**.
