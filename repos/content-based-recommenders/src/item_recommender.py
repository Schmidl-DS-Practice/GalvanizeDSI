from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import re

class ItemRecommender():
    '''
    Content based item recommender
    '''
    def __init__(self, similarity_measure=None):
        self.similarity_matrix = None
        self.item_names = None

        if similarity_measure == None:
            self.similarity_measure = cosine_similarity
        else:
            self.similarity_measure = similarity_measure

    def fit(self, X, titles=None):
        '''
        Takes a numpy array of the item attributes and creates the
        similarity matrix

        INPUT -
            X: NUMPY ARRAY - Rows are items, columns are feature values
            titles: LIST - List of the item names/titles in order of the
                            numpy arrray

        OUTPUT - None


        Notes:  You might want to keep titles and X as attributes
        to refer to them later

        Create the a similarity matrix of item to item similarity
        '''
        # While keeping this as a sparse matrix would be best the cosign sim
        # function returns a array so there is no reason.
        
        if isinstance(X, pd.DataFrame):
            self.item_counts = X
            self.item_names = X.index
            self.similarity_df = pd.DataFrame(self.similarity_measure(X.values, X.values),
                 index = self.item_names)
        else:
            self.item_counts = X
            self.similarity_df = pd.DataFrame(self.similarity_measure(X, X),
                 index = titles)
            self.item_names = self.similarity_df.index

    def get_recommendations(self, item, n=5):
        '''
        Returns the top n items related to the item passed in
        INPUT:
            item    - STRING - Name of item in the original DataFrame
            n       - INT    - Number of top related items to return
        OUTPUT:
            items - List of the top n related item names

        For a given item find the n most similar items to it (this can
        be done using the similarity matrix created in the fit method)
        '''
        return self.item_names[self.similarity_df.loc[item].values.argsort()[-(n+1):-1]].values[::-1]

    def get_user_profile(self, items):
        '''
        Takes a list of items and returns a user profile. A vector
        representing the likes of the user.
        INPUT:
            items  -   LIST - list of movie names user likes / has seen

        OUTPUT:
            user_profile - NP ARRAY - array representing the likes of the user
                    The columns of this will match the columns of the trained
                    on matrix


        Using the list of items liked by the user create a profile which
        will be a 1 x number of features array.  This should be the
        addition of the values for all liked item features (you can
        choose how to normalize if you think it is needed)
        '''
        user_profile = np.zeros(self.item_counts.shape[1])
        for item in items:
            user_profile += self.item_counts.loc[item].values

        return user_profile

    def get_user_recommendation(self, items, n=5):
        '''
        Takes a list of movies user liked and returns the top n items
        for that user

        INPUT
            items  -   LIST - list of movie names user likes / has seen
            n -  INT - number of items to return

        OUTPUT
            items - LIST - n recommended items


        Make use of the get_user_profile method to create a user profile
        that will be used to get the similarity to all items and
        recommend the top n.
        '''
        num_items = len(items)
        user_profile = self.get_user_profile(items)

        user_sim =  self.similarity_measure(self.item_counts, user_profile.reshape(1,-1))

        return self.item_names[user_sim[:,0].argsort()[-(num_items+n):-num_items]].values[::-1]

if __name__ == '__main__':
    df = pd.read_pickle('data/movie_data.pickle')
    df.set_index('Title', inplace = True)
    df['bag_of_words'] = ''
    columns = df.columns
    for index, row in df.iterrows():
        words = ''
        for col in columns:
            if col != 'Director':
                words += ' '.join(row[col])+ ' '
            else:
                words += row[col]+ ' '
        row['bag_of_words'] = words
        
    df.drop(columns = [col for col in df.columns if col!= 'bag_of_words'], inplace = True)

    # instantiating and generating the count matrix
    count = CountVectorizer()
    count_matrix = count.fit_transform(df['bag_of_words'])

    # creating a Series for the movie titles so they are associated to an ordered numerical
    # list I will use later to match the indexes
    indices = pd.Series(df.index)

    rec = ItemRecommender()
    count_df = pd.DataFrame(count_matrix.todense(), index=indices.values)
    rec.fit(count_df)
    # print(rec.get_recommendations('Fargo'))
    profile = rec.get_user_profile(['The Godfather','The Godfather: Part II'])
    # print(profile[584])
    count.get_feature_names()[584]
    # print(rec.get_user_recommendation(['The Godfather','The Godfather: Part II']))

    # part2
    # news = pd.read_pickle('data/articles.pkl') #not working
    # news.head()
    # news.headline

    # vectorizer = TfidfVectorizer(stop_words='english', max_features=10000)
    # vectorized_df = vectorizer.fit_transform(news.content)

    # news_recommender = ItemRecommender()
    # news_recommender.fit(vectorized_df, titles = news.headline)

    # print(news_recommender.get_recommendations('New York: Two Cities?'))