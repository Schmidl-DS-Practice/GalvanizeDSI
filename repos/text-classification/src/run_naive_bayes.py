from pymongo import MongoClient
from nltk.tokenize import word_tokenize, wordpunct_tokenize, RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.stem.snowball import SnowballStemmer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB as SKMultinomialNB
from naive_bayes import MultinomialNaiveBayes
import numpy as np

def load_data():
    client = MongoClient()
    db = client.nyt_dump
    coll = db.articles

    articles = coll.find({'$or': [{'section_name':'Sports'},
                                  {'section_name': 'Fashion & Style'}]})

    article_texts = []
    labels = []
    for article in articles:
        article_texts.append(' '.join(article['content'])), 
        labels.append(article['section_name'])
    return article_texts, np.array(labels)
 
def my_tokenizer(doc):
    tokenizer = RegexpTokenizer(r'\w+')
    article_tokens = tokenizer.tokenize(doc.lower())
    return article_tokens


if __name__ == '__main__':
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    model = MultinomialNaiveBayes()
    model.fit(X_train, X_test)
    y_pred = model.predict(X_test)
    


    X_tr_toks = [my_tokenizer(doc) for doc in X_train]
    X_te_toks = [my_tokenizer(doc) for doc in X_test]


