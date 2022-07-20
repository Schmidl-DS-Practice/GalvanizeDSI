from pymongo import MongoClient
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np

client = MongoClient()
db = client.nyt_dump

coll = db.articles

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

documents = [' '.join(article['content']).lower() for article in coll.find()]
# print(documents)
token = []
for content in documents:
    token.append(nltk.word_tokenize(content))
# print(token[0])

stop_words = set(stopwords.words('english'))

a_token = []
for words in token:

    for word in words:
        a_token.append(word)
        if word not in stop_words:
            a_token.append(word)

porter = PorterStemmer()
snowball = SnowballStemmer('english')
wordnet = WordNetLemmatizer()

token_porter = [[porter.stem(word) for word in words] for words in a_token]
token_snowball = [[snowball.stem(word) for word in words] for words in a_token]
token_wordnet = [[wordnet.lemmatize(word) for word in words] for words in a_token]

# Compare
for i in range(min(len(token_porter[0]), len(token_snowball[0]), len(token_wordnet[0]))):
    p, s, w = token_porter[0][i], token_snowball[0][i], token_wordnet[0][i]
    if len(set((p, s, w))) != 1:
        print("{}\t{}\t{}\t{}".format(a_token[0][i], p, s, w))

# Bag of words and TF-IDF

# 1. Create vocab, set of unique words
a_token = token_snowball # choose which stemmer/lemmatizer to use
vocab_set = set()
[[vocab_set.add(token) for token in tokens] for tokens in a_token]
vocab = list(vocab_set)

# 2. Create word count vectors manually.
matrix = [[0] * len(vocab) for doc in a_token]
vocab_dict = dict((word, i) for i, word in enumerate(vocab))
for i, words in enumerate(a_token):
    for word in words:
        matrix[i][vocab_dict[word]] += 1

# 3. Create word count vector over the whole corpus.
cv = CountVectorizer(stop_words='english')
vectorized = cv.fit_transform(documents)

tfidf = TfidfVectorizer(stop_words='english')
tfidfed = tfidf.fit_transform(documents)


# Cosine Similarity using TF-IDF

# 1. Compute cosine similarity
cosine_similarities = linear_kernel(tfidfed, tfidfed)

# 2. Print out similarities
for i, doc1 in enumerate(a_token):
    for j, doc2 in enumerate(a_token):
        print(i, j, cosine_similarities[i, j])

