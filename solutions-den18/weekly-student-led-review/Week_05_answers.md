## Week 5 Review Answers

1. What are the assumptions behind OLS linear regression?

  * Linear relationship between predictors and response.
  * Linear independence of regressors (X)
  * Errors (residuals) are normally distributed
  * Errors have mean of 0 (“strict exogeneity”).  E[e | X] = 0
  * (Spherical errors)
    * Homoscedasticity: constant variance of errors
    * No autocorrelation of errors

2. What are some metrics for linear regression goodness of fit, and what do they
   mean?
  
  * RSS = Residual sum of squares. What the model tries to minimize. Scales with
    the number of data points, hard to compare across different training set sizes.  
  * MSE = mean squared error. RSS divided by the number of points in the sample.
  * RMSE = Root mean squared error. Square root of MSE, so it is easy to interpret
    as it is in same scale as Y.
  * R^2 = “proportion of variance explained” by the model = 1 - RSS/TSS.  Between 
    0 and 1, 1 is best.
  * Adjusted R^2 = penalizes R^2 with addition of features
  * F-statistic: Tests whether there is a relationship between predictors and 
    response.  Used to test null hypothesis that all beta coefficients are 0. If
    F is large then p-value of F is small, and your model is not meaningless.

3. In the context of machine learning, what are bias and variance?  And what is 
   the bias-variance trade-off?
   
   Bias is the offset of the expected value of a prediction from the true value.
   Variance is the scatter of the predictions around the expected value.  The 
   bias-variance tradeoff is the general inverse relationship between the two:  
   as model complexity (or flexibility) changes either bias will increase and 
   variance will decrease, or vice versa.  This occurs because the underlying 
   signal is unknown and the data that the model trains on has some irreducible 
   error that is also unknown.  Therefore, changes in model complexity will change
   the ability of the model to fit the training data, and its performance on test
   data will be affected by the inherent assumption associated with the functional
   form of the "signal" in the model and its relation to the true underlying signal.

4. Explain the process you would use to make a generalizable supervised learning model. 
   In the process, compare/contrast cross-validation using a single train-test split 
   to k-fold.  What advantage does k-fold have over a single train-test split?
   Is k-fold always best?

   The secret to making a generalizable model is purposefully withholding data during
   the training phase, and checking how well the trained model does on data it hasn't
   seen.  If you do this for several models (e.g. Logistic Regression vs. Random 
   Forest Classifier) and design matrices (X) with different features 
   (inclusion/exclusion of features, feature engineering, reduction in dimensionality),
   you increase the chance your selected model trained on certain features 
   will generalize well on unseen data.
    
   The general process is:
   * Take whatever data you have and split it into a train and hold-out set.
     Forget about the hold-out set.  It will be used at the very end to provide
     an estimate for how your selected model performs on truly unseen data.
   * Now you will go through a cross-validation process.  This entails
     * Selecting a model, its hyper-parameters, and picking features 
     * Splitting the original train data into at least one train/test set, or 
       multiple train/test sets if doing k-fold
     * Training the model on the train set, and then recording its performance on
       the test set (or on multiple test sets, if using k-fold).
   * Picking the best model, hyper-parameters, and features based on
     performance on the test set(s).
   * Retraining that model on the entire train set.
   * Evaluating the model on the hold-out set.  

   k-fold is generally better than a single train-test split in the cross-validation
   process because you get several estimates for model performance given the model,
   its hyper-parameters, and features.  The estimates are usually averaged, which
   helps remove variance in performance that will naturally occur if you only use 
   a single train-test split.  So therefore the estimate of model performance obtained
   using cross-validation is more reliable than a single train-test split.

   However, when model training time is expensive (in time or money) then a
   single train-test split could be preferable.

5. A coworker explained his machine learning workflow to you, and you have a suspicion that there's 
   something wrong about it:

   "After I got the data I immediately did a train-test split to make a hold-out set.  Then
    I standardized the remaining training data and used 5-fold cross-validation to determine the best
    model hyper-parameters.  I used AIC as my model comparison metric.  I took the hyper-parameters
    I got from cross-validation and trained a model on the full training set.  Then I got my AIC
    on the hold-out set and it didn't do as well, by a long shot, as it did during cross-validation."

    Where did he go wrong?

    He standardized all the training data before going through the 
    cross-validation process.  This is a short-cut that some people make,
    but it violates the idea of the test set being unseen data, because
    the test set data (initially within the train set) contributed to
    the means and variances of the features through which the whole 
    data set was standardized.

6. What is the curse of dimensionality in machine learning?  What can you do to 
   address it?

   As the number of dimensions increase, the volume that the existing data occupy
   grows exponentially. You can relate the sample density in two differently 
   dimensioned spaces through the relation N1^(1/D1) ~ N2^(1/D2) where N1 and N2 
   are the number of samples in dimensions D1 and D2.  In high dimensional spaces
   all distance based metrics are far apart, or of equivalent magnitudes.    
   
   Common ways that dimensionality are addressed are by 1) gathering more data, 
   2) regularization, 3) collapsing multiple dimensions into fewer dimensions that
   contain the most variance (PCA, SVD), and 4) if a distance metric is required,
   using something like cosine similarity instead.

7. We talked about L1 and L2 regularization.  What are they and in what situations 
   might you use one instead of the other?
  
   Regularization is a technique to control overfitting by introducing a penalty
   term over the error function to discourage coefficients from reaching large values.
   L1 regularization (Lasso) regularizes using the absolute values of the coefficients,
   while L2 regularization (Ridge) regularizes using the square of the coefficients.

   In the case of two features that are collinear, an L1 will eventually pick one and
   zero the other one out, while L2 will shrink both coefficients.  And so depending
   on use case L1 or L2 might be preferable here.

   If you have a sparse signal (most of your features aren't predictive), then L1
   will do a better job finding the few predictive features.

   L2 will generally make more predictive models than L1.

   Remember you can have both: it's called an Elastic Net.

8. Draw a confusion matrix for binary predictions.
  
   || Predict N | Predict P |
   |-|:-:|:-:|
   | Actual N |TN|FP|
   | Actual P |FN|TP|  


9. Give an example for each case:
   * Precision is more important than recall.  
    
     Precision is the fraction of the predicted positives that were actually 
     positive. This would be more important in prison sentences and courts. 
     `TP/(TP+FP)`

   * Recall is more important than precision.  
    
     Recall is the fraction of the actually positive cases that were predicted 
     positive.  This would be more important in community health related domains,
     such as catching possible sources of contaminated food, or early screening 
     for disease. `TP/(TP+FN)`

   * You consider both to be important (and what metric would you use for that?)
   
     The F1 score is the harmonic average of precision and recall and often used 
     as a metric that takes both into account.  You'd like a process that screens 
     for an expensive medical procedure to have a large F1 score.

10.  How is a ROC curve generated?  What does it show?

     A ROC curve is made by taking predicted classification probabilities and 
     thresholding them to a positive or negative class to compare to actual 
     classifications to get true and false positive rates for that model evaluated 
     at that threshold. The ROC curve then displays the effect of the threshold on 
     the true positive and false positive rates for all thresholds. ROC curves are 
     useful for comparing models and the effect of the classification threshold in 
     a given model.

11. What are the similarities and differences between linear and logistic 
    regression and how do you interpret the coefficients in each case?
    
    Both are linear models where the response is a linear function of the inputs.
    However, in linear regression the target or response *is* the sum of the 
    coefficients and the inputs, yielding a continuously values response, while 
    in logistic regression the sum of the coefficients and inputs is related to 
    the logit - the log odds of (usually) the positive class occurring.  A 
    classification threshold is used with the probabilities calculated from the 
    odds to classify samples into discrete classes.

12. SQL: Given table `houses` below, write a query to...

    | id | sqft | beds | neighborhood | type | sale_price |
    |:----------:|:------------:|:----------:|:----------:|:-----------:|:-----------:|
    | 1 | 1150 | 2 | prospect-park | townhome | 244052 |
    | 2 | 2600 | 3 | calhoun-isles | single_family | 609536 |
    | 3 | 860 | 1 | uptown | condo | 472993 |
    | 4 | 1320 | 3 | north-loop | townhome | 309485 |
    | 5 | 1030 | 2 | downtown | townhome | 456141 |
    | 6 | 3000 | 3 | uptown | single_family | 544431 |
    | 7 | 1400 | 2 | longfellow | condo | 305314 |
    | 8 | 3000 | 4 | longfellow | single_family | 485802 |
    | 9 | 1700 | 3 | stephens-square | single_family | 337029 |

   * Return the average number of bedrooms and square footage for each type of home in the longfellow neighborhood.
     ```SQL
     SELECT type, AVG(beds) AS avg_beds, AVG(sqft) AS avg_sqft
     FROM houses
     WHERE neighborhood = 'longfellow'
     GROUP BY type
     ```
   * Return the average sale price for each neighborhood and home type.
     ```SQL
     SELECT neighborhood, type, AVG(sale_price) AS avg_price
     FROM houses
     GROUP BY neighborhood, type
     ```
