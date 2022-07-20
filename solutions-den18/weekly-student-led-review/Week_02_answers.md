## Week 2 Review Answers

1) What distribution would you use in the following cases:  
  * What is the probability that the mean volume of 50 bottles is less than 500 ml?   
  Normal - assume mean is normally distributed and see where 500 ml appears in the sampling mean.
  * Deciding to go for a run or not. 
  Bernoulli - a single yes/no trial with probability p_run
  * Determining how many days pass before you finally decide to go for a run.  
  Geometric - assuming any given day there is an equal chance of going for a run (p_run), the number of trials before a success.
  * Determining how likely it is that you go for 10 runs in a month.  
  Binomial - with same assumption as above, the number of success in a certain number of trials
  * Calculating which day of the month you buy new shoes.  
  Uniform
  * Assuming you run at a 9 minute mile avg pace, determining how likely it is that you pass the 3 mile mark in a race in 25 minutes?  
  Exponential - given a certain average rate (speed), figuring out the probability something will occur at a specific time.

2) What is the central limit theorem?  
  
  The central limit theorem (CLT) states that the arithmetic mean of a sufficiently
  large number of iterates of independent random variables, each with a well-defined
  (finite) expected value and finite variance, will be approximately normally 
  distributed, regardless of the underlying distribution.

3) How would you go about implementing a bootstrap, and why would you do it?  
  
  Take the sample that you have and sample from it with replacement to make many
  alternative samples.  Then calculate whatever parameter you want from each sample,
  and then build a confidence interval from those results by sorting them from low to high and discard the bottom and top X%.


4) Wikipedia provides a [list of numbers with cultural and practical signifigance:](https://en.wikipedia.org/wiki/List_of_numbers)  
    3, significant in Christianity as the Trinity. Also considered significant in Hinduism (Trimurti, Tridevi). Holds significance in a number of ancient mythologies.  
    4, considered an "unlucky number" in modern China, Japan and Korea due to its audible similarity to the word "Death."  
    5, number of fingers or toes for almost all amphibians, reptiles and mammals  
    7, considered a "lucky" number in Western cultures.  
    8, considered a "lucky" number in Chinese culture, also the number of bits in a byte.    
    10, the number base for most modern counting systems.  
    12, the number base for some ancient counting systems and the basis for some modern measuring systems. Known as a dozen.  
    13, considered an "unlucky" number in Western superstition. Also known as a "Baker's Dozen".  
    14, the number of days in a fortnight.  
    15, the number of players on a rugby union team. It is also the first point received in tennis.
    16, the base of the hexadecimal number system which is utilized within many programming languages.
    18, age of majority in most countries in the world.  
    19, the length of one side of a Go board.  
    21, the legal drinking age in the United States.  
    22, the namesake of catch-22, a paradoxical condition in which there is no escape due to mutually conflicting or dependent conditions.  
    23, number of chromosomes in a human haploid. Other human cells have 23 pairs of chromosomes.  
    24, number of hours in a day.  
    25, the number of cents in a quarter.  
    26, the number of English letters, bijective base 26 is used in the columns of Microsoft Excel.  
    31, the number of days most months of the year have.  
    42, the "answer to the ultimate question of life, the universe, and everything" in the popular 1979 science fiction work The Hitchhiker's Guide to the Galaxy.  
    60, the number base for some ancient counting systems, such as the Babylonians', and the basis for many modern measuring systems.  
    69, used as slang to refer to a sexual act.  
    86, a slang term that is used in the American popular culture as a transitive verb to mean throw out or get rid of.  
    108, considered sacred by the Dharmic Religions. Approximately equal to the ratio of the distance from Earth to Sun and diameter of the Sun.  
    256, The number of possible combinations within 8 bits, or a byte.  

    And there are others...

    Here are the numbers in a list:  
    [3, 4, 5, 7, 8, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22, 23, 24, 25, 26, 31, 42, 60, 69, 86, 108, 256]
    
    For this list:  
    a) Find a 90% confidence interval for the mean using the Central Limit Theorem.  
    b) Find a 90% confidence interval for the mean using bootstrapping.  
    c) Find a 68% confidence interval for the standard deviation using the Central Limit Theorem.  
    d) Find a 68% confidence interval for the standard deviation using bootstrapping.  
    e) Either a), b), c) or d) is a trick question.  Which one is it, and why?  

5) Conceptual - Studies of American health habits often show that urban dwellers 
  have lower average body mass index (BMI)s and are less likely to be obese than
  people who live in other types of locations. A naive scientist would conclude 
  that living in cities causes people to be thinner.

  Discuss at least two confounding variables and how you might change your sampling
  parameters to mitigate these effects.   
  
  Younger people tend to live in cities, and people tend to walk more in cities 
  than the suburbs.  Isn't it possible that lower BMIs could be due to 1) age and 
  2) activity level rather than living in the city?  
  You could try to mitigate these effects by comparing city/not city results stratified by age and activity level.

6) I surveyed 200 people and looked at their average expenditure on coffee/tea by season. I found that the mean coffee expenditure in winter was greater than that in the summer, with a p-value of .02. Is this significant? Why or why not? What significance level would convince you?  

  This test involves 4 choose 2 comparisons: Winter-Spring, Winter-Summer, Winter-Fall, Spring-Summer, Spring-Fall, Summer-Fall: 4!/((4-2)!2!) = 24 / 4 = 6.  Assuming the desired significance level is 0.05, accounting for these comparisons reduces it conservatively to 0.05/6 ~ 0.008 using the Bonferonni correction.  With this correction the p-value of 0.02 > 0.008, and so it's not significant.

7) What is statistical power, and what are four factors that influence it?   
* the statistical significance criterion used in the test
* the magnitude of the effect of interest in the population
* the sample size used to detect the effect
* the sample variance

