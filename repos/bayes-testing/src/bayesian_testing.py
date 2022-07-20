import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def first_plot():
    fig, ax = plt.subplots()
    ax.plot(x, pdf, c='purple', linestyle='--')
    ax.set_ylim([0, 1.01])
    ax.set_xlabel('CTR')
    ax.set_ylabel('PDF')
    plt.show()

def plot_with_fill(ax, x, y, label, show=True):
    if show:
        lines = ax.plot(x, y , label=label, lw=2)
        ax.set_xlabel('CTR')
        ax.set_ylabel('PDF')
        ax.legend(loc='upper right')
        ax.fill_between(x, 0, y, alpha=0.2, color=lines[0].get_c())
    #plt.show()

def calculate_and_plot_views(arr, view_lst, show=True):
#    start with a, b
#        make a beta dist with that a and b
#        plot it
#        for a given number of views
#            calculate successes
#            calcultate failures
#            calculate new a and new b
#            make a beta with new a and new b
#            plot it
#
    if show:
        a = 1 # alpha for prior
        b = 1 # beta for prior
        beta = stats.beta(a, b) # makes a beta distribution
        x = np.linspace(0, 1.0, 1001) #x axis points, CTR between 0-1
        pdf = beta.pdf(x) # makes prior pdf
        pdf = pdf/max(pdf)  # dividing the pdf by its max value to normalize
        fig, ax = plt.subplots()
        plot_with_fill(ax, x, pdf, 'Prior')
        for views in view_lst:
            arr_ss = arr[:views]
            successes = arr_ss.sum()
            arr_len = len(arr_ss)
            failures = arr_len - successes
            a = 1 + successes
            b = 1 + failures
            beta = stats.beta(a, b) # makes a beta distribution
            pdf = beta.pdf(x) # makes prior pdf
            pdf = pdf/max(pdf)  # dividing the pdf by its max value to normalize
            plot_with_fill(ax, x, pdf, f'Posterior after {views} views.')
        plt.show()


if __name__ == '__main__':

    #Q1
    arr_A = np.loadtxt('/home/leonardo_leads/Documents/SchoolDocs/GalvanizeDSI/repos/bayes-testing/data/siteA.txt')
    arr_B = np.loadtxt('/home/leonardo_leads/Documents/SchoolDocs/GalvanizeDSI/repos/bayes-testing/data/siteB.txt')

    #Q2
    x = np.linspace(0, 1.0, 1001) #x axis points, CTR between 0-1
    uni = stats.uniform(0,1) #the a and b
    pdf = uni.pdf(x)

    fig, ax = plt.subplots()
    plot_with_fill(ax, x, pdf, 'Prior', show=False)
    plt.close()
    #Q3
    a = 1
    b = 1
    bet = stats.beta(a, b)
    beta_pdf = bet.pdf(x)
    fig, ax = plt.subplots()
    plot_with_fill(ax, x, beta_pdf, 'Prior')

    #Q4
    arr_A_50 = arr_A[:50]
    success = arr_A_50.sum()
    failure = len(arr_A_50) - success

    new_alpha = success + a
    new_beta = failure + b

    #Q5
    x = np.linspace(0, 1.0, 1001) #x axis points, CTR between 0-1
    #Prior
    alpha = 1
    beta = 1
    prior = stats.beta(alpha, beta)
    prior_pdf = prior.pdf(x) # y1
    #Posterior after 50 views
    alpha += success
    beta +=  failure
    posterior_50 = stats.beta(alpha, beta)
    posterior_pdf_50 = posterior_50.pdf(x) #y2
    # make the plots
    fig, ax = plt.subplots()
    plot_with_fill(ax, x, prior_pdf, 'Prior', show=True) 
    plot_with_fill(ax, x, posterior_pdf_50, 'Posterior after 50 views',
                   show=True)
    plt.show() 

    #Q6
    view_lst = [50, 100, 200, 400, 800]
    calculate_and_plot_views(arr_A, view_lst, show=True)

