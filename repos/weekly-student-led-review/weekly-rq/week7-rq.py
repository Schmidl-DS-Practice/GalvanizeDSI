##Week 7 Review Questions
#1 In processing text to perform analyses, what steps are usually involved?
# When might you use, or not, some of these steps?
'''Lower case text
When capitalization matters (ie sport teams, verbs vs pronouns)
Strip punctuation
When it matters 
Remove stop words
Review stop word list make edits as necessary 
Stem or lementize
Stem to get rid of endings with -ing, -ed
Lementiize to dictionary root form
Convert to a bag of words
When order doesn’t matter'''


#2 The Naive Bayes classification algorithm is often used for text classification.
# Why is that? Explain how Bayes rule is used to implement to algorithm. 
# How is a classification made? Why is this method called "Naive" Bayes?
'''Computationally efficient
Naive assumes all data is independent
Can calculate priors and maximum likelihood and returns postier
All features are assumed independent(naive)'''

#3  What is the difference between supervised and unsupervised learning?
'''SL - has targets(y) that match to X
USL - only requires X, but is not mapped to targets(y). It clusters the X.'''


#4 Provide 3 types of questions you would answer with
'''a) supervised learning:
Supervised learning allows you to collect data or produce a data output from the previous experience.
Helps you to optimize performance criteria using experience. Helps you to solve various types of real-world computation problems.


b) unsupervised learning:
    finds all kind of unknown patterns in data.
    help you to find features which can be useful for categorization.
    It takes place in real time, so all the input data to be analyzed and labeled in the presence of learners.
    It is easier to get unlabeled data from a computer than labeled data, which needs manual intervention.'''

#5 Whiteboard the algorithm (pseudocode) for the KMeans algorithm.
    '''Initialize_centroids
    While not converged:
        Assign_data_to_centroids
        compute_new_centroid_means'''

#6 Why is using Within-Cluster-Sum-of-Squares (WCSS) not a good metric to determine how many clusters you should pick in Kmeans clustering?
# Name other methods/metrics you could use to pick the number of clusters.
'''Not easy or very precise
Silhouette Score, see lecture slides for other methods, domain knowledge'''


#7a) What are principal components?
    '''Directions in feature space along which the data are highly variable'''

  # b) What are some benefits of Principal Component Analysis?
    '''Dimensionality reduction 
        Remove collinearity of features'''

  # c) How are principal components calculated?
        '''Eigen-decompoisition of the X covariance or correlation matrix
        Singular value decomposition'''

#8 Compare and contrast Singular Value Decomposition (SVD) and Non-Negative Matrix Factorization (NMF).
# Which method makes more interpretable topics, and why? 
'''Singular Value Decomposition (SVD) is an alternative way of performing PCA. Instead of finding the eigendecomposition of the covariance matrix, we will decompose the original matrix of data, X. As we will find out at the end of this lecture, SVD is directly related to eigen-decomposition. 
NMF is a matrix factorization technique where a large matrix V is factored into two smaller matrices W and H, where all matrices are constrained to contain only zero or positive values making it more interpretable.'''


#9 What is the difference between hard and soft clustering?
# What algorithms did you learn this week that perform hard clustering?
# How about soft clustering?
'''Hard clustering: Each observation (row of data) can belong to only one cluster, e.g. article is sports, or politics, or finance
Algorithm: Kmeans

Soft: Each observation(row of data) can belong to multiple clusters
Algorithm: SVD, NMF'''
