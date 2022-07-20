# Content-Based Recommenders

## Introduction
You are going to build a basic recommender for movies.  The data you are going to be using is located in `data/movie_data.pickle`.  It contains the fields `['Title', 'Genre', 'Director', 'Actors', 'Key_words']`. Note that `Key_words` is the most important words from the movie description.  The fields Gener, Actors, and Key_words are all lists of words.  All names have been smashed into one word for simplicity.  This is a small data set of only the top 250 movies from IMDB.

## Basic

### Part 1: Build a recommender
1) Load the data (it is stored as a pickle file so you will have to use something other then `read_csv` to load it). Modify the data set so as to have an indicator column for all directors, genre, actors, and keywords.  (This can be done several ways one is using CountVectorizer after modifying the data into the correct format)

2) Write a model that will take in a DataFrame of items and their attributes it will then take a given index (movie) and return the top n recommended movies (most similar).  There is stub code for this in `src/item_recommender.py`.  Start with the `fit` and `get_recommendations` methods.

3) Test the code and see what movies are recommended with different input.  

4) Fill in code for the `create_user_profile` method.  There are many different ways to calculate this and you can modify the weights for specific parts by hand.  For now just sum up the counts for each movie to create the profile (try normalizing it or not).

5) Fill in the `get_user_recommendation` and test it.  Try several lists of movies.  Can you look into what is causing the movies to be selected?  You can look into the features of the bag of words.

6) What happens to the recommendations if you exclude Actor data and run again?

7) Try another similarity measure, like Jaccard do the results change?

## Advanced

### Part 2: Recommend articles 
Use the New York Times articles data `data/articles.pkl` and test it on the recommender you created. In a previous assignment you used TF-IDF and similarity to rank articles based on a search query so we will not reproduce that but now that we have talked about recommenders do you see how that process was related?  

1) Use the standard [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) and use your ItemRecommender class to get some recommendations. What are the top recommended articles when article 0 is passed in? What are the sections?  

2) Run a few times changing `max_features`, `stop_words`, and even try using CountVectorizer.  How does this change the recommendations?  Why? 

## Extra Credit

### Part 3: Improving the recommender

 With using content-based recommendation the way in which the feature matrix is calculated greatly affects the recommendations.  A higher weight could be put to the genre in our movie recommender or more weight on the keywords.  For the use of our document recommender we can modify the vectorizer to weight words in the title (or first paragraph) as being more important.  This could also help with keyword search and ranking.  

One of the original ideas for document searching involved the idea that if a word showed up in the title it should have more weight in the idea of the content of the document.  The idea being that you could modify TF-IDF in such a way so as the final score would be weighted to if the word showed up in the title it gained more weight.  Think of it like this:
```
TF-IDF(document) = TF-IDF(title) * alpha + TF-IDF(body) * (1-alpha)
```

1) Fit the TfidfVectorizer on all documents with the title included.  This will mean you will have to modify and store a modified version of your data that includes the content and title in one field.  Fit the vectorizer to that data but do not translate it.  What is done in the `fit` method in TF-IDF?

2) Transform the content of the articles and store the output feature matrix.

3) Transform the titles and store the output feature matrix.

4) Create a TF-IDF feature matrix using the formula above and your 2 feature matrix.  Try 2 different alpha values (maybe .9 and .1).

5) Use the Item Recommender and see how the recommendation changes for each alpha.

6) Try transforming search queries and getting the recommended articles from these quires based on the 2 different alphas.


### Part 4: Latent Dirichlet Allocation 

Use Latent Dirichlet Allocation (LDA) to build your feature matrix for the 20 News Group Data and compare results to the use of TF-IDF
 
