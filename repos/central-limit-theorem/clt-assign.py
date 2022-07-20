import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

import scipy.stats as stats

def make_draws(dist, params, size=200):
    """
    Draw a sample from a specified distribution
    with given parameters and return these in an array.

    Parameters
    ----------

    dist: scipy.stats distribution object:
      Distribution object from scipy.stats, must have a .rvs method

    params: dict:
      Parameters needed to define the distribution dist.
    For example, if dist = scipy.stats.binom, then params could be

          {'n': 100, 'p': 0.25}

    size: int:
      The number of values to draw

    Returns
    -------
    sample: np.array, shape (size, )
      An i.i.d sample from the specified distribution.
    """
    return dist(**params).rvs(size)

# Generate draws from the Binomial Distribution, using Scipy's binom object.
binomial_samp = make_draws(stats.binom, {'n': 100, 'p':0.25}, size=10)
#print('binomial---', binomial_samp, '\n')

uniform = make_draws(stats.uniform, {'loc':10, 'scale':20}, size=10)
#print('uniform---', uniform, '\n')

pois = make_draws(stats.poisson, {'mu':2}, size=10)
#print('pois---', pois, '\n')

exponen = make_draws(stats.expon, {'scale':2}, size=10)
#print('exponen---', exponen, '\n')

geom = make_draws(stats.geom, {'p':0.1}, size=10)
#print('geom---', geom)

def plot_means(ax, dist, dist_name, params, repeat=5000, size=200):
    samp_mat = np.zeros((repeat, size))
    for idx in range(repeat):
        samp_mat[idx, :] = make_draws(dist, params, size=size)
    samp_mean = np.mean(samp_mat, axis=1)
    ax.hist(samp_mean, bins=25)
    ax.set_xlabel('mean')
    ax.set_ylabel('count')
    ax.set_title('samp means')

fig, axs = plt.subplots(5, 1, figsize=(5, 20))
plot_means(axs[0], stats.binom, 'binomial', {'n':100, 'p': 0.1}, size=)
plot_means(axs[1], stats.uniform, 'uniform', {'loc':100, 'scale': 20}, size=)
plot_means(axs[2], stats.poisson, 'poisson', {'mu':2}, size=)
plot_means(axs[3], stats.expon, 'exponential', {'scale': 2}, size=)
plot_means(axs[4], stats.geom, 'geometric', {'p': 0.1}, size=)
plt.tight_layout()
plt.show()
