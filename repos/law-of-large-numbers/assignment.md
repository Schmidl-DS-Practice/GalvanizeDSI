# Law of Large Numbers

## Introduction

![100 Sample Mean Paths](images/100-paths.png)

In this assignment we will do some investigation into the law of large numbers.  This will give us a nice chance to practice using scipy to generate sequences of random numbers from various distributions, and use matplotlib to display the results of our investigations.  These two tools will be with us for the rest of the course, so it's a good idea to spend a bit of time using them in a comfortable scenario.

#### The Law of Large Numbers

Recall that the law of large numbers is our first example of a mathematical link between a population and a sample from that population.  It (approximately) states that in large samples, the mean of the sample is close to the expected value of the population from which the sample was drawn.

![Law of Large Numbers Statements](images/law-of-large-numbers.gif)

Let's play with this idea with different populations.

## Basic

### Part 1: Coin Flips

1\. To begin, setup the following imports in your python file or notebook:

```python
import numpy as np
from scipy import stats

%matplotlib inline
import matplotlib.pyplot as plt
```

Let's validate that the law of large numbers holds for coin flips and dice, which is the original context where [Gerolamo Cardano](https://en.wikipedia.org/wiki/Gerolamo_Cardano) discovered the law.

Since the results of coin flips are *not* numeric, we will need to make some convention to encode heads and tails as numeric values.  The traditional choice is `HEADS => 1, TAILS => 0`.

We can then flip a fair coin ten times using `scipy.stats` (which we imported under the name `stats`):

```python
stats.binom(n=1, p=0.5).rvs(10)
```

By a **fair** coin, we mean a coin with equal chance of landing heads or tails.  Below, we will refer to the probability of a coin landing heads as the **fairness** of the coin.

1\. Write a coin flipping function which flips *any* coin (may be unfair) a specified number of times.  Your function signature should look like this:

```python
def flip_coin(n_flips, p=0.5):
    # This part is your job.
```

2\. Flip a fair coin 1000 times with your function.  What will the sample average of these flips be and why?  Use `np.mean` to check.

3\. Flip an **unfair** coin 1000 times.  What will the sample average be now?  How would you expect the answer to change depending on how extreme the unfairness is?  Use `np.mean` to check your result.

4\. Now let's see how this all depends on the size of the sample.  Create a list with a range of sample sizes, starting at 10, and counting up to 1000 in increments of 10 (`list(range(...))` can be used for this).  Now, for each of these sample sizes, repeat the experiments above.  How does the accuracy of the results depend on the sample size?

5\. You're probably feeling like looking at a list of one-hundred numbers is not so illuminating, so *plot them*!  Make a line plot where the x-axis shows the sample size, and the y-axis show the sample mean.  Also include a horizontal line for the *population* value of the expectation.

6\. Since we are studying a random quantity, it's a good idea to try any experiment *multiple times* and look for patterns not just within one experiment, but amongst the different experiments.Run the above experiment 100 times, and plot all 100 resulting paths on the same axis.  

You will probably want to write a function that makes *one* path of sample means:

```python
def make_sample_mean_path(begin, end, step, p=0.5):
    # This part is up to you
```

And then use this inside a for loop to make the plots.

Describe the pattern that the paths make as a whole.  What do you think causes this pattern?

7\. Finally, let's explore what happens when we change the fairness of the coin.  Use subplots to draw the same picture as the above, but for different values of the coin fairness (I suggest 0.1, 0.25, 0.5, 0.75 and 0.9).  This may take a few seconds to run!

8\. You should notice that the width of the bands is greater for fair coins compared to very unfair coins.  This makes sense, for a fair coin the result of the flips is maximally inconsistent, where very unfair coins tend to give the same result often.

We can measure this with the concept of *variance* or *standard deviation* as follows.

Set up a grid of fairness values for your coins:

```python
fairnesses = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
```

For each value of fairness, flip a coin of that fairness 100 times, and then calculate the sample mean of the result (as we have been doing).  But now take an extra step: repeat this process 100 times, getting 100 sample means for each value of the coin fairness.  Take the variance of *these* sample means.  Plot the results vs the fairness of the coin.

## Advanced
### Part 2: Poisson Draws

The miracle of the law of large numbers is that it applies to samples from *any* population.  Let's try seeing how things work when drawing from a *Poisson* distribution.

**A Reminder:** The **Poisson** distribution is used to model *counts* of events that happen at a fixed rate over a fixed time period.  So, for example, the number of times I observe a chunk of uranium emit a radioactive particle in one minute is Poisson distributed.  The **rate** is the only parameter of the Poisson distribution, and it is often notated as $\lambda$.  The probability mass function of the Poisson distribution is:

![Poisson Probability Mass Function](images/poisson-pmf.gif)

1\. Repeat all your above work on the coin flip distribution for the Poisson distribution.  You'll want to start with a function like this, which is analogous to our `flip_coin` function from before:

```python
def sample_poisson(sample_size, lam=1.0):
    return stats.poisson(lam).rvs(sample_size)
```

## Extra Credit
### Part 3: A Mixture Distribution

We will finish our experiments with the concept of a **mixture distribution**.

Mixture distributions are useful when we suspect that a population we are studying is made up of several different subpopulations.  For example, at least approximately, the human population is made up of males and females, and this is reflected in the distribution of biological or social statistics.

Drawing from a mixture distribution is a two step process:
  
  - First (randomly) select one of the subpopulations to draw from.
  - Draw a datum from that subpopulation.
  
For example, to draw a random human height, we would first need a random human.  We can envision this as first choosing either "male" or "female" at random (though **not equally likely**, randomly **does not mean** equally likely), and then measure the height of a randomly chosen human from the chosen subpopulation.

![Schematic of Drawing from a Mixture Distribution](images/draw-from-mixture.png)

Notice that drawing from a (two subpopulation) mixture requires two pieces of information:

  - The probabilities of drawing from each subpopulation.
  - The distribution of the two subpopulations.
  
In the above example, since there are more male humans than female humans, the probability of choosing the male subpopulation must be greater than the probability of drawing from the female subpopulation (the true weights are approximately 107/207 to 100/207).

In this assignment, we will sample from a mixture of two Poissons, and verify that the law of large numbers holds for this mixture distribution (remember, it should work for **any** distribution).

1\. Write a function called `sample_poisson_mixture` that samples from a mixture of two Poisson distributions.  You will need to include as arguments the lambda parameters of the two Poissons, and the probability of sampling from one Poisson over the other:

```python
def sample_poisson_mixture(sample_size, lam1, lam2, p=0.5):
    # It's up to you.
```

2\. Draw a large sample from a mixture of Poissons with very different lambda parameters (5 and 20 work well).  Draw a histogram of this sample, what do you see?  Can you explain the geometric features of this histogram.

3\. Make a few subplots that show what happens as the mixture parameter `p` varies.  Before running your code, try to sketch out an answer for what you think the histograms will look like.  It's always good to try to guess an answer before you know the truth, if you're incorrect, you should analyse where your reasoning when wrong.

. Calculate the true expected value of a mixture of two Poissons.  This is a more subtle calculation than you may be used to.  You will need to use the [Law of Total Expectation](https://en.wikipedia.org/wiki/Law_of_total_expectation).  

Hint: Our case is covered by the second formula in the preamble to the above wikipedia article.  To apply it, partition all the possibilities according to whether we selected the first or second subpopulation.  In the notation of the wikipeda article:

```
A_1 = We draw from the first Poisson Subpopulation
A_2 = We draw from the second Poisson subpopulation
```

4\. Encode your calculation from the previous exercise into a python function:

```python
def poisson_mixture_expectation(lam1=5.0, lam2=20.0, p=0.5):
    # You can do it!
```

5\. Repeat your work for the coin flip and Poisson distributions for the Poisson mixture with mixture parameter 0.5.  Verify that this is consistent with your calculation of the population expectation (i.e. the calculation you used the law of total expectation for).

6\. Vary the mixture parameter `p` and make multiple subplots showing how this affects the sample mean paths.  Don't forget to indicate the population expectation somehow (a horizontal line works well).
