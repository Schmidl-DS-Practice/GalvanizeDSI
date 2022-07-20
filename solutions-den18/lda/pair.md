## LDA Pair Exercise

#### In honor of Halloween, we've got a spooky dataset for you. It's a bunch of Wikipedia articles from horror movies and paranormal events.

We're going to use Latent Dirichlet Allocation to do topic modeling on the articles. The first goal is to discern what are the distinct topics within the dataset, and what features describe them. Then we'll write a function that takes a given article and returns the most similar articles

1. Load the data from spooky_wikipedia.csv. Since this is a Wikipedia dump, there are some pages (such as lists) that we're not interested in so remove those. There are also some pages that have no text, so remove those as well. There's about 24,000 articles right now so take a smaller sample of that to start with (~1000).

2. Vectorize the corpus. Note that LDA generally does not take a TF-IDF matrix, but a bag-of-words vector (you can use sklearn's count vectorizer). You can start with the default stopwords, but you'll probably want to update those later. We'll tune some of these other hyperparameters later but start with max_df = 0.85, min_df=2 and max_features=1000.

3. Create an <a href="http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html">LDA instance </a> and think about what each of the parameters mean. In our use case, what does n_components represent? How do we input our alpha and beta priors? Use the 'online' learning method and n_jobs=-1 (all cores) or -2 (all cores but one) to speed up your processing.

4. Fit the LDA model on your vectorized corpus.

5. Examine the generated topics. what does lda.components_ represent? How do we determine the most important features in a topic? Write a function that takes the most important features for each topic in lda.components_, then uses the feature names from the vectorizer to print out the most important words for each topic. What do you think each topic describes? Try adding some words to your stopwords to make your categories more specific to spooky topics and less to wikipedia topics.

##### Checkpoint 1: Nice work; you've learned how to fit an LDA model and examine the topics to gain an intuitive understanding of the latent associations in a set of documents.  


Helpful hint: if you don't want to keep fitting your vectorizer and lda model over and over again, you can persist them (save them to a file) with joblib (similar to pickle but optimized for large data)

```python
    joblib.dump(lda, 'lda_model.joblib')
    joblib.dump(vectorizer, 'tf_vec.joblib')
    lda = joblib.load('lda_model.joblib')
    tf_vectorizer = joblib.load('tf_vec.joblib')
    # It's that easy!
```
Let's now work on creating a function that will take the name of an article and return the names of n articles most closely related to it.

6.  First we need to turn our vectorized corpus into a topic probabilities for each document. Which method of our model will return this?

7. Next, given a certain article, we need to compute the distance between this and every other document. sklearn.metrics.pairwise has great functions for cosine distance and euclidean distances here. How will the two differ in the way that they find which articles are the most similar?

8. Use cosine distance to create a vector that contains the distance from our document to every other document. Use argsort to determine the closest top 10.

9. Now we have an array that contains the indices of all of the most similar articles, we're almost there! Write a function that takes this array and returns the name of the input article as well as its most similar articles.

##### Checkpoint 2: Congratulations! You've just created a very useful recommender using LDA. This is a practical use-case; websites often use a similar approach to determine the articles for recommended reading that appear below the article text or in sidebars.

10. Do your recommendations make sense? Try changing hyperparameters of your count vectorizer and your LDA model to try to improve them!
I had pretty good results using the full dataset and these parameters:
```python
    lda = LatentDirichletAllocation(n_components = 30, learning_offset =50., verbose=1,
                                    doc_topic_prior=0.9, topic_word_prior= 0.9,
                                    n_jobs=-1, learning_method = 'online')
    tf_vectorizer =  CountVectorizer(max_df=0.85, min_df=2, max_features = 1000,
                                    stop_words=stop_words, ngram_range = (1,3))
```
Since we don't have traditional error metrics like we would in a supervised learning approach, it's hard to tune these hyperparameters in the same way. We can, however, use log-likelihood as a scoring function. We split our data, train our model, and then determine the likelihood that that our model of the documents could have generated the unseen text. The higher this value, the "better" we have modeled our corpus.
Using sklearn GridSearchCV, tune the number of topics using cross validation on log-loss(equivalent to negative log-likelihood; log-loss is the default scorer for the sklearn LDA model).

Extra credit: put this all into a class for easy usage!
