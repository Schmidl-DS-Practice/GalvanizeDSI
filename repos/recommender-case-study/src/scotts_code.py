import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

plt.style.use('bmh')

def create_dummy_genres(df, genre_lst):
    count = 1
    for i in genre_lst:
        df[i] = 0
        for j in range(df.shape[0]):
            if i in (df.iloc[j,4]):
                df.iloc[j, 4+count] = 1
        count += 1

def make_sns_bar_plot(ax, cols, labels, title, label=None):
    '''
    Creates a seaborn bar plot
    Parameters:
    ax = axes for the plot
    df = dataframe for the data
    col_name = str name of the dataframe column for the heights
    labels = str name of the dataframe column for the x axis labels
    color = color for the bars in the graph
    label = label the graph
    Returns:
    Bar plot
    '''
    
    tick_loc = np.arange(len(labels))
    xlabel = labels
    sns.barplot(tick_loc, cols, ax=ax, label=label)
    ax.set_xticks(ticks=tick_loc)
    ax.set_xticklabels([str(x) for x in xlabel], rotation= 45, fontsize=14)
    ax.set_title(title, fontsize=20)
    
if __name__ =="__main__":
        
    ratings_df = pd.read_csv('data/ml-latest-small/ratings.csv')
    ratings_df.drop('timestamp', axis=1, inplace=True)

    movies_df = pd.read_csv('data/ml-latest-small/movies.csv')

    # print('ratings: \n', ratings_df.head())
    # print('\n', 'movies: \n', movies_df.head())

    ratings_movies_merge = ratings_df.merge(movies_df, how='left', on='movieId')
    # print('\n ratings_movies_merge: \n', ratings_movies_merge.head())

    r = ratings_movies_merge['genres'].to_list()
    ii = []
    for i in r:
        a = i.split('|')
        ii.append(a)
    z = []
    for b in ii:
        z.extend(b)
    z = list(set(z))
    count = 1
    sub_df = ratings_movies_merge.iloc[:100,:]

    # create_dummy_genres(ratings_movies_merge, z) # used to great ratings_movies_merge.to_csv('')
    # ratings_movies_merge.to_csv('data/df_with_genre_dummies.csv')

    df = pd.read_csv('data/df_with_genre_dummies.csv')
    df.drop('genres', axis=1, inplace=True)
    # print(df.head())
    # print('\n', df.info())
    # print(df.sum())

    labels = ['Fantasy', 'Adventure', 'Comedy', 'Action', 'Drama', 
            '(no genres listed)', 'Film-Noir', 'Children', 'Horror',
            'Thriller', 'Sci-Fi', 'Western', 'War', 'IMAX', 'Animation',
            'Romance', 'Documentary', 'Musical', 'Mystery', 'Crime']
        
    lala = {}
    for l in labels:
        if l in df.columns:
            df1 = df[l].sum()
            lala[l] = df1
    lala_v = list(lala.values())
    
    fig, ax = plt.subplots()
    make_sns_bar_plot(ax, lala_v, labels, 'genres')
    plt.show()

