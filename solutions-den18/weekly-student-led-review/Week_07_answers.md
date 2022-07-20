### Week 7 Review Questions

1. In processing text to perform analyses, what steps are usually involved? When 
   might you use, or not, some of these steps?

  * Lowercase your text
  * Strip out miscellaneous spacing & punctuation  
  * Remove stop words
  * Stem or lemmatize the text
  * Use part-of-speech tagging  
  * Use a bag-of-words approach to make a **tf** (term-frequency) or **tfidf** (term-frequency, inverse document frequency) feature matrix 
  * Expand feature matrix with N-grams

  For each step above, you need to consider for your use case if it makes  sense.  For example, Lowercasing your text may not make sense if in your  corpus STOP has a different meaning than stop.  

2. The Naive Bayes classification algorithm is often used for text classification.
   Why is that?  Explain how Bayes rule is used to implement to algorithm.  How
   is a classification made?  Why is this method called "Naive" Bayes?

   The Naive Bayes approach is computationally efficient for "wide" data -
   data that have many features.  It works by calculating, for each row of data,
   the log likelihood that the row belongs to each class.  The log-likelihood is
   based on Bayes rule, where the priors are based on the fractions of the total corpus
   comprised of each class, and the likelihood for each token in the row of data is
   determined by the number of times it appears in each class divided by the total number
   of words in that class.  

   The total likelihood associated with each class is the product of the prior and the
   likelihoods of each token.  The reason it's called "naive" is that this process
   assumes that each of the tokens is independent, but we know that word frequencies
   in a document are correlated with other words.
   <br>
3. What is the difference between supervised and unsupervised learning?   
   <br>
   The main difference between the two types is that supervised learning is done
   using a ground truth, or in other words, we have prior knowledge of what the
   output values for our samples should be. Therefore, the goal of supervised 
   learning is to learn a function that, given a sample of data and desired 
   outputs, best approximates the relationship between input and output 
   observable in the data. Unsupervised learning, on the other hand, does not 
   have labeled outputs, so its goal is to infer the natural structure present 
   within a set of data points.
   <br>
4. Provide 3 types of questions you would answer with   
   a) supervised learning:   
    * Predicting house sale price given house attributes  
    * Determining from past behavior if someone will continue to use a service or not.
    * From photos associated with names, for a given photo determine who the person is. 
  <br>
   b) unsupervised learning:    
    * Deterimining if there are clusters of homes with defining characteristics.  
    * Looking for groupings of users and user behavior.  
    * From many photos, determine which photos are of the same people.
  <br>
5. Whiteboard the algorithm (psuedocode) for the KMeans algorithm.  
     * initialize k centriod locations
      - you may do this by randomly assigning each point to a cluster and  
        then find the centroid of each cluster or use kmeans++ to pick  
        starting cluster points far away from each other
   * then repeat until "convergence":  
     * assign each data point to the nearest centroid  
     * compute new centroids  
    
    Where "convergence" is ideally where the points stop changing their cluster,  
    though there may always be a few that oscillate back and forth as the  
    centroid locations changes slightly.
 <br>
6. Why is using Within-Cluster-Sum-of-Squares (WCSS) not a good metric to detemine 
   how many clusters you should pick in Kmeans clustering?  Name other
   methods/metrics you could use to pick the number of clusters.   
  <br> 
   As k is increased, WCSS will continue to decrease so it isn't helpful in
   determining the right value of k.  

   However, using the Elbow plot method, you could plot the WCSS associated 
   with increasing values of k and see if at some value of k there was a
   marked "elbow" where increasing values of k don't decrease the WCSS much 
   (so that increasing k is showing diminishing returns). The value of k at
   which the elbow occurs is an arguable value for k.
   
   Plotting the average silhouette score for the points in the clusters is 
   another way to pick the value of k.  A large average silhouette score means
   that there is large intercluster differences (large distances between points 
   in different clusters) and small intracluster differences (small distances
   between points in the same cluster).
  <br>
7. a) What are principal components?     
   <br>
   Principal components are normalized linear combinations of the features
   of a dataset oriented in decreasing orthogonal directions of variance. 
   They form a typically lower-dimensional, orthogonal basis for understanding
   the data.  
   <br>
   b) What are some benefits of Principal Component Analysis?    
   <br>
   PCA reduces dimensionality and eliminates correlated features.  
   <br>
   c) How are principal components calculated?  
   <br>
   Principal components can be calculated using eigen-decomposition or with SVD.
   In the case of eigen-decomposition, the principal components are eigenvectors
   of the covariance/correlation matrix.  In the case of SVD, the matrix 
   factorization M = USV results in three matrices, where the product of the
   first two (U and S) form the principal components.
   <br>
8. Compare and contrast Singular Value Decomposition (SVD) and Non-Negative
   Matrix Factorization (NMF). Which method makes more interpretable topics,
   and why?
   <br>
   Both NMF and SVD are matrix factorization techniques.  The benefit of 
   SVD is that othogonal directions of variance (principal components)
   can be determined and quantified, while NMF also provides bases for
   the describing the data in a lower dimensional space but the vectors
   are not guaranteed to be orthogonal (or necessarily unique from 
   implementation to implementation). The benefit of NMF is that all
   the quantities that comprise the vectors are positive, so relative
   magnitudes of the components can be used to interpret how much users
   load on to topics, and how topics load on to items.
  <br>
9. What is the difference between hard and soft clustering?  What algorithms
   did you learn this week that perform hard clustering?  How about soft
   clustering?
   <br>
   Hard Clustering: In hard clustering, each data point either belongs to a cluster
   completely or not.  KMeans is a hard clustering algorithm.  
   <br>
   Soft Clustering: In soft clustering, instead of putting each data point into
   a separate cluster, a probability or likelihood of that data point to be in
   each cluster is assigned. Matrix factorization algorithms (PCA, SVD, NMF) 
   are soft clustering algorithms because entities are made of linear combinations
   of the axes defined by the factorization.  Gaussian Mixture Models (GMMs) are
   soft clustering algorithms too, because each point is assigned a probability
   to each gaussian.

