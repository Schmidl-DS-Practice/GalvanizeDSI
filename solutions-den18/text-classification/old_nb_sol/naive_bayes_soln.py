from __future__ import division
from collections import Counter, defaultdict
import numpy as np
import itertools

class NaiveBayes(object):
    def __init__(self, alpha=1.):
        """
        INPUT:
        -alpha: float, laplace smoothing constant.

        ATTRIBUTES:
        - class_counts: the number of samples per class; keys=labels
        - class_feature_counts: the number of samples per feature per label;
                               keys=labels, values=Counter with key=feature
        - class_freq: the frequency of each class in the data
        - p: the number of features
        """
        self.class_counts = defaultdict(int)
        self.class_feature_counts = defaultdict(Counter)
        self.class_freq = None
        self.alpha = float(alpha)
        self.p = None

    def _compute_likelihoods(self, X, y):
        '''
        INPUT:
        - X: List of list of tokens.
        - y: numpy array, labels

        OUTPUT: None

        Compute the word count for each class and the frequency of each feature
        per class.  (Compute class_counts and class_feature_counts).
        '''

        for row, label in zip(X, y):
            self.class_counts[label] += len(row)
            word_counts = Counter(row)
            self.class_feature_counts[label].update(word_counts)

    def fit(self, X, y):
        '''
        INPUT:
        - X: List of list of tokens.
        - y: numpy array, labels

        OUTPUT: None
        '''
        #Compute class frequency P(y)
        self.class_freq = Counter(y)

        #Compute number of features.
        self.p = len(set(itertools.chain(*X)))

        #Compute likelihoods
        self._compute_likelihoods(X, y)

    def posteriors(self, X):
        '''
        INPUT:
        - X: List of list of tokens.

        OUTPUT:
        List of dictionaries with key=label, value=log(P(y)) + sum(log(P(x_i|y))).
        '''

        results = []
        # For every data point in X
        for row in X:
            # Calculate the number of times each feature appears
            row_counts = Counter(row)
            prob_dict = dict()
            # For each class in the training set
            for label, freq in self.class_freq.items():

                # Compute P(x_i | y)
                denominator = self.class_counts[label] + self.alpha * self.p
                log_p = 0
                for key in row_counts:
                    p_x_y = self.class_feature_counts[label][key] + self.alpha
                    p_x_y /= denominator
                    log_p += np.log(p_x_y)
                
                # log(P(y)) + sum(log(P(x_i|y))
                prob_dict[label] = np.log(freq / sum(self.class_freq.values())) + log_p

            results.append(prob_dict)
        return results

    def predict(self, X):
        """
        INPUT:
        - X: A list of lists of tokens.

        OUTPUT:
        - predictions: a numpy array with predicted labels.

        """
        # Choose the key with the largest value
        predictions = []
        for post in self.posteriors(X):
            pred = max(post.keys(), key=(lambda label: post[label]))
            predictions.append(pred)
        return np.array(predictions)

    def score(self, X, y):
        '''
        INPUT:
        - X: List of list of tokens.
        - y: numpy array, labels

        OUTPUT:
        - accuracy: float between 0 and 1

        Calculate the accuracy, the percent predicted correctly.
        '''

        return np.mean(self.predict(X) == y)
