## Welcome to Galvanize Denver's 18th Data Science Immersive!

This website is your primary resource for class activities. On this page you'll find information you about the program as a whole as well as links to daily readings, assignments, and lectures. Please make a habit of refreshing and checking it every day, and always make sure you're using the branch for this cohort.

**Do not fork or clone this repo.** Details may change, so **please bookmark this page**.

Please review the documents in the 'notes' directory of this repo. 

#  Weekly overview
The Data Science Immersive (DSI) has 8 instructional weeks, 3 capstone weeks, and the final showcase/career week.  There is a one-week break to rest, review and prepare. During this time instructors will have limited availability.

There are six graded 1 hour assessments on Mondays, plus a readiness assessment at the start of the course. Most instructional weeks end with a group case study on Friday. 

The capstone weeks are reserved for your capstone projects (see below).  Besides having most of each day to work on your capstone, you will also scrum with your peers and participate in mock job interiews. For capstones 1 & 2 you'll present your project to your peers and instructors on Friday afternoon. Capstone 3 is the final graduation project that is presented to the data science community at the end of the course.

To jump to a week of interest, click on the link.

| Week | Date | Topic |
| --- | --- | --- |
| 1 | 6/29 | [Programming for Data Science](#week-1-programming-for-data-science)
| 2 | 7/6 | [Statistics](#week-2-statistics)
| 3 | 7/13 | [Big Data](#week-3-big-data)
| 4 | 7/20 | [Unit 1 Capstone](#week-4-unit-1-capstone)
| 5 | 7/27 | [Supervised Learning and Regression](#week-5-supervised-learning-and-regression)
| 6 | 8/3 | [Nonlinear Supervised Learning](#week-6-nonlinear-supervised-learning)
| 7 | 8/10 | [Solo Week](#solo-week)
| 8 | 8/17 | [NLP and Unsupervised Learning](#week-7-nlp-and-unsupervised-learning)
| 9 | 8/24 | [Unit 2 Capstone](#week-8-unit-2-capstone)
| 10 | 8/31 | [Advanced Topics 1](#week-9-advanced-topics-1)
| 11 | 9/7 | [Advanced Topics 2](#week-10-advanced-topics-2)
| 12 | 9/14 | [Unit 3 Capstone](#week-11-unit-3-capstone)
| 13 | 9/21 | [Showcase](#week-12-showcase)


## Other important links
* [Solutions](https://github.com/GalvanizeDataScience/solutions-den18) for assessments, assignments, and the weekly review will be added to this repository.  If a solution is missing, please bug an instructor!
* [Previous student capstone projects](https://github.com/GalvanizeDataScience/project-proposals/blob/master/past_student_projects.md)  Whether you're looking for capstone ideas or resources to help you with your current capstone, take a look here.  Some of the most exemplary/helpful ones are marked with an asterisk.
* [Lectures](https://github.com/GalvanizeDataScience/lectures/tree/Denver) **Clone this Github repository locally.** Lectures for each day can be found in the lectures repo of the same name.  Checkout the Denver branch.
* [Quick reference](./quick-reference) We've curated online material to provide you "cheatsheets" for important topics in the DSI.  All the guides have been combined into `DSI_quick_ref.pdf` in the `quick-reference` folder, but each of the files is also available individually.  For instance, the `Git.pdf` is likely to come in handy everyday.  The `DSI_Installation_Guide.pdf` is also in this folder if at some point you need to re-install VSCode and Anaconda's distribution of Python.
 
## Capstone Projects
Capstone projects allow you to practice your new datascience skills on projects of your choosing.  They contribute to your Github portfolio and give you specific skills to talk about during job interviews. You will submit capstone proposals to the instructors for approval before the capstone weeks begin. Very often capstone 3 builds on work done on capstone 2, and sometimes even capstone 1.

## Daily Outline
In the weekly tables below, each row represents a day.  
Each row contains information and links:
* __Day__ Day of the Week
* __Readings__ Readings for the day (to be completed the night before).
* __Repos__ The day's exercise(s). 
* __Lectures__ The day's lecture notes and slides

Most Instructional days will follow the same general schedule:

* Assessments, Career-Services Activities, Guest Speakers
* Morning Lecture (~1.5 Hours)
* Morning Lab
* Lunch
* Afternoon Lecture (~1.5 Hours)
* Afternoon Lab 
* End-of-Day Assignment Review and Stand-Down

## Schedule:

<br/>

### Week 1: Programming for Data Science
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 6/29| [Unix Tutorial](http://www.ee.surrey.ac.uk/Teaching/Unix/) <br/> [Unix for Data Science](http://www.gregreda.com/2013/07/15/unix-commands-for-data-science/) <br/> [Unix Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) <br/> [Git Remote](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes) <br/> [Development Workflow](notes/workflow.md) <br/> [Pair Programming](notes/pairing.md) <br/> [Git Quick Reference](quick-reference/Git.pdf) <br/>  | [Readiness Assessment](https://learn-2.galvanize.com/cohorts/1971) <br/> [Unix (Denver)](https://github.com/GalvanizeDataScience/unix) <br/> [Git Intro](https://github.com/GalvanizeDataScience/git-intro) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/unix) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/git-intro) <br/> |
|Tuesday 6/30| [Python code style](https://docs.python-guide.org/writing/style/#general-concepts) <br/> [A Quick Tour of IPython Notebook](https://nbviewer.jupyter.org/github/jvns/pandas-cookbook/blob/master/cookbook/A%20quick%20tour%20of%20IPython%20Notebook.ipynb) (Extra) <br/> [A Taxonomy of Data Science](http://www.dataists.com/2010/09/a-taxonomy-of-data-science/) (Extra) <br/> [Classes and objects](http://www.greenteapress.com/thinkpython/html/thinkpython016.html) <br/>  | [Python Intro](https://github.com/GalvanizeDataScience/python-intro) <br/> [Object-Oriented Programming](https://github.com/GalvanizeDataScience/oop) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/python-intro) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/oop) <br/> |
|Wednesday 7/1| [Linear Algebra Review and Reference](http://cs229.stanford.edu/section/cs229-linalg.pdf) (Reference) <br/> [Linear Algebra for Deep Learning](http://www.deeplearningbook.org/contents/linear_algebra.html) (2.1–2.7) <br/> [Linear Algebra (precourse)](https://learn-2.galvanize.com/cohorts/1984/blocks/16/content_files/units/linear-algebra1/overview.md) <br/> [Numpy Reading](notes/reading_material/numpy_reading.md) <br/>  | [Linear Algebra](https://github.com/GalvanizeDataScience/linear-algebra) <br/> [Numpy](https://github.com/GalvanizeDataScience/numpy) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/linear-algebra) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/numpy) <br/> |
|Thursday 7/2| [10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html) <br/> [Pandas Top 10](http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/) <br/> [EDA with Pandas](http://nbviewer.ipython.org/github/cs109/content/blob/master/labs/lab3/lab3full.ipynb) (Extra) <br/> [Data Wranging with Pandas](http://nbviewer.ipython.org/github/cs109/content/blob/master/lec_04_wrangling.ipynb) (Extra) <br/> [Less is More](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/) <br/> [Matplotlib Tutorial 1](https://www.stat.berkeley.edu/~nelle/teaching/2017-visualization/README.html) <br/> [Matplotlib Tutorial 2](https://matplotlib.org/users/artists.html) <br/>  | [Pandas](https://github.com/GalvanizeDataScience/pandas) <br/> [Graphing in matplotlib](https://github.com/GalvanizeDataScience/matplotlib) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/pandas) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/matplotlib) <br/> |
|Friday 7/3| [What is EDA?](https://www.itl.nist.gov/div898/handbook/eda/section1/eda11.htm) <br/> [Capstone 1 Example: Denver Auto Accidents](https://github.com/johnherr/Traffic-Accidents-in-Denver) <br/> [Capstone 1 Example: Service Provisions by Non-state Actors](https://github.com/gagejane/Terrorism-NonViolent) <br/>  | [Student-led Review](https://github.com/GalvanizeDataScience/weekly-student-led-review) <br/> [Feature Branch Workflow](https://github.com/GalvanizeDataScience/feature-branch-git-workflow) <br/> [Pandas EDA Case study](https://github.com/GalvanizeDataScience/pandas-eda-case-study) <br/> Holiday (Independence Day) <br/>  | |
<br/>

### Week 2: Statistics
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 7/6| [Review of Probability Theory](http://cs229.stanford.edu/section/cs229-prob.pdf) <br/> [Basic Probability](https://seeing-theory.brown.edu/basic-probability/index.html) <br/> [Binomial Distribution and Test](https://www.youtube.com/watch?v=J8jNoF-K8E8) <br/>  | [Assessment 1](https://learn-2.galvanize.com/cohorts/1971) <br/> [Probability Distributions](https://github.com/GalvanizeDataScience/probability-distributions) <br/> [Binomial Tests](https://github.com/GalvanizeDataScience/binomial-tests) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/probability-distributions) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/binomial-tests) <br/> |
|Tuesday 7/7| [Bootstrapping Intro](https://www.youtube.com/watch?v=_nhgHjdLE-I) <br/> [Frequentist Inference](https://seeing-theory.brown.edu/frequentist-inference/index.html) <br/> [Law of Large Numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers) <br/>  | [Sampling Distributions](https://github.com/GalvanizeDataScience/sampling-distributions) <br/> [The Law of Large Numbers](https://github.com/GalvanizeDataScience/law-of-large-numbers) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/sampling-distributions) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/law-of-large-numbers) <br/> |
|Wednesday 7/8| [The Central Limit Theorem](https://www.youtube.com/watch?v=YAlJCEDH2uY) <br/> [Central Limit Theorem](https://www.khanacademy.org/math/ap-statistics/sampling-distribution-ap/sampling-distribution-mean/v/central-limit-theorem) <br/> [MLE](https://www.youtube.com/watch?v=I_dhPETvll8) <br/> [Maximum Likelihood](https://www.youtube.com/watch?v=XepXtl9YKwc) <br/> [Maximum Likelihood for Normal Distribution](https://www.youtube.com/watch?v=Dn6b9fCIUpM) (Optional) <br/>  | [The Central Limit Theorem](https://github.com/GalvanizeDataScience/central-limit-theorem) <br/> [Maximum-Likelihood Estimation](https://github.com/GalvanizeDataScience/maximum-likelihood) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/central-limit-theorem) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/maximum-likelihood) <br/> |
|Thursday 7/9| [z-test VS t-test](https://www.youtube.com/watch?v=5ABpqVSx33I) <br/> [Hypothesis Testing](https://www.youtube.com/watch?v=-FtlH4svqx4) <br/> [Power Analysis](https://www.youtube.com/watch?v=lHI5oEgNkrk) <br/>  | [Hypothesis Testing](https://github.com/GalvanizeDataScience/hypothesis-testing) <br/> [Statistical Power](https://github.com/GalvanizeDataScience/statistical-power) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/hypothesis-testing) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/statistical-power) <br/> |
|Friday 7/10| [Bayesian Intuition](https://www.youtube.com/watch?v=HZGCoVF3YvM) <br/> [Introduction to Bayesian statistics part I](https://mathcs.clarku.edu/~djoyce/ma218/bayes1.pdf) <br/> [Introduction to Bayesian statistics part II](https://mathcs.clarku.edu/~djoyce/ma218/bayes2.pdf) <br/>  | [Student-led Review](https://github.com/GalvanizeDataScience/weekly-student-led-review) <br/> [Intro to Bayesian Statistics](https://github.com/GalvanizeDataScience/bayes-intro) <br/> [Baysian Hypothesis Testing](https://github.com/GalvanizeDataScience/bayes-testing) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/bayes-intro) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/bayes-testing) <br/> |
<br/>

### Week 3: Big Data
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 7/13| [Getting Started with Docker](https://docs.docker.com/get-started/) (wait to install until class) <br/> [AWS setup](https://github.com/GalvanizeDataScience/unix/blob/master/setup_aws.md) <br/> [Getting Started with AWS](https://aws.amazon.com/start-now/) <br/> [About AWS](https://aws.amazon.com/about-aws/) <br/>  | [Assessment 2](https://learn-2.galvanize.com/cohorts/1971) <br/> [Docker](https://github.com/GalvanizeDataScience/docker) <br/> [AWS (Denver)](https://github.com/GalvanizeDataScience/aws) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/docker) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/aws) <br/> |
|Tuesday 7/14| [SQL Zoo](http://sqlzoo.net/wiki/Main_Page) (tutorial 1–9) <br/> [Visual Explanation of Joins](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) <br/>  | [SQL](https://github.com/GalvanizeDataScience/sql) <br/> [SQL from Python](https://github.com/GalvanizeDataScience/sql-python) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/sql) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/sql-python) <br/> |
|Wednesday 7/15| [Introduction to Algorithms](http://ressources.unisciel.fr/algoprog/s00aaroot/aa00module1/res/%5BCormen-AL2011%5DIntroduction_To_Algorithms-A3.pdf) (Chapter 2 pg 16–42) <br/> [Little book of MongoDB](http://openmymind.net/mongodb.pdf) <br/> [Basic Web Scaping](https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe) <br/> [Web Scraping Using BeautifulSoup](https://www.dataquest.io/blog/web-scraping-tutorial-python/) <br/>  | [Algorithmic Complexity](https://github.com/GalvanizeDataScience/algorithmic-complexity) <br/> [Web Scraping](https://github.com/GalvanizeDataScience/web-scraping) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/algorithmic-complexity) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/web-scraping) <br/> |
|Thursday 7/16| [Capstone 1 proposals due 8:30 am](./notes/capstones.md)<br/>[Learning Spark](https://drive.google.com/file/d/0B1cm3fV8cnJwc2ZnMFJmT2RLOXM/view?usp=sharing) (pg 1–22) <br/> [Learning Spark](https://drive.google.com/file/d/0B1cm3fV8cnJwc2ZnMFJmT2RLOXM/view?usp=sharing) (ch 11; Optional) <br/>  | [Spark](https://github.com/GalvanizeDataScience/spark-rdds) <br/> [SQL and Dataframes in Spark](https://github.com/GalvanizeDataScience/spark-dfs) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/spark-rdds) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/spark-dfs) <br/> |
|Friday 7/17|  | [Student-led Review](https://github.com/GalvanizeDataScience/weekly-student-led-review) <br/> [Spark Case Study](https://github.com/GalvanizeDataScience/spark-case-study) <br/>  | |
<br/>

### Week 4: Unit 1 Capstone
[Hourly Schedule and Mock Interview Sign-up for Week](https://docs.google.com/spreadsheets/d/1U1ixWgdEuJbcVQbnbQpDtQ4Or_5SWhU_Zd28ojZ6WZk/edit?usp=sharing)  
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 7/20| [Capstone guide](./notes/capstones.md) <br/>  | [Assessment 3](https://learn-2.galvanize.com/cohorts/1971) <br/> Begin Capstone 1 <br/> [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
|Tuesday 7/21| [Capstone guide](./notes/capstones.md) <br/>  | [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
|Wednesday 7/22| [Capstone guide](./notes/capstones.md) <br/>  | [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
|Thursday 7/23| [Capstone guide](./notes/capstones.md) <br/>  | [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
|Friday 7/24|  | Presentation in afternoon <br/>  | |
<br/>

### Week 5: Supervised Learning and Regression
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 7/27| [K-Nearest Neighbors](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (pg 39–42,104–109) <br/> [Classifying with k-Nearest Neighbors](https://drive.google.com/file/d/0B1cm3fV8cnJwcUNWWnFaRWgwTDA/view?usp=sharing) (Section 2.1) <br/> [KNN (Learn)](https://learn-2.galvanize.com/cohorts/1971/blocks/244/content_files/knn/README.md) <br/> [The Bias-Variance Trade-Off](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (2.2.2) <br/> [Cross Validation](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (5–5.1.4) <br/> [Bias-Variance (Learn)](https://learn-2.galvanize.com/cohorts/1971/blocks/244/content_files/bias-variance/readme.md) <br/> [Cross Validation (Learn)](https://learn-2.galvanize.com/cohorts/1971/blocks/244/content_files/cross-validation/readme.md) <br/>  | [K-Nearest Neighbors](https://github.com/GalvanizeDataScience/knn) <br/> [Cross Validation](https://github.com/GalvanizeDataScience/cross-validation) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/knn) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/cross-validation) <br/> |
|Tuesday 7/28| [Linear Regression](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (3.3–3.4) <br/>  | [Intro to Linear Regression](https://github.com/GalvanizeDataScience/linear-regression-eda) <br/> [Predictive Linear Regression](https://github.com/GalvanizeDataScience/predictive-linear-regression) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/linear-regression-eda) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/predictive-linear-regression) <br/> |
|Wednesday 7/29| [Regularization](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (6-6.1 pg 203–214,Optional) <br/> [Shrinkage Methods](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (6.2 pg 214–228) <br/> [Regularization (Learn)](https://learn-2.galvanize.com/cohorts/1971/blocks/244/content_files/regularized-regression/readme.md) <br/> [Logistic Regression](https://drive.google.com/file/d/0B1cm3fV8cnJwcUNWWnFaRWgwTDA/view?usp=sharing) (Chapter 5 pg 83–90) <br/> [Logistic Regression](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (pg 127–137) <br/>  | [Regularized Regression](https://github.com/GalvanizeDataScience/regularized-regression) <br/> [Logistic Regression](https://github.com/GalvanizeDataScience/logistic-regression) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/regularized-regression) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/logistic-regression) <br/> |
|Thursday 7/30| [Andrew Ng notes](http://cs229.stanford.edu/notes/cs229-notes1.pdf) (1–7,16–19) <br/>  | [Gradient Descent](https://github.com/GalvanizeDataScience/gradient-descent) <br/> [Decision Rules](https://github.com/GalvanizeDataScience/decision-rules) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/gradient-descent) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/decision-rules) <br/> |
|Friday 7/31|  | [Student-led Review](https://github.com/GalvanizeDataScience/weekly-student-led-review) <br/> [Regression Case Study](https://github.com/GalvanizeDataScience/regression-case-study) <br/>  | |
<br/>

### Week 6: Nonlinear Supervised Learning
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 8/3| [Introduction to Time Series Analysis](https://algorithmia.com/blog/introduction-to-time-series) <br/> [Forecasting: principles and practice](https://otexts.com/fpp2/) (ch 1,2,& 6–8) <br/> [Time Series Analysis and its Applications](https://www.stat.pitt.edu/stoffer/tsa4/tsa4.pdf) (ch 1–3) <br/> [ARIMA Models in Python](http://conference.scipy.org/proceedings/scipy2011/pdfs/statsmodels.pdf) <br/> [Recursion](https://runestone.academy/runestone/books/published/pythonds/Recursion/toctree.html) <br/> [Recursion](https://github.com/GalvanizeDataScience/welcome/tree/master/readings/recursion) <br/> [Visual Introduction to Decision Trees](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) <br/> [Decision Trees](https://drive.google.com/file/d/0B1cm3fV8cnJwcUNWWnFaRWgwTDA/view?usp=sharing) (3–3.1 pg 37–48) <br/> [Decision Trees (Learn)](https://learn-2.galvanize.com/cohorts/1971/blocks/244/content_files/dec_tree/README.md) <br/>  | [Assessment 4](https://learn-2.galvanize.com/cohorts/1971) <br/> [Time Series](https://github.com/GalvanizeDataScience/time-series) <br/> [Decision Trees](https://github.com/GalvanizeDataScience/decision-trees) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/time-series) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/decision-trees) <br/> |
|Tuesday 8/4| [Ensembles](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (8.2 pg 316–321) <br/>  | [Random Forests - Implementation](https://github.com/GalvanizeDataScience/random-forests-implementation) <br/> [Random Forests - Application](https://github.com/GalvanizeDataScience/random-forests-application) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/random-forests-implementation) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/random-forests-application) <br/> |
|Wednesday 8/5| [Boosting](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (8.2.3 pg 321–323) <br/> [Boosting Methods](https://web.stanford.edu/~hastie/ElemStatLearn/download.html) (10–10.6 pg 337–350,Optional) <br/>  | [Boosting - Implementation](https://github.com/GalvanizeDataScience/boosting-implementation) <br/> [Gradient Boosted Regressors](https://github.com/GalvanizeDataScience/gradient-boosted-regression) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/boosting-implementation) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/gradient-boosted-regression) <br/> |
|Thursday 8/6| [Neural Networks Demystified](https://www.youtube.com/watch?v=bxe2T-V8XRs) (Parts 1–7) <br/> [What is a Neural Network](https://www.youtube.com/watch?v=aircAruvnKk) (Parts 1 and 2) <br/> [Neural networks and deep learning with Torch](https://www.cs.ox.ac.uk/people/nando.defreitas/machinelearning/) (Lecture 9) <br/> [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) <br/> [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) <br/>  | [Multi-Layer Perceptrons](https://github.com/GalvanizeDataScience/perceptrons) <br/> [Recurrent Neural Networks](https://github.com/GalvanizeDataScience/recurrent-neural-nets) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/perceptrons) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/recurrent-neural-nets) <br/> |
|Friday 8/7|  | [Student-led Review](https://github.com/GalvanizeDataScience/weekly-student-led-review) <br/> [Supervised Learning Case Study](https://github.com/GalvanizeDataScience/supervised-learning-case-study) <br/>  | |
<br/>

### Solo Week
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 8/10|  | Relax and review and work on Capstone 2 <br/>  | |
|Tuesday 8/11|  |  | |
|Wednesday 8/12|  |  | |
|Thursday 8/13|  |  | |
|Friday 8/14|  |  | |
<br/>

### Week 7: NLP and Unsupervised Learning
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 8/17| [Digital Image Processing Basics](https://www.geeksforgeeks.org/digital-image-processing-basics/) <br/> [Convolutional Neural Networks](https://cs231n.github.io/convolutional-networks/) <br/> [Intuitive Explanation of CNNs](https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/) <br/>  | [Assessment 5](https://learn-2.galvanize.com/cohorts/1971) <br/> [Image Processing](https://github.com/GalvanizeDataScience/image-processing) <br/> [Convulutional Neural Networks](https://github.com/GalvanizeDataScience/convolutional-neural-nets) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/image-processing) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/convolutional-neural-nets) <br/> |
|Tuesday 8/18| [Text Feature Extraction I](http://blog.christianperone.com/?p=1589) <br/> [Text Feature Extraction II](http://blog.christianperone.com/?p=1747) <br/> [Text Feature Extraction III](http://blog.christianperone.com/?p=2497) <br/> [NLP](http://www.datascienceassn.org/sites/default/files/Natural%20Language%20Processing%20with%20Python.pdf) (Sections 1.1–1.7) <br/> [NLP in Python](http://www.datascienceassn.org/sites/default/files/Natural%20Language%20Processing%20with%20Python.pdf) (3.6 pg 107–108) <br/> [Scalability of Semantic Analysis in NLP](https://radimrehurek.com/phd_rehurek.pdf) (Sections 1.1–1.7) <br/>  | [Natural Language Processing](https://github.com/GalvanizeDataScience/nlp) <br/> [Text Classification and Naive Bayes](https://github.com/GalvanizeDataScience/text-classification) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/nlp) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/text-classification) <br/> |
|Wednesday 8/19| [Clustering](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (pg 385–400) <br/> [PCA](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf) (ch 10.2 pg 374–385) <br/> [PCA Explained Visually](https://setosa.io/ev/principal-component-analysis/) <br/>  | [Clustering](https://github.com/GalvanizeDataScience/clustering) <br/> [Principle-Component Analysis](https://github.com/GalvanizeDataScience/pca) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/clustering) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/pca) <br/> |
|Thursday 8/20| [SVD](http://infolab.stanford.edu/~ullman/mmds/book.pdf) (ch 11) <br/> [The why and how of NMF](https://blog.acolyer.org/2019/02/18/the-why-and-how-of-nonnegative-matrix-factorization/) <br/> [NMF: A Simple Tutorial in Python](http://www.quuxlabs.com/blog/2010/09/matrix-factorization-a-simple-tutorial-and-implementation-in-python/) <br/>  | [Singluar Value Decomposition](https://github.com/GalvanizeDataScience/svd) <br/> [Topic Modeling with NMF](https://github.com/GalvanizeDataScience/topic-modeling) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/svd) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/topic-modeling) <br/> |
|Friday 8/21|  | [Student-led Review](https://github.com/GalvanizeDataScience/weekly-student-led-review) <br/> [NLP Case Study](https://github.com/GalvanizeDataScience/nlp-case-study) <br/>  | |
<br/>

### Week 8: Unit 2 Capstone
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 8/24| [Capstone guide](./notes/capstones.md) <br/>  | [Assessment 6](https://learn-2.galvanize.com/cohorts/1971) <br/> Begin Capstone 2 <br/> [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
|Tuesday 8/25| [Capstone guide](./notes/capstones.md) <br/>  | [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
|Wednesday 8/26| [Capstone guide](./notes/capstones.md) <br/>  | [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
|Thursday 8/27| [Capstone guide](./notes/capstones.md) <br/>  | [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
|Friday 8/28|  | Presentation in afternoon <br/>  | |
<br/>

### Week 9: Advanced Topics 1
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 8/31| [Flask](http://flask.pocoo.org/) <br/> [Flask Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) <br/> [HTTP Methods](http://www.w3schools.com/tags/ref_httpmethods.asp) <br/> [Social Network Analysis](http://www.asecib.ase.ro/mps/Social%20Network%20Analysis%20for%20Startups%20[2011].pdf) (ch 2 pg 19–38) <br/> [Graphs](http://infolab.stanford.edu/~ullman/mmds/book.pdf) (ch 10.1–10.2 pg 343–356) <br/>  | [Building Data Products with Flask](https://github.com/GalvanizeDataScience/flask) <br/> [Introduction to Graphs](https://github.com/GalvanizeDataScience/graphs-searching) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/flask) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/graphs-searching) <br/> |
|Tuesday 9/1| [Guide to LDA](https://medium.com/@lettier/how-does-lda-work-ill-explain-using-emoji-108abf40fa7d) <br/>  | [Time Series and ARIMA](https://github.com/GalvanizeDataScience/time-series-arima) <br/> [Latent Dirichlet Allocation](https://github.com/GalvanizeDataScience/latent-dirichlet-allocation) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/time-series-arima) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/latent-dirichlet-allocation) <br/> |
|Wednesday 9/2| [Content-Based Recommenders](http://infolab.stanford.edu/~ullman/mmds/book.pdf) (ch 9.1–9.2 pg 307–320) <br/> [Collaborative filtering](http://infolab.stanford.edu/~ullman/mmds/book.pdf) (ch 9.3 pg 320–327) <br/> [Collaborative filtering–based recommendation engines](https://drive.google.com/file/d/0B1cm3fV8cnJwcUNWWnFaRWgwTDA/view?usp=sharing) (14.4-14.5 pg 286–295) <br/>  | [Content-Based Recommenders](https://github.com/GalvanizeDataScience/content-based-recommenders) <br/> [Similarity-Based Recommenders](https://github.com/GalvanizeDataScience/similarity-based-recommenders) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/content-based-recommenders) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/similarity-based-recommenders) <br/> |
|Thursday 9/3| [Dimensionality Reductions](http://infolab.stanford.edu/~ullman/mmds/book.pdf) (ch 9.4–9.5 pg 328–340)) <br/> [Matrix Factorization Techniques](https://datajobs.com/data-science-repo/Recommender-Systems-%5BNetflix%5D.pdf) <br/>  | [Factorization Recommenders](https://github.com/GalvanizeDataScience/factorization-recommenders) <br/> [Recommender Case Study](https://github.com/GalvanizeDataScience/recommender-case-study) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/factorization-recommenders) <br/> |
|Friday 9/4|  | [Recommender Case Study](https://github.com/GalvanizeDataScience/recommender-case-study) <br/>  | |
<br/>

### Week 10: Advanced Topics 2
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 9/7|  | Holiday (Labor Day) <br/>  | |
|Tuesday 9/8| [Autoencoders](http://ufldl.stanford.edu/tutorial/unsupervised/Autoencoders/) <br/> [Gentle Introduction to Transfer Learning](https://machinelearningmastery.com/transfer-learning-for-deep-learning/) <br/> [Transfer Learning](https://machinelearningmastery.com/transfer-learning-for-deep-learning/) <br/>  | [Autoencoders](https://github.com/GalvanizeDataScience/autoencoders) <br/> [Transfer Learning](https://github.com/GalvanizeDataScience/transfer-learning) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/autoencoders) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/transfer-learning) <br/> |
|Wednesday 9/9| [Multi-armed bandit](http://stevehanov.ca/blog/index.php?id=132) <br/>  | [The Multi-Armed Bandit Problem](https://github.com/GalvanizeDataScience/multi-armed-bandit) <br/> [Reinforcement Learning](https://github.com/GalvanizeDataScience/reinforcement-learning-with-nn) <br/>  | [AM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/multi-armed-bandit) <br/> [PM](https://github.com/GalvanizeDataScience/lectures/tree/Denver/reinforcement-learning-with-nn) <br/> |
|Thursday 9/10|  | [Fraud-Detection Case Study](https://github.com/GalvanizeDataScience/fraud-detection-case-study) <br/>  | |
|Friday 9/11|  | [Fraud-Detection Case Study](https://github.com/GalvanizeDataScience/fraud-detection-case-study) <br/>  | |
<br/>

### Week 11: Unit 3 Capstone
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 9/14| [Capstone guide](./notes/capstones.md) <br/>  | Begin Capstone 3 <br/> [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
|Tuesday 9/15| [Capstone guide](./notes/capstones.md) <br/>  | [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
|Wednesday 9/16| [Capstone guide](./notes/capstones.md) <br/>  | [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
|Thursday 9/17| [Capstone guide](./notes/capstones.md) <br/>  | [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
|Friday 9/18| [Capstone guide](./notes/capstones.md) <br/>  | [Mock Interviews](https://github.com/GalvanizeDataScience/mock-interview-questions) <br/>  | |
<br/>

### Week 12: Showcase
| Day | Readings | Repos | Lecture Materials |
|:--:|:-----------------------------------------|:--:|:--:|
|Monday 9/21|  |  | |
|Tuesday 9/22|  |  | |
|Wednesday 9/23|  |  | |
|Thursday 9/24|  | Demo Day <br/>  | |
|Friday 9/25|  | Graduation <br/>  | |


## Textbooks
We will focus on a few canonical texts for the class and readings will be assigned from them. If they are not in a physical form in our library, they are located in digital form on the Time Capsule or the Internet.
* [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf): The book we use for the majority of machine learning readings.
* [Elements of Statistical Learning](https://web.stanford.edu/~hastie/Papers/ESLII.pdf): If ISLR doesn't have enough detail for you, then look in ESL by the same authors.
* [Machine Learning In Action](https://drive.google.com/file/d/0B1cm3fV8cnJwcUNWWnFaRWgwTDA/view?usp=sharing)
* [Deep Learning Book](http://www.deeplearningbook.org/) Intended as a deep learning text, its introductory treatment of probability, linear algebra, and mathematics is excellent.
* [Forecasting: Principles and Practice](https://otexts.com/fpp2/) We introduce forecasing, but it's a specialized discipline.  This free text expands on the subject.

### Supplementary
* [Doing Data Science](http://www.amazon.com/Doing-Data-Science-Straight-Frontline/dp/1449358659): One of the best treatments of the field with plenty of case studies.
* [Python for Data Analysis](http://shop.oreilly.com/product/0636920023784.do): Some of the `pandas` methods have changed (always reference `pandas` [online documentation](http://pandas.pydata.org/)) but a solid book on data analysis in Python.
* [Practical Data Science with R](http://www.manning.com/zumel/): through we will not use R, this is a stellar book and we will use it for its content/theory

## Video Series
* [Youtube lectures by Hastie and Tibshirani on Statistical Learning](https://www.youtube.com/watch?v=5N9V07EIfIg&list=PLOg0ngHtcqbPTlZzRHA2ocQZqB1D_qZ5V)
* [StatsQuest](https://www.youtube.com/user/joshstarmer) - A goofy but clear explanation of statistics and machine learning concepts.
* [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) Self-described as combination math & entertainment, this website has explanations for many machine learning topics.

## Getting Help
* [Data Science Stack Exchange](http://datascience.stackexchange.com/)
* [Stats Stack Exchange](http://stats.stackexchange.com/)
* [MetaOptimize: ML and Datascience forum](http://metaoptimize.com/qa)

## References

### Machine Learning
* [Machine Learning in Action](http://www.manning.com/pharrington/)
* [Programming Collective Intelligence](http://www.amazon.com/Programming-Collective-Intelligence-Building-Applications/dp/0596529325)
* [Machine Learning for Hackers](http://shop.oreilly.com/product/0636920018483.do)
* [An Introduction to Machine Learning](http://alex.smola.org/drafts/thebook.pdf)

### Statistics
* [Probabilistic Programming and Bayesian Methods for Hackers](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/)
* [Think Stats](http://www.greenteapress.com/thinkstats/)
* [Think Bayes](http://www.greenteapress.com/thinkbayes/)
* [All of Statistics](http://www.stat.cmu.edu/~larry/all-of-statistics/)
* [Mostly Harmless Econometrics](http://www.amazon.com/Mostly-Harmless-Econometrics-Empiricists-Companion/dp/0691120358)

### Computer Science/Programming
* [Think Python](http://www.greenteapress.com/thinkpython/thinkpython.html)
* [Algorithms (Papadimitriou)](http://www.cs.berkeley.edu/~vazirani/algorithms)
* [Think Complexity: Analysis of Algorithms](http://www.greenteapress.com/compmod/html/thinkcomplexity004.html)

### Numpy/Scipy
* [Official Numpy Tutorial](http://wiki.scipy.org/Tentative_NumPy_Tutorial)
* [scipy Lectures](https://scipy-lectures.github.io/intro/numpy/index.html)
* [Crash Course in Python for Scientist](http://nbviewer.ipython.org/gist/rpmuller/5920182)
* [Scientific Python Lectures](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-2-Numpy.ipynb)
* [Numpy Broadcasting](http://wiki.scipy.org/EricsBroadcastingDoc)
* [Python Bootcamp Lectures](http://nbviewer.ipython.org/github/profjsb/python-bootcamp/blob/master/Lectures/05_NumpyMatplotlib/IntroNumPy.ipynb)
* [scipy Lectures](https://scipy-lectures.github.io)

### SQL
* [http://sqlfiddle.com/](http://sqlfiddle.com/)
* [http://use-the-index-luke.com/](http://use-the-index-luke.com/)
* [http://missqlcommand.com/](http://missqlcommand.com/)
* [http://sql.learncodethehardway.org/book/](http://sql.learncodethehardway.org/book/)
* [SQL School](http://sqlschool.modeanalytics.com/)

### scikit-learn
* [Introduction to Machine Learning with sklearn](http://researchcomputing.github.io/meetup_spring_2014/python/sklearn.html)
* [scikit-learn workshop](https://github.com/jakevdp/sklearn_pycon2014)
* [Machine Learning Tutorial](https://github.com/amueller/tutorial_ml_gkbionics)
* [Introduction to scikit-learn](http://nbviewer.ipython.org/github/tdhopper/Research-Triangle-Analysts--Intro-to-scikit-learn/blob/master/Intro%20to%20Scikit-Learn.ipynb)
* [Data analysis with scikit-learn](http://sebastianraschka.com/Articles/2014_scikit_dataprocessing.html)
* [Advanced Machine Learning with scikit-learn](https://us.pycon.org/2013/community/tutorials/23/)

### Extra
* [University of Colorado Computational Science workshops](http://researchcomputing.github.io/meetup_spring_2014/)
* [Networkx tutorial](http://snap.stanford.edu/class/cs224w-2012/nx_tutorial.pdf)


