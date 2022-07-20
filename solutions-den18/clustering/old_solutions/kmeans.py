import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import Counter
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

## K-MEANS
print("\nPart 1 - Kmeans")
# 1. Apply k-means clustering to the articles.pkl
os.chdir('../data')
articles_df = pd.read_pickle("articles.pkl")
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(articles_df['content'])
features = vectorizer.get_feature_names()
kmeans = KMeans()
kmeans.fit(X)

# 2. Print out the centroids.
print("\n2) cluster centers:")
print(kmeans.cluster_centers_)

# 3. Find the top 10 features for each cluster.
top_centroids = kmeans.cluster_centers_.argsort()[:,-1:-11:-1]
print("\n3) top features (words) for each cluster:")
for num, centroid in enumerate(top_centroids):
    print("%d: %s" % (num, ", ".join(features[i] for i in centroid)))

# OUTPUT:
# 0: said, mr, government, state, official, court, people, attack, police, united
# 1: yard, touchdown, game, quarterback, giant, team, season, smith, manning, jet
# 2: yankee, rivera, game, inning, pettitte, season, run, hit, ray, said
# 3: mr, art, ms, music, new, work, like, said, opera, dance
# 4: team, game, season, said, cup, player, league, year, race, coach
# 5: percent, said, company, bank, year, new, market, rate, million, government
# 6: iran, rouhani, iranian, nuclear, mr, obama, israel, united, netanyahu, president
# 7: republican, health, house, government, care, shutdown, obama, law, senate, mr


# 4. Limit the number of features and see if the words of the topics change.
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(articles_df['content'])
features = vectorizer.get_feature_names()
kmeans = KMeans()
kmeans.fit(X)
top_centroids = kmeans.cluster_centers_.argsort()[:,-1:-11:-1]
print("\n4) top features for each cluster with 1000 max features:")
for num, centroid in enumerate(top_centroids):
    print("%d: %s" % (num, ", ".join(features[i] for i in centroid)))

# OUTPUT:
# 0: mr, court, judge, said, case, state, law, justice, prison, lawyer
# 1: company, said, percent, year, new, market, government, bank, state, million
# 2: mr, ms, art, music, new, work, said, like, city, film
# 3: cup, sept, race, year, said, team, editor, new, world, 2013
# 4: said, attack, mr, official, people, government, united, syria, killed, military
# 5: iran, nuclear, mr, obama, united, president, nation, said, state, speech
# 6: game, season, team, said, player, league, yard, play, coach, run
# 7: republican, party, mr, government, house, senate, health, democrat, care, obama

# 5. Print out the titles of a random sample of the articles assigned to each
# cluster to get a sense of the topic.
print("\n5) random sample of titles in each cluster")
assigned_cluster = kmeans.transform(X).argmin(axis=1)
for i in range(kmeans.n_clusters):
    cluster = np.arange(0, X.shape[0])[assigned_cluster==i]
    sample_articles = np.random.choice(cluster, 3, replace=False)
    print("cluster %d:" % i)
    for article in sample_articles:
        print("    %s" % articles_df.ix[article]['headline'])

# cluster 0:
#     Britain Plans to Require Community Service for Long-Term Unemployment Benefits
#     Japan's Leader Gives No Ground in Islands Dispute
#     Greek Civil Servants Start 2-Day Strike
# cluster 1:
#     College Football Around the Country
#     First-Round Picks Pay Off in Jets' Pass Rush
#     Nova Throws for 3 Touchdowns as Rutgers Rallies Past Arkansas
# cluster 2:
#     Scherzer Wins 21st as Tigers Clinch
#     Now Making Money for the Yankees ...
#     Yankees' Fond, and Not So Fond, Farewells
# cluster 3:
#     The Chick-Magnet Dreams of a Hollywood Guy
#     A Fight for Love, in the Met and Out
#     The Dawn of a World, Dreamlike Yet Chaotic
# cluster 4:
#     At McLaren, Celebrating a Half-Century of Excellence
#     Meteoric Rise Lands Jordan Spieth on U.S. Presidents Cup Team
#     In the Market for Another Liriano
# cluster 5:
#     Evidence North Korea Restarted Reactor
#     Possibility of Delay Threatens European Bank Overhaul and the Region&#8217;s Economy
#     Atomic Goal: 800 Years of Power From Waste
# cluster 6:
#     Give Iran a Chance
#     Short of a Deal, Containing Iran Is the Best Option
#     Iran's President Responds to Netanyahu
# cluster 7:
#     Deeply Conservative, but Not an Obama-Hater
#     Home Care in the Home Stretch
#     Our Democracy Is at Stake


# 6. Which topics has k-means discovered?
# A couple obvious ones from above:
# Cluster 2 is sports.
# Cluster 7 is conservative news.
print("\n6) answers will vary.")

# 7. If you set k == to the number of NYT sections in the dataset, does it
# return topics that map to a section?
kmeans = KMeans(n_clusters=10)
kmeans.fit(X)
assigned_cluster = kmeans.transform(X).argmin(axis=1)
print("\n7) top 2 topics for each cluster")
for i in range(kmeans.n_clusters):
    cluster = np.arange(0, X.shape[0])[assigned_cluster==i]
    topics = articles_df.ix[cluster].dropna()['section_name']
    most_common = Counter(topics).most_common()
    print("Cluster %d: %s" % (i, most_common[0][0]))
    if len(most_common) > 1:
        print(" %s" % (most_common[1][0]))

#print
# OUTPUT
# Cluster 0: U.S.  Opinion
# Cluster 1: Sports  Opinion
# Cluster 2: Sports  Arts
# Cluster 3: World  Opinion
# Cluster 4: Arts  Sports
# Cluster 5: World  Opinion
# Cluster 6: Sports
# Cluster 7: World  U.S.
# Cluster 8: Opinion  Business Day
# Cluster 9: Business Day  Opinion

# It sort of classifies by section, but some (like sports and world) end up in
# multiple clusters.


# 8. Try clustering with a subset of the sections.
mask = np.logical_or(
       np.logical_or((articles_df['section_name']=='Sports').values,
                     (articles_df['section_name']=='Arts').values),
                     (articles_df['section_name']=='Business Day').values)
three_articles_df = articles_df[mask]
kmeans = KMeans(n_clusters=3)
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(three_articles_df['content'])
kmeans.fit(X)
assigned_cluster = kmeans.transform(X).argmin(axis=1)
print("8) Top 2 topics for each cluster")
for i in range(kmeans.n_clusters):
    cluster = np.arange(0, X.shape[0])[assigned_cluster==i]
    topics = three_articles_df.ix[cluster].dropna()['section_name']
    most_common = Counter(topics).most_common()
    print("Cluster %d: %s" % (i, most_common[0][0]))
    if len(most_common) > 1:
        print(" %s" % (most_common[1][0]))

#print
# top 2 topics for each cluster
# Cluster 0: Sports  Arts
# Cluster 1: Sports  Arts
# Cluster 2: Sports  Arts

# It doesn't really do better here.

