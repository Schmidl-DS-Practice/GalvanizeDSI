import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pipeline as pipe

def clustered(df,n_clusters=5):
    corpus = df['text']
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(corpus)
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
    feature_names = vectorizer.get_feature_names()
    df['Kmean_label'] = kmeans.labels_
    return df,feature_names,kmeans

def get_pipe_clustered(n_clusters=5):
    df = pipe.get_df()
    df,_ = clustered(df)
    return df


if __name__ == '__main__':
    df = pipe.get_df('data/ufodata.json', max_iters = 20000)
    df, feature_names,km = clustered(df,n_clusters=5)
    # print(feature_names)

    print(df.info())
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = feature_names
    for i in range(5):
        print("Cluster %d:" % i, end='')
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind], end='')
            print()