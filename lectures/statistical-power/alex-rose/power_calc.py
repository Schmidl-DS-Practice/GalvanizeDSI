from scipy import stats
from math import ceil

def z_power(alpha, n, mu_a, mu_b, s):
    '''Calculates the power of a one-tailed Z-test.

        Args:
            alpha: Allowable Type I error rate.
            n: Sample size.
            mu_a: The mean value of a
            mu_b: The mean value of b
            s: The standard deviation of a
        Returns:
            power: the power of the z-test
    '''
    stderr = s / n**.5
    score = (mu_b - mu_a)/stderr - stats.norm.ppf(1-alpha)
    return stats.norm.cdf(score)

def z_solve_for_n(power, alpha, mu_a, mu_b, s):
    '''Solves for the number of samples needed
        to achieve a particular power on a one-tailed Z-test.

        Args:
            power: The desired power.
            alpha: Allowable Type I error rate.
            mu_a: The mean value of a
            mu_b: The mean value of b
            s: The standard deviation of a (note: We make a simplying assumption that)
        Returns:
            n: The required sample size.
    '''
    return ((stats.norm.ppf(power) - stats.norm.ppf(alpha)) * s / (mu_b - mu_a) )**2

if __name__ == "__main__":
    # Breakout 2 starting code
    alpha = 0.20 # tolerated Type I error rate (incorrectly rejecting H0)
    beta = 0.05   # tolerated Type II error rate (failing to reject H0 when we should)
    power = 1 - beta

    mu_a = 0.06  # the mean value of a
    mu_b = 0.07  # the mean value of b
    s = 0.24    # the standard deviation of a
    
    required_n = z_solve_for_n(power, alpha, mu_a, mu_b, s)
    print(required_n)

    # Code here for Breakout 3




