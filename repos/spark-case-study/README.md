# Politics Makes Strange Bedfellows
In 2017, Emmanuel Macron and Marine Le Pen were the final two candidates in the French Presidential Election.  The two candidates had drastically different approaches to governing, and as such, the election was a major topic of discussion on Twitter.

## The Data
<a href="https://s3.us-east-2.amazonaws.com/jgartner-test-data/twitter/zippedData.zip">The data</a> you are provided a line delimited json file (746 MB) of tweets from France during that time period.  Your task is to leverage your understanding of Spark, visualization, and feature engineering to explore the dataset and provide answers to some basic questions.  

# Your Task
You and your team will have the task of reading in, cleaning, and exploring this dataset.  Your job is to gain insight into what is happening during the time period.  Your task for today is to produce the following:

1. A python script containing helper functions.
You should be working toward transforming this large cumbersome dataset into something that is regular and easily digestible.  You need to find inconsistencies in the data, and try to think about how you would clean them.  You can do cleaning in data as they are RDDs, DataFrames, or ideally both, but the processes should be calling function that are reusable.

2. A presentation about your choices.
Later this afternoon you'll stop work and get together as a class to present your findings.  You can either choose to use slides or jupyter notebooks.  The latter might be nice, because you may want to highlight bits of code.


## Hints
### 1. Non-UTF Characters
We suggest reading in the data into spark RDDs, not directly into Dataframes.  You can do so using the ```textFile``` command from the ```SparkContext```, and then getting python dictionaries using the ```json``` class.  If you do a ```take(1)```, it should work just fine.  If, however, you try to do a count, you'll end up throwing an error.  This happens because the ```json``` class fails when you encounter the non-utf8 characters in the dataset.  To get around this, you should wrap the json decoding in a ```try - except``` block, and return ```None``` if an exception is hit.  You can then filter out none.

### 2. Messy Data
This will be the most challenging dataset you've had to work with up to this point.  The data is somewhat large, and tweets are a complicated and messy source of information. Your first steps should be to understand which fields you'll be leveraging.  Once you've read in the data, start by doing a ```take(1)``` to get a feel for what a tweet JSON string looks like.

Also note that data is messy so you'll need to do a lot of checks and filter out inconsistent data.  <b>Being able to adjust based on error messages is an important skill, consider this a chance to practice!</b>

#### Repo Initially Forked from alro5921. Due to Forking Repo was Initially Private.
