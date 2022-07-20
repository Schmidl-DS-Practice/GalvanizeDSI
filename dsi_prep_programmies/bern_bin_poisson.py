import random
from fact_comb_permu import combinations
from fact_comb_permu import factorial
from math import e

def bernoulli_random(p = 0.5):
    '''random variables which consist of a single trial that can be
    either success or failure. E(x) = mean = p. var = p*(1-p)
    random.random() gives random float num btwn 0,1;
    random.randint() gives a random int btwn specified nums;
    random.choice() gives a random parameter from given
    random.choices() gives random parameter from given, weighted,
        commulative weighted, k = num of times to run'''
    p = random.random()
    if p >= 0.5:
        return 1
    return 0

def binomial_pmf(n, k , p):
    '''P(X = k). random var represents number of successes in bern
        trials. model probabilities which represent num of successes
        in num trials'''
    return combinations(n, k)*(p**k)*((1-p)**(n-k))

def binomial_cdf(n, k, p):
    sum_ = 0
    for i in range(k + 1):
        '''k + 1 = P(X<=x); k = P(X<x);
            k + 1 and 1 - sum_ = P(X>x); k and 1 - sum_ = P(X>=x); '''
        sum_ += binomial_pmf(n, i, p)
    return sum_
'''binomial: expected value = n * p; var = n*p*(1-p);
    std = (n*p*(1-p))**.5'''

def poisson_pmf(lmbda, k):
    '''proba of a given number of events occuring in some fixed
    time or space. assumptions: events occur at a known constant
    rate; each occurence is independent. sample space is infinite.
    P(X=k). new lambda = alpha * time'''
    return (lmbda**k)*(e**-lmbda)/factorial(k)

def poisson_cdf(lmbda, k):
    sum_ = 0
    for i in range(k+1):
        '''k+1 = P(X<=k); k = P(X<k);
            k+1 and 1 - sum_ = P(X>k); k and 1 - sum_ = P(X>=k)'''
        sum_ += poisson_pmf(lmbda, i)
    return sum_
'''poisson: expected value = lmbda; var = lmbda; std = lmbda**.5 '''