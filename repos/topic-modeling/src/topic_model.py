import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import numpy as np


def load_data_return_content(filePath):
    df = pd.read_pickle(filePath)
    Vec = TfidfVectorizer(max_features=5000, stop_words='english')
    content = Vec.fit_transform(df['content'])
    features = Vec.get_feature_names()
    return features, content, df

class NMF(object):
    def __init__(self, k, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
        self.W = None
        self.H = None
        
    def fit(self, V, threshold):
        V = V.toarray()
        self.W =  np.random.rand(V.shape[0], self.k)
        self.H = np.random.rand(self.k, V.shape[1])
        i = 0
        while (i<self.max_iterations): # or less than convergance criteria 
            self.H = np.linalg.lstsq(self.W, V, rcond=None)[0]
            self.H = np.clip(self.H, 0, 5)
            self.W = np.linalg.lstsq(self.H.T, V.T, rcond=None)[0]
            self.W = self.W.T
            self.W = np.clip(self.W, 0, 5)
            i+=1
            self.cost = np.linalg.norm(V - np.dot(self.W, self.H))
            print(self.cost)
            if np.abs(self.cost) < threshold:
                return self.W, self.H
        return self.W, self.H


if __name__ == '__main__':
    filePath = 'data/articles.pkl'
    features, content, df = load_data_return_content(filePath)
    nmf = NMF(k=4)
    W, H = nmf.fit(content, 10)
    print(W, H)
