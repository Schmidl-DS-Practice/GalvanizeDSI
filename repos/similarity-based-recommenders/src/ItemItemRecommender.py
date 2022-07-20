from time import time
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse

class ItemItemRecommender(object):
    """Item-item similarity recommender."""

    def __init__(self, neighborhood_size):
        """Initialize the parameters of the model."""
        self.neighborhood_size = neighborhood_size

    def fit(self, ratings_mat):
        """Fit the model to the data specified as an argument.
        Store objects for describing model fit as class attributes.
        """
        self.ratings_mat = ratings_mat
        self.n_users = ratings_mat.shape[0]
        self.n_items = ratings_mat.shape[1]
        self.item_sim_mat = cosine_similarity(self.ratings_mat.T)
        self._set_neighborhoods()

    def make_cos_sim_and_neighborhoods(self, ratings_mat, neighborhood_size):
        '''
        Args:
            ratings_mat (sparse matrix): 2-dimensional matrix of ratings
            neighborhood_size (int): number of similar items to look at
        Returns:
            items_cos_sim (numpy array): an item-item matrix where each element
            is the cosine_similarity of the items at the corresponding row and
            column. This is a square matrix where the length of each dimension
            equals the number of columns in ratings_mat.

            neighborhood (numpy array): a 2-dimensional matrix where each row is
            the neighborhood for that item. The elements are the indices of the
            n (neighborhood_size) most similar items. Most similar items are at
            the end of the row.
        '''
        items_cos_sim = cosine_similarity(ratings_mat.T)
        least_to_most_sim_indexes = np.argsort(items_cos_sim, 1)
        neighborhood = least_to_most_sim_indexes[:, -neighborhood_size:]
        return items_cos_sim, neighborhood

    def _set_neighborhoods(self):
        """Get the items most similar to each other item.
        Should set a class attribute with a matrix with number of rows
        equal to number of items, and number of columns equal to
        neighborhood size. Entries in this matrix will be indices of other
        items.
        You will call this in your fit method.
        """
        least_to_most_sim_indexes = np.argsort(self.item_sim_mat, 1)
        self.neighborhoods = least_to_most_sim_indexes[:, -self.neighborhood_size:]

    def pred_one_user(self, user_id, report_run_time=False):
        """Accept user id as arg. Return the predictions for a single user.
        Optional argument to specify whether or not timing should be
        provided on this operation.
        """
        start_time = time()
        items_rated_by_this_user = self.ratings_mat[user_id].nonzero()[1]
        # Just initializing so we have somewhere to put rating preds
        out = np.zeros(self.n_items)
        for item_to_rate in range(self.n_items):
            relevant_items = np.intersect1d(self.neighborhoods[item_to_rate],
                                            items_rated_by_this_user,
                                            assume_unique=True)  # assume_unique speeds up intersection op
        # note: self.ratings_mat has data type `sparse_lil_matrix`, while
        # self.items_sim_mat is a numpy array. Luckily for us, multiplication
        # between these two classes is defined, and even more luckily,
        # it is defined to as the dot product. So the numerator
        # in the following expression is an array of a single float
        # (not an array of elementwise products as you would expect
        #  if both things were numpy arrays)
            out[item_to_rate] = self.ratings_mat[user_id, relevant_items] * \
                self.item_sim_mat[item_to_rate, relevant_items] / \
                self.item_sim_mat[item_to_rate, relevant_items].sum()
        if report_run_time:
            print("Execution time: %f seconds" % (time()-start_time))
        cleaned_out = np.nan_to_num(out)
        return cleaned_out

    def pred_all_users(self, report_run_time=False):
        """Return a matrix of predictions for all users.
        Repeated calls of pred_one_user, are combined into a single matrix.
        Return value is matrix of users (rows) items (columns) and
        predicted ratings (values).
        Optional argument to specify whether or not timing should be
        provided on this operation.
        """
        start_time = time()
        all_ratings = [
            self.pred_one_user(user_id) for user_id in range(self.n_users)]
        if report_run_time:
            print("Execution time: %f seconds" % (time()-start_time))
        return np.array(all_ratings)

    def top_n_recs(self, user_id, n=10):
        """Take user_id argument and number argument.
        Return that number of items with the highest predicted ratings,
        after removing items that user has already rated.
        """
        pred_ratings = self.pred_one_user(user_id)
        item_index_sorted_by_pred_rating = list(np.argsort(pred_ratings))
        items_rated_by_this_user = self.ratings_mat[user_id].nonzero()[1]
        unrated_items_by_pred_rating = [item for item in item_index_sorted_by_pred_rating
                                        if item not in items_rated_by_this_user]
        return unrated_items_by_pred_rating[-n:]

def get_ratings_data():
    ratings_contents = pd.read_table("data/u.data",
        names=["user", "movie", "rating", "timestamp"])
    return ratings_contents

def load_movies():
    columns = """movie id | movie title | release date | video release date | IMDb URL | unknown | Action | Adventure | Animation |
            Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western """
    columns = [word.strip() for word in columns.split('|')]
    columns = [word.replace(' ','_') for word in columns]
    movies = pd.read_table("./data/u.item", names= columns, sep='|', encoding='latin-1')
    movies = movies[['movie_id', 'movie_title']]
    return movies

if __name__ == '__main__':
    get_ratings_data()
    load_movies()

    

    # it_recommender = ItemItemRecommender(neighborhood_size)
