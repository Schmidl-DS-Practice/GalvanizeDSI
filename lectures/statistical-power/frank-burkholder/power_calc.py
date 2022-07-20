
from scipy import stats

alpha = 0.01 # allowable Type I error rate (incorrectly rejecting H0)
beta = 0.05   # allowable Type II error rate (failing to reject H0 when we should)
power = 1 - beta

mu_a = 0.012  # the mean value of a
mu_b = 0.01  # the mean value of b
s = 0.099     # effective standard deviation of the difference between a & b distributions

n = ((stats.norm.ppf(1-beta) - stats.norm.ppf(alpha)) * s / (mu_b - mu_a))**2






