import numpy as np
import random
from sklearn import datasets
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from sklearn.metrics import silhouette_score

class KMeans(object):
    '''
    K-Means clustering
    ----------
    n_clusters : int, optional, default: 8
        The number of clusters to form as well as the number of
        centroids to generate.
    init : {'random', 'random_initialization', 'k-means++'}
        Method for initialization, defaults to 'k-means++':
        'k-means++' : selects initial cluster centers for k-mean
        clustering in a smart way to speed up convergence. See section
        Notes in k_init for more details.
        'random': choose k observations (rows) at random from data for
        the initial centroids.
        If an ndarray is passed, it should be of shape (n_clusters, n_features)
        and gives the initial centers.
    n_init : int, default: 1
        Number of time the k-means algorithm will be run with different
        centroid seeds. The final results will be the best output of
        n_init consecutive runs in terms of inertia.
    max_iter : int, default: 1000
        Maximum number of iterations of the k-means algorithm for a
        single run.
    tolerance : int, default : .00001
    Attributes
    ----------
    cluster_centers_ : array, [n_clusters, n_features]
        Coordinates of cluster centers
    labels_ :
        Labels of each point
    '''

    def __init__(self, n_clusters=8, init='random', n_init=1,
                 max_iter=300, tolerance = 1e-4, verbose = False):

        self.n_clusters = n_clusters
        self.init = init
        self.max_iter = max_iter
        self.tolerance = tolerance
        self.n_init = n_init
        self.verbose = verbose
        self.centroids_ = None
        self.labels_ = None

    def _initialize_centroids(self, X):
        '''
        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
            Data points to take random selection from for initial centroids
        You should code the simplest case of random selection of k centroids from data
        OPTIONAL: code up random_initialization and/or k-means++ initialization here also
        '''
        if self.init == 'random':
            # random choice centroid initialization
            randinds = np.random.choice(np.arange(X.shape[0]), self.n_clusters)
            self.centroids_ =  X[randinds]
        elif self.init == 'random_initialization':
            labels = np.random.choice(self.n_clusters, size = X.shape[0])
            self.centroids_ = np.array([X[labels == label].mean(axis = 0) for label in range(k)])
        else:
            # use Kmeans plus plus
            self.centroids_ = self._kmeans_plus_plus(X)

    def _kmeans_plus_plus(self, X):
        '''
        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
        helper function to initialize centroids in a smart way
        '''
        centroids = np.zeros((self.n_clusters, X.shape[1]))
        for j in range(self.n_clusters):
            if j == 0:
                centroids[j] = X[np.random.choice(X.shape[0])]
            else:
                # compute square of euclidean distance to nearest centroid
                dists = cdist(X, centroids[:j].reshape(-1, X.shape[1]))
                dists2 = dists.min(axis = 1)
                # pick random choice with probabilty propertional to distances
                ind = np.random.choice(X.shape[0], p = dists2/dists2.sum())
                centroids[j] = X[ind]
        return centroids

    def _assign_clusters(self, X):
        '''
        computes euclidean distance from each point to each centroid and
        assigns point to closest centroid)
        assigns self.labels_
        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
            Data points to assign to clusters based on distance metric
        '''
        labels = self.predict(X)
        self.labels_ = labels

    def _compute_centroids(self, X):
        '''
        compute the centroids for the datapoints in X from the current values
        of self.labels_
        assigns self.centroids_
        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
            Data points to assign to clusters based on distance metric
        '''
        centroids = [X[self.labels_==j].mean(axis=0) for j in range(self.n_clusters)]
        return np.array(centroids)

    def fit(self, X):
        ''''
        Compute k-means clustering.
        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
            Training instances to cluster.
        '''
        best_score, best_centroids = np.inf, self._kmeans_plus_plus(X)
        for i in range(self.n_init):
            # initialize new centroids
            self._initialize_centroids(X)

            # fit this initialization
            for j in range(self.max_iter):
                self._assign_clusters(X)
                new_centroids = self._compute_centroids(X)

                # check convergence
                if (np.linalg.norm(self.centroids_ - new_centroids, axis = 1) < self.tolerance).all():
                    if self.verbose:
                        print('Initialization {} converged on interation {}'.format(i, j))
                    break

            # re-assign centroids
            self.centroids_ = new_centroids

            # check score
            new_score = self.score(X)
            if new_score < best_score:
                best_score = new_score
                best_centroids = self.centroids_

        # assign centroids and labels to be best centroids
        self.centroids_ = best_centroids
        self._assign_clusters(X)
        return

    def predict(self, X):
        '''
        Optional method: predict the closest cluster each sample in X belongs to.
        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            New data to predict.
        Returns
        -------
        labels : array, shape [n_samples,]
            Index of the cluster each sample belongs to.
        '''
        distances = cdist(X, self.centroids_)
        return distances.argmin(axis = 1)

    def score(self, X):
        '''
        return the total residual sum of squares
        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            New data.
        Returns
        -------
        score : float
            The SSE
        '''
        labels = self.predict(X)
        SSE = ((X - self.centroids_[labels])**2).sum()
        return SSE


def load_data():
    '''
    loads iris data set and returns iris data set as a np array
    '''
    iris = datasets.load_iris()
    return iris['data']


def elbow_plot(data, plotname):
    plt.clf()
    ks = np.arange(2, 11)
    sses = []
    for k in ks:
        model = KMeans(n_clusters = k, verbose = True)
        model.fit(data)
        sses.append(model.score(data))
    plt.plot(ks, sses)
    plt.xlabel('Number of clusters')
    plt.ylabel('SSE')
    plt.title('Elbow Plot')
    plt.savefig(plotname)


def silhouette(data, k):
    model = KMeans(n_clusters = k, init='k-means++', verbose = True)
    model.fit(data)
    labels = model.labels_
    return silhouette_score(data, labels, metric='euclidean')

if __name__ == '__main__':
    iris = load_data()

    elbow_plot(iris, 'elbow_plot.png')
    for k in range(2, 11):
        print(silhouette(iris, k))
