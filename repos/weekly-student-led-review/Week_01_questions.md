## Week 1 Review Questions

1. What is `git`, and why is it useful to you as a Data Scientist?

2. What is the difference between `git` and `Github`?  What does `Github` provide 
   that is useful to you as a Data Scientist and developer?

3. There is a common `git` expression: 'ABC'.  What does it mean, and why is it 
   good advice?

4. What is Unix?  How has the Unix philosophy influenced software development?

5. You try to run an application, but are told that you don't have permission to
   access a certain file.  Describe the steps you would use to solve 
   this problem (allowing access to the file).

5. Compare and contrast functional and object oriented programming paradigms.  
    Then discuss the the 3 pillars of OOP and how they relate to Python.

6. What are some distinguishing characteristics of the Python programming 
   language?  

7. What are some differences between Python 2 and Python 3?  Why was Python 3
   developed?

8. List major data structures in Python.  Which data structure(s) would you use to
   in each of the following situations, and why:

  * Unchanging sales records

  * A customer database where changing information, such as address, email,
  and purchases are associated with a given customer name.

  * Driving waypoint locations between arbitrary points A and B.

  * The unique words used in a text corpus.

  * A search engine that returns results quickly for a given search term.

9. Write a one line list comprehension to perform the following matrix
   multiplication (A dot product B).  Describe how it works. How would you check
   it with NumPy?
```python
    A = [ [ 2, 4], [ 1, 7], [-1, 8] ]

    B = [ [3, 2, -5, 6],  [1, -3, 4, 8] ]
```

10. The `data` folder contains tweets from Elon Musk in March of 2017. Write a
    Python TweetData class to hold Elon's tweets.  The class should have at least two
    attributes: .raw and .cleanedtweets.  The .raw attribute should hold the raw data (3
    columns and 120 rows).  The .cleanedtweets attribute should only have 1 column
    (but still 120 rows) containing only lowercase alphanumeric characters present
    in the 3rd column of the raw tweets.  Feel free to use whatever additional 
    attributes or methods you need to make the class and an Elon Tweets object.

