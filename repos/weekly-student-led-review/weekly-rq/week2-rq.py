import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

##1
'''---->normal: z-test'''
'''---->bernoulli'''
'''---->exponential(geometric)'''
'''---->poisson'''
'''---->uniform'''
'''---->poisson'''

##2
'''---->CLT: the more samples taken from any distribution, the closer the means resemble the normal
distribution'''

##3
'''---->Take samples from a sample of a population, with replacement.
To gather information about the population.'''

##4
a = [3, 4, 5, 7, 8, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22, 23, 24, 25, 26, 31, 42,
60, 69, 86, 108, 256]
#a Find a 90% confidence interval for the mean using the Central Limit Theorem.
b = np.mean(a)
c = np.std(a)
normal = stats.norm(b, c)
n = normal.ppf(0.10)
o = normal.ppf(0.90)

#b Find a 90% confidence interval for the mean using bootstrapping

#c
'''---->Trick Question'''

#d Find a 68% confidence interval for the standard deviation using bootstrapping.

#e Either a), b), c) or d) is a trick question. Which one is it, and why?

##5
'''---->Confounding Variable: dependent:'''

##6
'''---->A p-value of 0.02 is significant as 0.05 is usually the alpha that is used. As 0.02 < 0.05,
that is significant. An alpha > 0.05 would be enough to convince me.'''

##7
'''---->alpha, effective size, sample size, beta'''


