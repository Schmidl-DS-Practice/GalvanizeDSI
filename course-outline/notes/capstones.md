# DSI Capstone guide

Capstone projects showcase your data science skill and passion.  They 
result in a digital portfolio of public Github repositories that you can talk
about with potential employers.  We've had employers waive in-person coding 
requirements because an applicant's Github "looks great."  We hope that happens
to you.

Quick links:
* [Capstone I](#Capstone-I)
* [Capstone II](#Capstone-II)
* [Capstone III](#Capstone-III)

# Capstone I

## Components of a Good Capstone
The Galvanize curriculum has been tailored over time to equip you with skills 
requested in the job market.  Look to showcase these skills: 

* **Well Written Code**  
There's a reason that we test for Python in our entrance exam and work on it 
every day.  Code is how you to bring ideas to life.  Code is what you share with
others to get a job done.  Well written code with relevant documentation is your
ticket to working with others.

* **A Helpful, Organized Github Repository**  
Make it as easy as possible for those from diverse backgrounds to understand your 
capstone.  Have a well written `README.md` that introduces your project at a high 
level for all to understand, but also provides depth for those looking for it. 
Organizationally, put Python scripts in the `src` folder, Jupyter notebooks in 
a `notebooks` folder, data (probably just a subset) in a `data` folder, tests
for your Python scripts in a `tests` folder, and images in an `images` folder.

Here are some examples of excellent READMEs and Githubs from past first capstones:
* [Traffic Accidents in Denver](https://github.com/johnherr/Traffic-Accidents-in-Denver)
* [Purifying Hearthstone Data](https://github.com/NJacobsohn/Hearthstone-Data-Analysis)
* [Does Work-Life Balance Matter?](https://github.com/tsandefer/dsi_capstone_1)
* [Services provided by Non-State actors](https://github.com/gagejane/Terrorism-NonViolent)

* **Evidence of Data Wrangling**
Data wrangling - the process of cleaning and unifying messy and complex data sets 
for easy access and analysis - consumes a large part of our jobs as data scientists. 
Clean datasets aren't the norm, so most likely whatever data you have will be 
sufficiently messy to show your skill.  However, there are some sites that host 
data that may have already been cleaned or featurized (Kaggle, for instance) that 
don't present much of a challenge.  Check with your instructors if you have questions 
about the cleanliness of your data.

## Capstone I specifics
Your first capstone project comes before you have learned anything about machine 
learning.  Many students wonder why we choose to have a capstone at this time, 
but it turns out that demonstrating mastery of the technological and statistical
foundations of the field are very powerful examples of your ability to quickly 
integrate onto DS teams.  As a reminder, your capstone projects should serve as 
demonstrations of a large and general skill set. 

### Skills to Feature
#### Web Scraping
Being able to create your own dataset is a powerful skill that requires practice.
This is a great opportunity for you to work with ```BeautifulSoup```, 
```Selenium```, and ```Scrapy``` in order to create a novel dataset.
Note the complications acquiring data that you experience in this process. 
Lessons learned will help you with making and cleaning datasets in the future. 

*BONUS* - Often the most interesting studies come from combining multiple sources 
of information.  Make an entirely new dataset that helps you answer a specific
problem.   

#### Data Pipelines
Information is not data.  Data is well formatted, regular, and able to be 
leveraged by statistical models.  As such, building a pipeline that will clean 
and transform the data into well formatted files is very important.  If you 
web-scraped into Mongo, consider a pipeline that will read in `.json` from Mongo 
and write tabular, cleaned data to PostgresQL.

#### Data Visualization
A significant portion of this project should be devoted to data exploration and plotting. 
Make sure to follow best practices (axis labels with easily legible font!).  

#### Hypothesis Testing
This capstone is an excellent time to demonstrate your ability to conduct a 
statistical study.  Remember that test power, significance levels, the null
and alternate hypotheses should be conducted before a single byte of data is 
collected.

*Note* - many students feel that if they fail to reject their null hypothesis, 
their capstone is a failure.  As scientists, we should be dispassionate about 
the outcomes of our studies.  This means that if we only have results where we 
fail to reject the null, we're either being unscrupulous or unambitious. 

## Capstone I proposal  

You need to write-up a Capstone I proposal and submit it to your instructors for
review.  Please submit a **one-page PDF** file (no text files, markdowns, or 
Word Documents).

The proposal should:

1) State your question.  What is it that you are curious about?  What are you looking 
for in the data?

2) Demonstrate that you have looked at your data.  What are your columns?  Are they
numerical/catagorical?  How many Nan's are there?  Have you made a couple of plots? 
We only have a week for this capstone; it's hard to do a good job when you've only 
had the real dataset for a couple of days.  This can make it challenging to 
work with a company.  Their timescale is different from the DSI.  "Fast" for them is a 
couple of weeks.  You needed the dataset yesterday.

3) State your MVP.  MVP is your Minimum Viable Product.  What's the minimum that you 
hope to accomplish?  Then, feel free to expand on MVP+, and MVP++.  

## Evaluation  
The three capstones account for 40% of your DSI assessment score/grade.  The scores
equally weight each capstone, and equally weight the presentations (~10 minutes) and 
accompanying Github for each capstone.  

#### Capstone I Github scoring rubric:

|Scoring item                          |Points | Description                                                 |
|:-------------------------------------|:-----:|:------------------------------------------------------------|
|Repo. organization and commit history |   3   | 0: No organization, 1 commit.<br> 1: Poor organization, 3+ commits.<br> 2: Ok organization, 3+ commits.<br>3: scripts in `src`, jupyter notebooks in `notebooks`, data, images, and other files similarly organized and 5+ commits.|
|Appropriate use of scripts/notebooks  |   3   | 0: Everything in a jupyter notebook.<br> 3: Perhaps some EDA presented in notebooks, but data acquisition, cleaning, and important analyses in scripts.|
|Object-oriented programming           |   3   | 0: You are repeating repeating yourself yourself.<br> 2: In functions.<br> 3: Appropriate use of classes|
|Code style                            |   3   | 0: It is difficult to understand what your code is doing and what variables signify. <br>2: Good variable/function/class names, `if __name__ == '__main__'` block, appropriate documentation.<br>  3: All previous and would perfectly pass a [pycodestyle](https://pypi.org/project/pycodestyle/) test.|
|Coding effort (in scripts)            |   3   | 0: <= 50 lines of code.<br> 1: 51-100<br> 2: 101-150<br> 3: > 150     |

#### Capstone I presentation scoring rubric
|Scoring item                          |Points | Description                                                 |
|:-------------------------------------|:-----:|:------------------------------------------------------------|
|Project question/goal                 |   2   | 0: What are you doing?<br> 1: Theme explained, but no clear question/goal.<br>2: Stated clearly with gusto.        |
|Description of raw data               |   2   | 0: Mentioned in passing - no idea of what the features are, where it came from, how it was obtained.<br>  1: Just a few features, the source described in text (but no images of raw data.)<br> 2: Source described, walk through exemplary features and rows, appropriate tables/screenshots.|
|Exploratory Data Analysis             |   3   | 0: Who needs to understand the data, anyway? <br>1: Perfunctory - general pair-wise scatter matrix that says..what?<br> 2:  Documentation of interesting relationships between the features and target. <br>3: All previous and with thoughtful feature engineering.|
|Analysis (e.g cleaning pipeline, database creation, statistical tests) |   5   | 0: None<br> 1: Approach invalid/unsuited to problem.<br>  2: Brief description focused on results without any explanation of approach/method.<br> 3: Clearly explained process that my be slightly incomplete or with minor errors.<br>4: Clearly explained with no/few errors.<br> 5: Impressive effort.| 
|README                                |   3   | 0: Missing or useless in describing project.<br>  1: Misspellings, hard to read font, strange formatting, ugly screenshots, inconsistent text sizes, wall-of-text.<br> 2: Generally pleasing that describes project well - good illustrations, a few minor issues. <br>3: Beautiful and an impressive showcase for the project with good organization, appropriate use of text and illustrations, and helpful references.|

# Capstone II

For most, Capstone II is a start on your final capstone project.  Quality data,
EDA, and feature engineering take time and are as important in this Capstone II
as Capstone I.  They set you up for success.  

## Capstone II goals

* An MVP that demonstrates supervised or unsupervised learning (and maybe both).
* In the case of supervised learning, picking an appropriate metric to quantify 
  performance, and then use of that metric in cross-validation to arrive at
  a model that generalizes as well as possible on unseen data.  Be prepared 
  for the request: "Describe the process you used to ensure your model
  was properly fit."
* In the case of unsupervised learning, picking an appropriate clustering 
  method and metric to guide the choice of the number of hard or soft clusters.
  This should be followed up with a thoughtful discussion as to why the 
  chosen number of clusters is "correct."
* In all cases, discussion of the cleaning and featurization pipeline and how 
  raw data were transformed to the data trained on.  Text processing especially
  requires discussion.  
* In the case of classification and class imbalance, discussion of how the
  class imbalance was addressed.  Did you use a default decision threshold,
  or did you pick a different threshold through out-of-model knowledge (e.g.
  a cost-benefit matrix and a profit curve.)


## Capstone II proposal  

You need to write-up a Capstone II proposal and submit it to your instructors for
review.  Please submit a **one-page PDF** file (no text files, markdowns, or 
Word Documents).

The proposal should:

1) State your question.  What is it that you are curious about?  What are you looking 
for in the data?

2) Demonstrate that you have looked at your data.  What are your columns?  Are they
numerical/catagorical?  How many Nan's are there?  Have you made a couple of plots? 
We only have a week for this capstone. It's very hard to do a good capstone when 
you've only had the real dataset for a couple of days.  This can make it challenging to 
work with a company.  Their timescale is different from the DSI.  "Fast" for them is a 
couple of weeks.  You needed the dataset yesterday.

3) State your MVP.  MVP is your Minimum Viable Product.  What's the minimum that you 
hope to accomplish?  Then, feel free to expand on MVP+, and MVP++.  

## Evaluation  
The three capstones account for 40% of your DSI assessment score/grade.  The scores
equally weight each capstone, and equally weight the presentations (~10 minutes) and 
accompanying Github for each capstone.  

The rubrics for Capstone II are similar to Capstone I.

#### Capstone II Github scoring rubric:

|Scoring item                          |Points | Description                                                 |
|:-------------------------------------|:-----:|:------------------------------------------------------------|
|Repo. organization and commit history |   3   | 0: No organization, 1 commit.<br> 1: Poor organization, 3+ commits.<br> 2: Ok organization, 3+ commits.<br>3: scripts in `src`, jupyter notebooks in `notebooks`, data, images, and other files similarly organized and 5+ commits.|
|Appropriate use of scripts/notebooks  |   3   | 0: Everything in a jupyter notebook.<br> 3: Perhaps some EDA presented in notebooks, but data acquisition, cleaning, and important analyses in scripts.|
|Object-oriented programming           |   3   | 0: You are repeating repeating yourself yourself.<br> 2: In functions. <br>3: Appropriate use of classes|
|Code style                            |   3   | 0: It is difficult to understand what your code is doing and what variables signify.<br> 2: Good variable/function/class names, `if __name__ == '__main__'` block, appropriate documentation.<br>  3: All previous and would perfectly pass a [pycodestyle](https://pypi.org/project/pycodestyle/) test.|
|Coding effort (**in scripts**)            |   3   | 0: <= 50 lines of code<br> 1: 51-100<br> 2: 101-150<br> 3: > 150     |

#### Capstone II presentation scoring rubric
|Scoring item                          |Points | Description                                                 |
|:-------------------------------------|:-----:|:------------------------------------------------------------|
|Project question/goal                 |   2   | 0: What are you doing?<br> 1: Theme explained, but not clear question/goal stated.<br> 2: Stated clearly with gusto.        |
|Description of raw data               |   2   | 0: Mentioned in passing - no idea of what the features are, where it came from, how it was obtained.<br>  1: Just a few features, the source described in text (but no images of raw data.) <br>2: Source described, walk through exemplary features and rows, appropriate tables/screenshots.|
|Exploratory Data Analysis             |   3   | 0: Who needs to understand the data, anyway?<br> 1: Perfunctory - general pair-wise scatter matrix that says..what?<br> 2:  Documentation of interesting relationships between the features and target.<br> 3: All previous and with thoughtful feature engineering.|
|Analysis (e.g cleaning pipeline, modeling, validation of model, presentation of results) |   5   | 0: None<br> 1: Approach invalid/unsuited to problem.<br>  2: Brief description focused on results without any explanation of approach/method.<br> 3: Clearly explained process that my be slightly incomplete or with minor errors.<br>4: Clearly explained with no/few errors.<br> 5: Impressive effort.| 
|README                                |   3   | 0: Missing or useless in describing project.<br>  1: Misspellings, hard to read font, strange formatting, ugly screenshots, inconsistent text sizes, wall-of-text.<br> 2: Generally pleasing that describes project well, good illustrations, a few minor issues. <br>3: Beautiful and an impressive showcase for the project with good organization, appropriate use of text and illustrations, and helpful references.|


# Capstone III

Capstone III is what you present at the capstone showcase.  For most, it's
a continuation of Capstone II.  Besides making your Capstone II model better,
Capstone III could feature:  
* improvements in deployment (creation of a Docker image)  
* improvements in a user interface (a Flask web application hosted on AWS)  
* more streamlined, better commented, object-oriented, refactored code 
* evidence of test-driven-development: a `tests` directory with a test suite that tests all or some parts of your code  
* scale-up of the project to train on big data in the cloud with a powerful instance  
* comparison of results from a big data tool (e.g. Spark) on a big data dataset compared to a model trained in sklearn on a much smaller dataset  

If you decide to change projects between Capstones II and III, please consider 
this cautionary image describing the project Valley of Despair:
<p align="center">
<img src="https://dscottsmith.files.wordpress.com/2013/05/valleyofdespair.png" width="400"> 
</p> 

If Capstone II worked out for you, there's a good chance you've pushed through 
the "4) Why am I here" stage and got to "5) First win."  If you continued working 
on Capstone II for Capstone III, it would be on the up-and-up to "6) New levels achieved"
and beyond.  If you're starting a new project for Capstone III, you're back to the 
beginning and you've got to navigate the Valley of Despair again!  

If you _still_ want to change projects, you'll need to submit a new project proposal (**if you
aren't changing projects, a Capstone III project proposal isn't required.**)  For your 
Capstone III proposal to be successful, we'll want to see significant progress on
the project already (you've parsed the data, provide EDA, maybe even preliminary results).
You only have about a week to work on it, after all. 


## Capstone III goals

* An MVP+ or MVP++ that demonstrates advanced skill in supervised or unsupervised learning (and maybe both).
* A professional Github containing your project's code, with a Readme that describes your project at an advanced level.  Here are a few examples of impressive final project Readmes:  
  * [Therapist Recommender](https://github.com/camerongridley/TherapistRecommender)
  * [Removing Lines from Uncle Peter's Sailboat Drawings](https://github.com/reiffd7/line_remover_)
  * [The Evolution of Machine Learning](https://github.com/stevenrouk/evolution-of-machine-learning)
* A professional poster or talk describing the project.  This talk or poster is an iterative process with your peers and the instructional staff.

## Capstone III proposal  

This is **not required** if you are expanding on your Capstone II project.  

Please write up a Capstone III proposal and submit it to your instructors for
review.  Please submit a **one to two page PDF** file (no text files, markdowns, or 
Word Documents).

The proposal should:

1) State your question.  What is it that you are curious about?  What are you looking 
for in the data?

2) Demonstrate that you have looked at your data.  What are your columns?  Are they
numerical/catagorical?  How many Nan's are there?  Have you made a couple of plots? 
We only have a week for this capstone. It's very hard to do a good capstone when 
you've only had the real dataset for a couple of days.  This can make it challenging to 
work with a company.  Their timescale is different from the DSI.  "Fast" for them is a 
couple of weeks.  You needed the dataset yesterday.

3) State your MVP.  MVP is your Minimum Viable Product.  What's the minimum that you 
hope to accomplish?  Then, feel free to expand on MVP+, and MVP++. 

4) Show evidence of **remarkable** progess. The project should be much farther along 
than your capstone II was by the time of proposal submittal.  You only have 1 week to 
work on this project before you present to the datascience community.  You need
much more than a good idea and some EDA for your new Capstone III project proposal
to be approved.

## Evaluation  
This capstone should help you get a job!  Your Github's code, Readme, and your
talk/poster should all be ready to land that first job interview.
