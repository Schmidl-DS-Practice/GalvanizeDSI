# Spark RDDs

## Basic
### Part 1: RDD and Spark Basics

Here we will get familiar with the basics of Spark via the Spark Python API,
`pyspark` module in python. For now, we will be just working with a single node that will
parallelize processes across all of our cores (rather than distributing them
across worker nodes).

1\. Initiate a `SparkSession`. A `SparkSession` embeds both a `SparkContext` and a `SQLContext` to use RDD-based and DataFrame-based functionalities of Spark. Specify your `SparkSession` as follows.

```python
import pyspark as ps

spark = (ps.sql.SparkSession.builder 
        .master("local[4]") 
        .appName("morning sprint") 
        .getOrCreate()
        )
```

Create a variable `sc` using the following line. It will let you use `sc` as a `sparkContext` for compatibility with pre-2.0 RDD-based spark commands.

```
sc = spark.sparkContext
```

2\. Spark operates in **[Resilient Distributed Datasets](http://spark.apache.org/docs/latest/programming-guide.html#resilient-distributed-datasets-rdds) (RDDs). An RDD is
a collection of data partitioned across machines**. RDDs allow the processing
of data to be parallelized due to the partitions. RDDs can be created from
a SparkContext in two ways: loading an external dataset, or by parallelizing
an existing collection of objects in your currently running program (in our
Python programs, this is often times a list).

* Create an RDD from a Python list.

```python
lst_rdd = sc.parallelize([1, 2, 3])
```

* Read an RDD in from a text file. **By default, the RDD will treat each line
as an item and read it in as string.**

```python
file_rdd = sc.textFile('data/cookie_data.txt')
```

3\. Now that we have an RDD, we need to see what is inside. RDDs by default will
  load data into partitions across the machines on your cluster. This means that
  you can quickly check out the first few entries of a potentially enormous RDD
  without accessing all of the partitions and loading all of the data into memory.

```python
file_rdd.first() # Returns the first entry in the RDD
file_rdd.take(2) # Returns the first two entries in the RDD as a list
```
4\. To retrieve all the items in your RDD, every partition in the RDD has to be
  accessed, and this could take a long time. In general, before you execute
  commands (like the following) to retrieve all the items in your RDD, you
  should be aware of how many entries you are pulling. Keep in mind that to
  execute the `.collect()` method on the RDD object (like we do below), your entire
  dataset must fit in memory in your driver program (we in general don't want
  to call `.collect()` on very large datasets).

  The standard workflow when working with RDDs is to perform all the big data
  operations/transformations **before** you pool/retrieve the results. If the
  results can't be collected onto your driver program, it's common to write
  data out to a distributed storage system, like HDFS or S3.

  With that said, we can retrieve all the items from our RDD as follows:

```python
file_rdd.collect()
lst_rdd.collect()
```

### Part 2: Intro to Functional Programming

Spark operations fit within the [functional programming paradigm](https://en.wikipedia.org/wiki/Functional_programming).
In terms of our RDD objects, this means that our RDD objects are immutable and that
anytime we apply a **transformation** to an RDD (such as `.map()`, `.reduceByKey()`,
or `.filter()`) it returns another RDD.

Transformations in Spark are lazy, this means that performing a transformation does
not cause computations to be performed. Instead, an RDD remembers the chain of
transformations that you define and computes them all only when and action requires
a result to be returned.

**Spark notes**:

  * A lot of Spark's functionalities assume the items in an RDD to be tuples
  of `(key, value)` pairs, so often times it can be useful to structure your
  RDDs this way.
  * Beware of [lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation), where transformations
  on the RDD are not executed until an **action** is executed on the RDD
  to retrieve items from it (such as `.collect()`, `.first()`, `.take()`, or
  `.count()`). So if you are doing a lot transformations in a row, it can
  be helpful to call `.first()` in between to ensure your transformations are
  running properly.
  * If you are not sure what RDD transformations/actions there are, you can
  check out the [docs](https://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD).

**Steps**:

1\. Turn the items in `file_rdd` into `(key, value)` pairs using `.map()`. In order to do that, you'll find a template function `parse_json_first_key_pair` in the `spark_intro.py` file. Implement this function that takes a json formatted string (use `json.loads()`) and output the key,value pair you need. Test it with the string `u'{"Jane": "2"}'`, your function should return `(u'Jane', 2)`. **Remember to cast value as type** `int`.


2\. Now use `.filter()` to look for entries with more than `5` chocolate chip cookies.

3\. For each name, return the entry with the max number of cookies.

**Hint**:
* Use `.reduceByKey()` instead of `.groupByKey()`. See why [here](https://databricks.gitbooks.io/databricks-spark-knowledge-base/content/best_practices/prefer_reducebykey_over_groupbykey.html).
* You may get a warning saying that you should install `psutil`. You can with
`pip install psutil`.

4\. Let's show the first results using `.sortBy()` and `.take()`. `.sortBy()` requires a lambda function that outputs the value/quantity on which we want to sort our rows. Because we currently have only one value, you will use **`lambda (k, v): v`** or **`lambda x: x[1]`** (they are equivalent).

5\. Calculate the total revenue from people buying cookies (we're assuming that
each cookie only costs $1).

**Hint**:
* `rdd.values()` returns another RDD of all the values.
* Use `.reduce()` to return the sum of all the values.

## Advanced
### Part 3: Spark for Data Processing

  We will now explore some airline data. We will walk through the steps of doing this on a AWS EMR cluster but you can do it locally as well.  If you do it on the EMR you will want to place the data in an s3 bucket and make sure to give your EMR a IAM roll with access to s3. 

  - [Read here](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html) about EMR and how to set up a cluster and get a running notebook.

  - As you will be working in the cloud you will want to place your data into an s3 bucket. You can follow [these instructions](https://docs.aws.amazon.com/quickstarts/latest/s3backup/step-1-create-bucket.html).  The file can be found in your data folder.

  - Make sure you assign a IAM role with when creating the cluster so you have access to our data. [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).  Make sure the role has `AmazonS3FullAccess`

#### 3.1: Loading Data from an S3 bucket
  1\. Load the data from S3 as follows.

```python
link = 's3a://<your_bucket_name>/airline-data-extract.csv'
airline_rdd = sc.textFile(link)
```

**Reminder**: If you get an error make sure you have an IAM assigned that has s3 access.


---

2\. Print the first 2 entries with `.take(2)` on `airline_rdd`. The first entry is the column names and starting with the second we have our data.

3\. Now run `.count()` on the RDD. 


#### 3.2: Create a pipeline on a sub-sample dataset

Now we can move on to looking at the data and transforming it. In this section we will operate only on a limited data set, develop a full pipeline and later on execute that on the full scale data.

We want to identify airports with the worst / least delays. Consider the following about delays:

* **2 types of delays:** Arrival delays, `ARR_DELAY`, and departure delays, `DEP_DELAY`.
* All delays are in terms of **minutes**.
* Arrival delays are associated with the destination airport, `DEST_AIRPORT_ID`.
* Departure delays are associated with the origin airport, `ORIGIN_AIRPORT_ID`.


1\. As you just saw the `.count()` action takes a long time to run. More involved commands can take even longer. In order to not waste time when writing/testing your code, it's common practice to work with a sub-sample of your data until you have your code finalized/polished and ready to run on the full dataset. Use `.take(100)` to sample out the first 100 rows and assign it to a new RDD using `sc.parallelize()`.

2\. Let's do some preprocessing and parsing. You may have noticed that those rows are in fact csv lines. We are going to parse those lines one by one and output a list of the values we can split from those lines.

In order to do that, we've written the function `split_csvstring` in the `spark_intro.py` file employing the `csv` module function `csv.reader()` and the `StringIO` module.

Test it with the string `'a,b,0.7,"Oct 7, 2016",42,'`, your function should return `['a', 'b', '0.7', 'Oct 7, 2016', '42', '']`

Use `.map()` to apply it to your RDD. Print the first 2 lines, with `take(2)`, to confirm the rows have been cleaned correctly. The first 2 lines should look like the following.

```
[['YEAR', 'MONTH', 'UNIQUE_CARRIER', 'ORIGIN_AIRPORT_ID', 'DEST_AIRPORT_ID', 'DEP_DELAY', 'DEP_DELAY_NEW', 'ARR_DELAY', 'ARR_DELAY_NEW', 'CANCELLED', ''],
['2012', '4', 'AA', '12478', '12892', '-4.00', '0.00', '-21.00', '0.00', '0.00', '']]
```

3\. Use `filter()` with a `lambda` function to filter out the line containing the column names. Keep that line in a variable so that you can use in next question.

4\. Write a function `make_row_dict()`, that takes a row (list of values) as an argument and returns a dictionary where the keys are column names and the values are the values for the column. Follow the specifications below to make your dictionary.

The dictionary will only keep track of the following columns:

`['DEST_AIRPORT_ID', 'ORIGIN_AIRPORT_ID', 'DEP_DELAY', 'ARR_DELAY']`
* Cast the values for `DEP_DELAY` and `ARR_DELAY` as floats. These values
correspond with delay lengths in minutes.
* Subtract `DEP_DELAY` from `ARR_DELAY` to get the actual `ARR_DELAY`.
* If a flight is `CANCELLED`, add 5 hours, 300 minutes, to `DEP_DELAY`.
* There are missing values in `DEP_DELAY` and `ARR_DELAY` (i.e. `''`) and
 you would want to replace those with `0.0`.

You'll find a template function `make_row_dict` in the `spark_intro.py` file with a `doctest` you can try to make it work, using `python -m doctest -v spark_intro.py`.

Now use `.map()` with your function  `make_row_dict()` over your RDD to make a new RDD made of dictionaries.

5\. Now we will use these dictionaries to create 2 RDDs, where the items are tuples. Remember, much of Spark's functionality assumes RDDs to be storing (key, value) tuples. You can `.map()` to create those RDDs using `lambda` functions applied to the RDD generated in 4.

The first RDD will contain tuples `(DEST_AIRPORT_ID, ARR_DELAY)`. The other RDD will contain `(ORIGIN_AIRPORT_ID, DEP_DELAY)`. Run a `.first()` or `.take()` to confirm your results.

6\. Using the two RDDs you just created, make 2 RDDs with the mean delay time for each origin airports and each destination airports. You will need to `.groupByKey()` and then take the mean of the delay times for each airport. Use `.mapValues()` to calculate the mean of each group's values.

This is where having our RDDs be composed of `(key, value)` pairs is relevant.
It allows us to use the `.groupByKey()` method on our RDD.

**Note:** There is a slightly more performant way of calculating the mean which uses
`.aggregateByKey()` rather than `.groupByKey()`. This transformation models the combiner
model that we saw in Hadoop. Unfortunately, the documentation for `.aggregateByKey()` is
quite poor. Check out [this](http://stackoverflow.com/a/29930162) stack overflow post
for a good description for how to use it.

7\. Run `.cache()` on the RDDs you just made. Remember to set the name of the RDD using `.setName()` before running `.cache()` (e.g. `rdd.setName('airline_rdd').cache()`). Setting the name will allow you to identify the RDD in the Spark web UI (see extra credit).

When you cache the RDDs, you make sure that computations which produced them don't
need to be performed every time they are called upon. It is good practice to use `cache()`
for RDDs that you are going to repeatedly use.

8\. Perform appropriate actions on your RDDs to answer the following questions:

* Q1: What are the top 10 departing airports that have the lowest average delay?
* Q2: What are the top 10 departing airports that have the highest average delay?
* Q3: What are the top 10 arriving airports that have the lowest average delay?
* Q4: What are the top 10 arriving airports that have the highest average delay?

There are a couple of ways that you can do this. One is by using `sortBy()` and then
`take(10)`. However, this is not the most efficient way. Why not?

The other way, more efficient way to answer this question is with `takeOrdered()`.
You'll have to be a little clever to get the highest delays. Check out the
[docs](https://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.RDD.takeOrdered)
for a hint.

You'll need to run all the transformations that you tested on the smaller dataset
on the full data set to answer these questions.


