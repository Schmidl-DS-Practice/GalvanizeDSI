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
