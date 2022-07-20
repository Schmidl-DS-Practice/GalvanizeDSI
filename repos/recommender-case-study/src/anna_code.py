import pandas as pd

def merge_dataframes(df1, df2, merge_on = 'movieId'):
    df1 = df1.copy()
    df2 = df2.copy()
    new_df = df1.merge(df2, how='left', on=merge_on)
    return new_df

def make_decades(df):
    df = df.copy()
    eighties = df[(df['year'] >= 1980) & (df['year'] < 1990)]
    ninties = df[(df['year'] >= 1990) & (df['year'] < 2000)]
    aughts = df[(df['year'] >= 2000) & (df['year'] < 2010)]
    tens = df[df['year'] >= 2010]
    return eighties, ninties, aughts, tens

if __name__ == "__main__":
    ratings_df = pd.read_csv('../data/ml-latest-small/ratings.csv')
    movies_df = pd.read_csv('../data/ml-latest-small/movies.csv')
    tags_df = pd.read_csv('../data/ml-latest-small/tags.csv')
    links_df = pd.read_csv('../data/ml-latest-small/links.csv')
    movie_rating_df = merge_dataframes(ratings_df, movies_df)

    def to_year(title):
        str_year = title.strip()[-5:-1]
        if not str.isnumeric(str_year):
            return -1
        return int(str_year)

    movie_rating_df['year'] = movie_rating_df['title'].apply(to_year)

    eighties, ninties, aughts, tens = make_decades(movie_rating_df)
    #print(eighties.head())
    u18 = movie_rating_df[movie_rating_df['userId'] == 18][['title', 'rating']]
    print(len(movie_rating_df['userId'].unique()))