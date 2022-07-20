import numpy as np
import argparse
import pandas as pd

#1
'''Git -> Free open-source, distrubted version control system.
        It allows for control, distrubtion, and collaboration of all
        versions of your projects, in the form of repos.'''

#2
'''Github is cloud-based and allows you to manage your repos. The spot
        to collaborate with colleagues on projects. Fork, clone, add,
        push, and pull each others repos to get the best outcome.'''

#3
'''Always be committing. This is the procedure for updating your repos.'''

#4
'''Unix->open-source, operating system developed in the 1970s at Bell
        Labs for software devolopers.
        Unix philosophy is building short, clear, simple code that can be easily maintained and
        repurposed by any developer. -write programs that do one thing
        well. -write programs that work together. -write programs to
        handle text'''

#5
'''Contact the owner of the app for approval. If this is a Git repo
        perform at pull request'''

#6
'''Functional programming-> define a function name and arguments.
        Inside the function give a procedure for the function
        to follow and return the end resolution.
    OOP-> define a class with attributes(data) and methods(procedures).
        The attributes are what information is wanted and the methods
        are what do we want from the attributes.
    Three pillars of OOP-> Classes; Attributes; Methods.'''

#7
'''Readability is the first and most important. Python was designed
    to be simple; to write/read as normal speech. It is also
    interpreted(line by line and not all at once),
    dynamicaly typed(type of value is decided at runtime),
    and large library(do not have to right own code for everything)
    to name a few more. '''

#8
'''New libraries, unicode, returns decimals, print(), range()'''

#9
'''List, tuple, dictionary, set
    -tuple
    -dictionary
    -tuple
    -set
    -dictionary'''

#10
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

#11 figure out how to run below code
class TweetData(object):
    '''Reads tweets saved in a csv with 3 columns: id, timestamp, and tweet text.
        Parses data in the tweet text into a cleaned form containing only alpha-
        numeric characters. @Addresses are maintained, but links are dropped.'''
                
    def __init__(self, filename):
        df = pd.read_csv('elonmusk_tweets_201703.csv')
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
    parser.add_argument('elonmusk_tweets_201703.csv')
    args = parser.parse_args()
    tweets = TweetData(args.filename)