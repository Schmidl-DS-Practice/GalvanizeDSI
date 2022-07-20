## Week 6 Review Questions

1. Write out the cost functions for:  
  * Ordinary least squares  

  * Linear regression using L1 regularization 

  * Linear regression using L2 regularization  

  * Linear regression using Elastic net  


2. You're trying to make model that will predict the female gold medal winner in the high jump in the next Olympics.  You have results and data for 1000 high-jumpers in the past.  You're using four features: `jumper_height`, `jumper_weight`, `best_jump_height`, and `fastest_100m_time` as features and your model performs ... just ok during cross-validation. Then it hits you: you also have `maximum_squat_weight` for all the jumpers, why don't you use that as a feature too?  Using this additional feature (5 total now) during cross-validation, however, you get widely varying estimates of model performance.  
  * What do you think is going on?  

  * As a bonus, how many data points would you need with 5 features to have the same sample density as your model had with 4 features?  

3. Decision tree questions:  
  * Describe, step-by-step, how a decision tree is built.  

  * Describe how a binary split is made at a node in the case of:  
    * classification  

    * regression  

    * You decide to use a Decision Tree on the Olympic high jumper problem and you end up with a model that does very well on the training data but predicts poorly in cross-validation.  What can you do?  

4. What are the two things that make a random forest "random"?  

5. What problem from bagging is solved by using a random forest? Hint: what type of algorithm is a decision tree split?  


6. You are a data scientist at a subscription company, and you decide to use a random forest model for predicting churn. The model works well, but your boss wants some insight into what factors contribute to customer churn. What can you tell him/her?  

7. Compare and contrast random forests and boosted trees with regards to:  
  * The data that each tree in the ensemble is built on. 

  * How the quality of a split on a given feature and its value is evaluated.   
  
  * The general depth of each tree.  

  * The bias-variance trade-off associated with each tree in the ensemble. 

  * How the ensemble can achieve a low-bias, low-variance model.  
