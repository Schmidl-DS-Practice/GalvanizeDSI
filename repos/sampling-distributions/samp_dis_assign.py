import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

#Basic:Part 1
def bootstrap(x, resamples=5):
    """"Draw bootstrap resamples from the array x.

    Parameters
    ----------
    x: np.array, shape (n, )
      The data to draw the bootstrap samples from.
    
    resamples: int
      The number of bootstrap samples to draw from x.
    
    Returns
    -------
    bootstrap_samples: np.array, shape (resamples, n)
      The bootsrap resamples from x.
    """
    n_obs = x.shape[0]
    print(x)
    boot_samples = []
    for _ in range(resamples):
        boot_idxs = np.random.randint(n_obs, size=n_obs)
        boot_sample = x[boot_idxs]
        boot_samples.append(boot_sample)
        print('boot_idxs:', boot_idxs)
        print('boot_sample:', boot_sample)
    return boot_samples

print(bootstrap(np.array([1,2,3,4,5])))

#Part 2
productivity = np.loadtxt('/home/leonardo-leads/Documents/galvanize_dsi/repos/sampling-distributions/data/productivity.txt')

#Q2: The decision should be base off the confidence interval and the mean difference.

#Q3:
def bootstrap_ci(sample, stat_function=np.mean, resamples=5, ci=95):
    """Calculate the CI of chosen sample statistic using bootstrap sampling.

    CI = confidence interval

    Parameters
    ----------
    sample: Numpy array
        1-d numeric data

    stat_function: function, optional (default=np.mean)
        Function for calculating as sample statistic on data

    iterations: int, optional (default=1000)
        Number of bootstrap samples to create

    ci: int, optional (default=95)
        Percent of distribution encompassed by CI, 0<ci<100

    Returns
    -------
    tuple: lower_ci(float), upper_ci(float), bootstrap_samples_statistic(array)
        Lower and upper bounds of CI, sample stat from each bootstrap sample
    """
    boostrap_samples = bootstrap(sample, resamples=resamples)
    bootstrap_samples_stat = list(map(stat_function, boostrap_samples))
    low_bound = (100. - ci) / 2
    high_bound = 100. - low_bound
    lower_ci, upper_ci = np.percentile(bootstrap_samples_stat, [low_bound, high_bound])
    return lower_ci, upper_ci, bootstrap_samples_stat

lower_ci, upper_ci, bootstrap_means_prod = bootstrap_ci(productivity, ci=95)
print("The 95% bootstrapped CI of the mean: ({}, {})".format(lower_ci, upper_ci))

#Q4:
fig, ax = plt.subplots(figsize=(10, 4))
ax.hist(bootstrap_means_prod, bins=20)
ax.set_ylabel('Count')
ax.set_xlabel('Difference in Productivity')

plt.show()
