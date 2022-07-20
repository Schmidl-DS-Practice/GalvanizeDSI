
Improving Movie Recommendations for your Customer
=======================

Let us help your users stay engaged and up to date with your latest content!


Team Suggestions
---------------------

Three ways to increase engagement for your users:

  1. **New Users** - Suggesting Top movies from all time, and top decade movies
  2. **Current Users** - Suggestions for user based on reviews
  3. **HYBRID** -  Suggestions for user based on reviews, and top decade movies

### New Users

Top 8 All Time

<p align="center">
    <img src="https://media.giphy.com/media/KGBjjGHK1eAwAqdAwb/giphy.gif">
</p>
<p>&nbsp;</p>

Movies for your 80's Movie Night

<p align="center">
    <img src="https://media.giphy.com/media/jP4iZf7SsBpv3yKAQH/giphy.gif">
</p>
<p>&nbsp;</p>




Existing Client Recommender Models
--------------------------------------

|  Genre Categories                     |
|:---------------------------------------:|
|  Fantasy, Adventure, Comedy, Action, Drama, Film-Noir, Children, Horror, Thriller, Sci-Fi, Western, War, IMAX, Animation, Romance, Documentary, Musical, Mystery, Crime |

<br>
<br>


### Example User 18


User 18 has rated 502 movies. <br>
**5 Star Movies:**
* The Good, the Bad and the Ugly
* Once Upon a Time in the West   
* Shawshank Redemption  
* Citizen Kane   
* The Usual Suspects    
* The Godfather: Part II 
* 12 Angry Men   

**Based on user ratings, we think User 18 would also enjoy:**
* A streetcare Named Desire
* The Philadelphia Story
* Glory
* Star Wars: Episode V - The Empire Strikes Back

5 Star Movies            |  Our Recommendations
:-------------------------:|:-------------------------:
<img src="https://media.giphy.com/media/eK0ycZaB7dGtY19wvL/giphy.gif">  |  <img src="https://media.giphy.com/media/Te17mNjGyDc8VsFH0f/giphy.gif">

The data on the models
--------------

We ran three models on a 100,000 rating sample with a single 3Ghz processor. 


|             | Validation RMSE | Training Time per 100k ratings (seconds) | **Reduction in Churn**
|------------:|----------------:|---------------------------------:| ---------:|
| **Model**   |                 |                                  |     |
| MeanOfMeans |            0.93 |                       0.55        |        -       |
|         SVD |            0.89 |                       2.8        |       4.3%      |
|       SVD++ |            0.87 |                     203.0        |       6.4%     |



The SVD model predicted about 5% better than the current model at roughly four times the training time, and the SVD++ model predicted a further 3% better at the cost of two-hundred times the training time.

Cost Benefit Analysis
-----------------------

The model training was done on a one 3GHZ processor, which is roughly equilveant to the power of one AWS vCPU. At the current AWS rate, a processing unit with 64 cores and sufficient RAM costs approximately two dollars an hour to run. If our company has 100 million subscribers, we may have upwards of a billion total ratings from all users, 10,000 times more ratings than the training sample. This would take 

|    **Model**  | Estimated Full Training Time (minutes) | Estimated Training Cost (Dollars) |
|------------:|---------------------------------------:|----------------------------------:|
| MeanOfMeans |                                     1.3 |                              0.05 |
|         SVD |                                    8.8 |                               2.5 |
| SVD++       | 617                                  | 17.6                              |

Even training the most expensive model would be trivial compared to any reasonable 

Next Steps
------------------
* Run models on premium AWS server 
* Try statistical modeling on different genre categories





    

#### Repo Initially Forked from jlan84. Due to Forking Repo was Initially Private.
