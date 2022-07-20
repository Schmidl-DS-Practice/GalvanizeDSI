Solutions to Data-Products Individual Exercises
===============================================

This is a web application that classifies text snippets from newspaper articles according to their high level subject/topic.

Model
-----

The model is purposefully minor: we have implemented a tf-idf vectorizer followed by a naive Bayes classifier, both with the default parameters.  The only novelty here is that both components of the model are wrapped in a single class, which implements the usual sklearn fit, predict_proba, predict API.  This allows us to serialize and manipulate only one object in the application itself.

App
---

There are two implementations of the app, in the `app_with_form` and `app_with_ajax` directory.  The basic functionality of the apps are the same, but

  - `app_with_form` implements the architecture discussed in the assignment.  It uses a html form to pass text data from the user into flask, which then classifies the article and responds.

  - `app_with_ajax` implements a more modern style, with javascript and ajax.  This version uses ajax to pass the text data to flask, which responds with a classification, all without needing to reload another page.  This creates a more seamless user experience.

Setup
-----

To get everything running you need to first create the model object in the appropriate location.  This can be accomplished as follows (assuming you are in the `app` directory):

```
python build_model.py --data data/articles.csv --out static/model.pkl
```

Then start the app you wish to use:

```
python app_with_ajax.py
```

or

```
python app_with_form.py
```
