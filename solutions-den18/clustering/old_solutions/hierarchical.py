import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import Counter
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

## HIERARCHICAL CLUSTERING


os.chdir('../data')
articles_df = pd.read_pickle("articles.pkl")

# 1.  Create a subset of the original articles by filtering the data set to
# contain at least one article from each section and at most around 200 total
# articles.
small_mask = np.zeros(len(articles_df)).astype(bool)
indices = np.arange(len(articles_df))
for category in articles_df['section_name'].unique():
    category_mask = (articles_df['section_name']==category).values
    new_index = np.random.choice(indices[category_mask])
    small_mask[new_index] = True
additional_indices = np.random.choice(indices[np.logical_not(small_mask)],
                                      100 - sum(small_mask),
                                      replace=False)
small_mask[additional_indices] = True
small_df = articles_df.ix[small_mask]

# Verify that this is good:
assert len(small_df) == 100
assert len(small_df['section_name'].unique()) == \
    len(articles_df['section_name'].unique())


# 2-3. The first step to using scipy's Hierarchical clustering is to first find
# out how similar our vectors are to one another.

# first vectorize...
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
small_X = vectorizer.fit_transform(small_df['content'])
small_features = vectorizer.get_feature_names()

# now get distances
distxy = squareform(pdist(small_X.todense(), metric='cosine'))


# 4. Pass this matrix into scipy's linkage function to compute our
# hierarchical clusters.
link = linkage(distxy, method='complete')

# 5. Using scipy's dendrogram function plot the linkages as
# a hierachical tree.
dendro = dendrogram(link, color_threshold=1.5, leaf_font_size=9)
plt.show()


## HIERARCHICAL TOPICS
# 1. To make your clusters more interpretable, change the labels on the data
# to be the titles of the articles.
dendro = dendrogram(link, color_threshold=1.5, leaf_font_size=9,
                    labels=small_df['headline'].values)
# fix spacing to better view dendrogram and the labels
plt.subplots_adjust(top=.99, bottom=0.5, left=0.05, right=0.99)
plt.show()


# 2. Label each point with the title and the section.

labels = (small_df['headline'] + ' :: ' + small_df['section_name']).values
dendro = dendrogram(link, color_threshold=1.5, leaf_font_size=9,
                    labels=labels)
# fix spacing to better view dendrogram and the labels
plt.subplots_adjust(top=.99, bottom=0.5, left=0.05, right=0.99)
plt.show()


# 3. Explore different clusters on a per section basis.
for i, category in enumerate(['Arts', 'Sports', 'World']):
    cat_indices = articles_df[articles_df['section_name']==category].index
    indices = np.random.choice(cat_indices, 40)
    cat_df = articles_df.ix[indices]
    vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
    cat_X = vectorizer.fit_transform(cat_df['content'])
    distxy = squareform(pdist(cat_X.todense(), metric='cosine'))
    ax = plt.subplot(1, 3, i + 1)
    dendro = dendrogram(linkage(distxy, method='complete'),
                        color_threshold=4,
                        leaf_font_size=4,
                        labels=small_df['headline'].values)
    ax.set_title(category)
plt.subplots_adjust(top=.95, bottom=0.5, left=0.05, right=0.99)
plt.show()


# 7. Perform the same analysis as above and inspect the dendrogram with the
# words from the articles.
distxy_words = squareform(pdist(small_X.T.todense(), metric='cosine'))
dendro = dendrogram(linkage(distxy_words, method='complete'),
                    color_threshold=1.5, leaf_font_size=9,
                    labels=small_features)
plt.subplots_adjust(top=.99, bottom=0.2, left=0.05, right=0.99)

