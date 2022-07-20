import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def plot_distribution(x, y, label):
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8,4))
    ax.plot(x, y, c='k', label=label)
    ax.set_xlabel('time (minutes)')
    ax.set_ylabel('pdf')
    plt.tight_layout(pad=1)
    plt.savefig('expon_dist.png', dpi=100)


if __name__ == '__main__':
    lmda_1mile = 9 # minutes/mile
    lmda_3mile = 3 * lmda_1mile # minutes/3miles (27 minutes/3miles)

#    mu = 4 # average amount of time
#    m = 1/mu
    

    dist_expon = stats.expon(scale=lmda_3mile)

    x_01 = dist_expon.ppf(0.00)
    x_99 = dist_expon.ppf(0.99)

    times = np.linspace(x_01, x_99, 50)
    pdf = dist_expon.pdf(times)

    plot_distribution(times, pdf, '27 minutes/3 miles') 




