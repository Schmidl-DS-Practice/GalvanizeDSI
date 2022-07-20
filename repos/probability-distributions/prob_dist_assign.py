import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

##Basic:Part 1
#1
poisson = stats.poisson.pmf(0, 2)
#print(poisson)

#2
binomial = stats.binom.pmf(n=20, k=2, p=0.1)
#print(binomial)

#3
binomial1 = stats.binom.cdf(n=20, k=2, p=0.1)
#print(binomial1)

#4 
poisson1 = stats.poisson.pmf(0, 1.5)
#print(poisson1)

#5; rate = 2 person / 1 min * 8 tall / 100 persons = 0.16 tall persons / min
exponential = stats.expon(scale=1/.16)
#print(1-exponential.cdf(10))

#6


#Advanced:Part 2
#1
def profit_rvs():
    num_views = int(stats.uniform(loc=5000, scale=1000))
    conversions = stats.binom(p=0.12, n=num_views).rvs()
    wholesales = stats.binom(p=0.2, n=conversions).rvs()
    non_wholesales = stats.binom(conversions - wholesales)
    profit = (wholesales * 50 + non_wholesales * 60)
    return profit

#2
samples = [profit_rvs() for i in range(10000)]

fig, ax = plt.subplots()
ax.hist(samples, bins=30)
ax.set_xlabel('profit', fontsize=14, fontweight='bold')
ax.set_ylabel('freq', fontsize=14, fontweight='bold')
ax.set_title('histo of rand gen profits')
print()

#3
print('2.5%', np.percential(samples, 2.5))
print('97.5%', np.percentil(samples, 97.5))