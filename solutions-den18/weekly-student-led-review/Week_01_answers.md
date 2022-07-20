## Week 1 Review Answers

1. What is `git`, and why is it useful to you as a Data Scientist?  
   Git is a free and open source distributed version control system. It's useful
   to Data Scientists as a way to track changes in code and collaborate on
   software projects.

2. What is the difference between `git` and `Github`?  What does `Github` provide 
   that is useful to you as a Data Scientist and developer?  
   Git is a version control system, while Github is a hosting service for Git
   repositories.  Github allows remote repositories on the web which faciliate
   collaborations by multiple remote users.

3. There is a common `git` expression: 'ABC'.  What does it mean, and why is it 
   good advice?  
   'ABC' means Always Be Committing.  It's good advice because frequent commits
   ensure that changes to the codebase are documented (and saved) in incremental
   steps.

4. What is Unix?  How has the Unix philosophy influenced software development?  
   Unix is a multi-tasking, multi-user computer operating system (OS).  Unix 
   systems are characterized by a modular design, which dictates that the OS
   provide a set of simple tools that perform specific functions.  This
   philosophical approach to making software has been called the Unix
   philosophy.

5. You try to run an application, but are told that you don't have permission to
   access a certain file.  Describe the steps you would use to solve 
   this problem (allowing access to the file).  
   Assuming you are on Unix/Linux, you could first try to run the command as a
   superuser by prefacing your terminal command with `sudo`.  Next, check the
   file permissions.  The mode of the file may need to be changed using `chmod`.

5. Compare and contrast functional and object oriented programming paradigms.  
    Then discuss the the 3 pillars of OOP and how they relate to Python.  
    
    *from http://www.codenewbie.org/blogs/object-oriented-programming-vs-functional-programming*  
    Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which are data structures that contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods -- Wikipedia https://en.wikipedia.org/wiki/Object-oriented_programming

    Functional programming is a programming paradigm, a style of building the structure and elements of computer programs, that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data -- Wikipedia https://en.wikipedia.org/wiki/Functional_programming

    In all programs, there are two primary components: the data (the stuff a program knows) and the behaviors (the stuff a program can do to/with that data). OOP says that bringing together data and its associated behavior in a single location (called an “object”) makes it easier to understand how a program works. FP says that data and behavior are distinctively different things and should be kept separate for clarity.

    *from https://stackoverflow.com/questions/2078978/functional-programming-vs-object-oriented-programming*  
    An object-oriented approach is useful when you have a fixed set of operations on things, and as your code evolves, you primarily add new things. This can be accomplished by adding new classes which implement existing methods, and the existing classes are left alone.

    A functional approach is useful when you have a fixed set of things, and as your code evolves, you primarily add new operations on existing things. This can be accomplished by adding new functions which compute with existing data types, and the existing functions are left alone.

    The three pillars of OOP are **Encapsulation**, **Inheritance**, and **Polymorphism**.
    * Encapsulation: requires code to manipulate an object's state only through method calls.
        * Python does not enforce encapsulation! (We are all consenting adults.)
    * Inheritance: A subclass (child) inherits some data and methods from a superclass (parent or base), but then the subclass specializes the behavior.
    * Polymorphishm: The idea of treating objects the same way if they support the same interface (even if they are different classes!) Think addition and subtraction for floats and integers.   



6. What are some distinguishing characteristics of the Python programming 
   language?  
    * Python supports many different programming paradigms:   
        * imperative: focuses on describing how a program operates; uses statements to change a program's state
        * object-oriented: focuses on objects that contain data and methods to work on that data
        * procedural: based on the idea of a procedural call, it's a type of imperative programming that relies heavily on blocks and scope
        * functional: computation is based on the evaluation of mathematical functions, and avoids changing state and mutable data. It's a declarative programming paradigm.
    * It's interpreted, instead of compiled.
    * Design philosophy emphasizes code readability
    * Has a large development community, and open source development.  

7. What are some differences between Python 2 and Python 3?  Why was Python 3
   developed?
    * print function is different
    * many of the functions that returned a list in python 2 return an iterator in Python

    One of the guiding principles of Python 3 was to "reduce feature duplication by removing the old ways of doing things."

8. List major data structures in Python.  Which data structure(s) would you use to
   in each of the following situations, and why:

  * Unchanging sales records - tuple, because it's a lightweight data structure good for unchanging data

  * A customer database where changing information, such as address, email, and purchases are associated with a given customer name. - dictionary, with key as customer identifier(name), and a list as values, where the list elements can be changed

  * Driving waypoint locations between arbitrary points A and B. - an arbitrary length list of tuples associated with each waypoint

  * The unique words used in a text corpus. - set, unique values

  * A search engine that returns results quickly for a given search term. - dictionary with key as search term and value as the results

9. Write a one line list comprehension to perform the following matrix
   multiplication (A dot product B).  Describe how it works. How would you check
   it with NumPy?
```python
    import numpy as np

    def matrix_multiplication(A, B):
        return [[sum(A[i][j]*B[j][k] for j in range(len(A[0])))
            for k in range(len(B[0]))] for i in range(len(A))]

    if __name__ == '__main__':
        A = [ [ 2, 4], [ 1, 7], [-1, 8] ]

        B = [ [3, 2, -5, 6],  [1, -3, 4, 8] ]

        print("Matrix multiplication results:")
        mat = matrix_multiplication(A, B)
        for line in mat:
            print(line)

        print("\nNumpy results:")
        Anp = np.array(A)
        Bnp = np.array(B)
        print(np.dot(Anp,Bnp))
        #[[ 10  -8   6  44]
        # [ 10 -19  23  62]
        # [  5 -26  37  58]]
```

10. The `data` folder contains tweets from Elon Musk in March of 2017. Write a
    Python TweetData class to hold Elon's tweets.  The class should have at least two
    attributes: .raw and .cleanedtweets.  The .raw attribute should hold the raw data (3
    columns and 120 rows).  The .cleanedtweets attribute should only have 1 column
    (but still 120 rows) containing only lowercase alphanumeric characters present
    in the 3rd column of the raw tweets.  Feel free to use whatever additional 
    attributes or methods you need to make the class and an Elon Tweets object.

```python
    import argparse
    import pandas as pd

    class TweetData(object):
        '''Reads tweets saved in a csv with 3 columns: id, timestamp, and tweet text.
           Parses data in the tweet text into a cleaned form containing only alpha-
           numeric characters. @Addresses are maintained, but links are dropped.
        '''
        
        def __init__(self, filename):
            df = pd.read_csv(filename)
            self.raw = df.values
            self.raw_columns = list(df.columns)
            self.cleanedtweets = df['text'].apply(self._clean_tweet).values.reshape((-1,1))

        def _clean_word(self, raw_word):
            link_txt = 'https'
            encoding_txt = 'xa6'
            if (link_txt in raw_word or encoding_txt in raw_word):
                word_cleaned = ''
            elif raw_word[0] == '@':
                word_cleaned = raw_word
            else:
                word_cleaned = ''.join([c for c in raw_word if c.isalnum()])
            return word_cleaned

        def _clean_tweet(self, raw_text):
            text_str = raw_text[2:]
            words = text_str.split(' ')
            cleaned_tweet = ' '.join([self._clean_word(word) for word in words])
            return cleaned_tweet

    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Process Twitter Tweets')
        parser.add_argument('filename')
        args = parser.parse_args()
        tweets = TweetData(args.filename) 
```
