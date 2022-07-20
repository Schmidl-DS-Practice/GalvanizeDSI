##MINE ANSWERS
#1
'''Assumptions of Inferential Linear Regression
1. Linearity: the relationship between the X and the y can be modeled linearly
2. Independence: the residuals should be independent from each other
3. Normality: the residuals are normally distributed
4. Homoscedasticity: the variance of the residuals is constant
Note: you might see other assumptions mentioned if you do a quick Google
search and we will briefly touch on one of the main ones:
5. No multicollinearity: the independent variables are not highly correlated with
each other'''

#2
'''RSS, MSE, RMSE r^2, adjusted r^2'''

#3
'''bias - accurancy of our predictions. error from assumptions
variance - difference between many models predictions.
variance is an error from sensitivity to small fluctuations in the training set.
High variance can cause an algorithm to model the random noise in the training data, 
rather than the intended outputs (overfitting).
bias-variance trade-off - inversely correlated. with low k: high variance
low bias "overfitting"; with high k: low variance high bias.'''

#4
'''clean your data, split(stratify it: the distribution of your test set replicates
the ratio of the distribution of the classes in your whole data set), cross validate
your model to get best hyperparameter/use traiing set to train several models
of varying complexity, evaluate each model using validation set, keep the model that
performs thebest over the validation set.
-k-fold you split the data into k # of folds, fit the model to the fold
and perform the evaluation metric on each fold, average them.
-k-fold is better because it account for variance in training set, the estimate is less
variable. usually the better option.'''

#5
'''took data and split it initially, he then took the training data and split it again
to do k-folds cross validation. he also didn't standarie the test data, which
affected the metric of how well the model was fitting.'''

#6
'''The more features you have, the data becomes 'further away' from each other,
which makes finding a pattern harder. the data becomes less dense. removing
collinear features, perform dimensionality reduction, reduce complexity, get more data.
'''

#7
'''Lasso-L1, sets coefficients exactly to zero, use feature selection(auto),
   sparse models, stepwise feature selection. Better for sparse models.
   Ridge-L2, computationally easy because it forces the parameters to be small
   Also differentable. Better for dense models'''

#8
'''assignment from decision rules'''

#9
'''recall-minimize false negative.
   precision-minimize false positive
   accuracy-balance dataset
   f1 score-imbalanced dataset'''

#10
'''plot true positive rate vs false positive rate. total performance by area under
curve. get closest to one you can.'''

#11
'''linear-sum of products of the coefficients and features is the target yhat. 
continuous dependent variables using a given set of independent variables.
best fit line
   logistic-sum of products and features is the target logodds.
predict values that are categorical variables.
s-curve(sigmoid)'''

#12
'''SELECT AVG(beds), sqft
   FROM houses
   WHERE neighborhood = 'longfellow'
   GROUP BY type;
   
   SELECT AVG(sale_price)
   FROM houses
   GROUP BY neighborhood, type;
   '''
##JENNY'S ANSWERS

## Week 5 Review Questions
​
#1. What are the assumptions behind OLS linear regression?\
 - linearity(relationship between X + y can be modeled linearly), independence(residuals are independent), normality(residuals are normally distributed), homoscedasticity(variance of residuals is constant), no multicolinearity (independent variables are not highly correlated)
​
#2. What are some metrics for linear regression goodness of fit, and what do they mean?
 - RSS, MSE, RMSE, R^2, adjusted R^2
​
#3. In the context of machine learning, what are bias and variance?  And what is the bias-variance trade-off?
 - bias is the accuracy of our predictions. Error from erroneous assumptions in the learning algorithm (high bias - the model gives you the same answer regardless of )
 - variance is the difference between many model's predictions, the error from sensitivity to small fluctuations in the training set. (crazy line)
​
 - bias, variance tradeoff - either low bias/high variance(overfit) or high bias/low variance(predictions are similar to one another, but they're inaccurate on average). 
​
#4. Explain the process you would use to make a generalizable supervised learning model. 
   In the process, compare/contrast cross-validation using a single train-test split 
   to k-fold.  What advantage does k-fold have over a single train-test split?
   Is k-fold always best?
​
   - clean your data, split it (stratify it: the distribution of your test set replicates the ratio of the distribution of the classes in your whole data set), cross validate your model to get the best hyper-parameters/use training set to train several models of varying complexity, evaluate each model using the validation set, keep the model that performs the best over the validation set
​
   - k-fold you split the data into k # of folds, fit the model to the fold, and perform the evaluation metric on each fold, average them. In the single you do it once.
​
   - k-fold is better because it accounts for variance in training set, the estimate is less variable. Usually the better option.  
​
#5. A coworker explained his machine learning workflow to you, and you have a suspicion that there's something wrong about it:
​
   "After I got the data I immediately did a train-test split to make a hold-out set.  Then I standardized the remaining training data and used 5-fold cross-validation to determine the best model hyper-parameters.  I used AIC as my model comparison metric.  I took the hyper-parameters I got from cross-validation and trained a model on the full training set.  Then I got my AIC on the hold-out set and it didn't do as well, by a long shot, as it did during cross-validation."
​
    Where did he go wrong?
​
  - He took the data and split it initially, he then took the training data and split it again to do k-fold cross validataion. He also didn't standardize the test data, which affected the metric of how well the model was fitting.
​
#6. What is the curse of dimensionality in machine learning?  What can you do to address it?
 - The more features you have, the data becomes 'further away' from eachother, which makes finding a pattern harder. The data becomes less dense. Removing colinear features, perform dimensionality reduction, reduce complexity, get more data.
​
#7. We talked about L1 and L2 regularization.  What are they and in what situations might you use one instead of the other?
 - Lasso - L1, sets coefficients exactly to zero, use for feature selection (auto), sparse models, stepwise feature selection. Better for sparse models.
 - Ridge - L2, computationally easier because it forces the parameters to be small. Also differentiable. Better for dense models.
​
#8. Draw a confusion matrix for binary predictions.
​
                   | actual positive | actual negative |  
predicted positive |                 |                 |  
--------------------------------------------------------
predicted negative |                 |                 |
--------------------------------------------------------
​
#9. Give an example for each case:
  * Precision is more important than recall.  
 - when you want to minimize false positives
  * Recall is more important than precision.  
- when you want to minimize false negatives
  * You consider both to be important (and what metric would you use for that?)
 - accuracy when you have a balanced dataset, F1 score when you have an imbalanced dataset
​
#10. How is a ROC curve generated?  What does it show?
 - TPR vs FPR, shows the total performance by area under the curve, you want to get closest to 1, find the balance of highest TPR and FPR.
​
#11. What are the similarities and differences between linear and logistic regression and how do you interpret the coefficients in each case?
 - LINEAR: continuous, best-fit, sum of products of the coefficients and features is the target yhat.
 - LOGISTIC: categorical, s-curve (sigmoid), the sum of products and features is the target logodds.
​
#12. SQL: Given table `houses` below, write a query to...
​
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
​
  * Return the average number of bedrooms and square footage for each type of home in the longfellow neighborhood.
​
  SELECT type, AVG(beds), AVG(sqft)
  FROM houses
  WHERE neighborhood = 'longfellow'
  GROUP BY type;
  
  * Return the average sale price for each  neighborhood and home type.
​
  SELECT AVG(sale_price)
  FROM houses
  GROUP BY neighborhood, type;