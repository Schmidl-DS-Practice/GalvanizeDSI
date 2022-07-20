## Week 5 Review Questions

1. What are the assumptions behind OLS linear regression?

2. What are some metrics for linear regression goodness of fit, and what do they mean?

3. In the context of machine learning, what are bias and variance?  And what is the bias-variance trade-off?

4. Explain the process you would use to make a generalizable supervised learning model. 
   In the process, compare/contrast cross-validation using a single train-test split 
   to k-fold.  What advantage does k-fold have over a single train-test split?
   Is k-fold always best?

5. A coworker explained his machine learning workflow to you, and you have a suspicion that there's 
   something wrong about it:

   "After I got the data I immediately did a train-test split to make a hold-out set.  Then
    I standardized the remaining training data and used 5-fold cross-validation to determine the best
    model hyper-parameters.  I used AIC as my model comparison metric.  I took the hyper-parameters
    I got from cross-validation and trained a model on the full training set.  Then I got my AIC
    on the hold-out set and it didn't do as well, by a long shot, as it did during cross-validation."

    Where did he go wrong?

6. What is the curse of dimensionality in machine learning?  What can you do to address it?

7. We talked about L1 and L2 regularization.  What are they and in what situations might you use one instead of the other?

8. Draw a confusion matrix for binary predictions.

9. Give an example for each case:
  * Precision is more important than recall.  

  * Recall is more important than precision.  

  * You consider both to be important (and what metric would you use for that?)

10. How is a ROC curve generated?  What does it show?

11. What are the similarities and differences between linear and logistic regression and how do you interpret the coefficients in each case?

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

  * Return the average sale price for each  neighborhood and home type.
