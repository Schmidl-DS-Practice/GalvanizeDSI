from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
##Basic:Part1

#1:either four or not four. Parameters: n=1256, k=how many fours?, p=1/6

#2:more information about how many of each type of sides

#3:lands or playable(success=land). Parameters: n=100, k=how often there is a land card, p=17/40

#4:hypergeometric

#5:either four or not four. Parameters: n=1256, k=how many fours?, p=9/60

#6:either land on top or not. Parameters: n=100, k=1, p=(num of land/total cards)(prob of num of land)

##Binomial Hypothesis Tests:Part2

#1 a)Ho = 0.50, Ha > 0.5; b) binomial; c)n=137, k=72, p=0.5; d)(1-binomial distribution); e)not reject
n = 137
p = .5
binom_dist = stats.binom(n=n, p=p)
p_value = 1 - binom_dist.cdf(72 - 1)
print(f"p-value: {p_value:.5f}")

cut_off = 72

fig, ax = plt.subplots(1, figsize=(10, 4))
bars = ax.bar(range(cut_off), [binom_dist.pmf(i) for i in range(cut_off)], color="grey")
bars = ax.bar(range(cut_off,n), [binom_dist.pmf(i) for i in range(cut_off,n)], color="red")
ax.set_xlabel("Number of correct answers")
ax.set_ylabel("Probability")
ax.set_title(f"p-value: {p_value:.2f}")
plt.show()

#2
