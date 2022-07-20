import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def flip_coin(n, p):
    """Flip a coin of fairness p, n times.
    
    Parameters
    ----------
    n: int
      The number of times to flip the coin.

    p: float, between zero and one.
      The probability the coin flips heads.

    Returns
    -------
    flips: np.array of ints
      The results of the coin flips, where 0 is a tail and 1 is a head.
    """
    return [np.random.choice([0,1], p=[1-p,p]) for x in range(n)]
flips = flip_coin(10,0.5)

def coin_log_likelihood(p, flips):
    """Return the log-likelihood of a parameter p given a sequence of coin flips.
    """
    binomial = stats.binom(n=1, p=p)
    log_sum = 0
    for flip in flips:
        log_sum += np.log(binomial.pmf(flip))
    return log_sum

flip_data = np.array([1,0,0,0,1,1,0,0,0,0])

p1_likelihood = coin_log_likelihood(.25, flip_data)
p2_likelihood = coin_log_likelihood(0.5, flip_data)
print(p1_likelihood,p2_likelihood)
fig, ax = plt.subplots(figsize=(5,5))
tick_loc = np.arange(2)
print(tick_loc)
ax.bar(tick_loc, np.array([p1_likelihood,p2_likelihood]), width=0.8, alpha=0.7)
ax.set_xticks(ticks=tick_loc)
ax.set_xticklabels([0.25, 0.5])
plt.show()






