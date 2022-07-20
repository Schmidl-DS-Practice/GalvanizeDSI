import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#  Assume you're trying to make (the best) cancer screening model.
#  You have a couple of options:
#  1) Use a single model that has a recall of 90% (a 90% chance of correctly detecting cancer)
#  2) An ensemble model of 11 models, where each model only has a recall of 70%.
#  
#  Which option is better?

def plot_pmf(dist, n_2):
    fig, ax = plt.subplots(1, 1)
    x = np.arange(0, n_2 + 1)
    y = dist.pmf(x)
    ax.plot(x, y, 'bo', ms=8, label='binom pmf')
    ax.vlines(x, 0, y, colors='b', lw=5, alpha=0.5)
    ax.set_xlabel("number of times ensemble accurately predicts cancer")
    ax.set_ylabel("probability")
    plt.show()

def simulation_check(n_2, p_2, num_simulations):
    if n_2 % 2 == 0:
        raise ValueError("You should use an odd number of models!")
    sim_result = []
    for _ in range(num_simulations):
        correct_lst = []
        for model in range(n_2):
            correct = np.random.random()
            if correct <= p_2:
                correct_lst.append(1)
            else:
                correct_lst.append(0)
        if sum(correct_lst) > n_2/2:
            sim_result.append(1)
        else:
            sim_result.append(0)
    return np.mean(sim_result)


if __name__ == '__main__':
    # single model 
    n_1 = 1 
    p_1 = 0.90 

    # ensemble model
    n_2 = 11
    p_2 = 0.7


    # treat each model's prediction as a bernoulli trial with p_2 chance of success,
    # where there are n_2 trails.  The ensemble model's chance of correctly identifying
    # cancer is the sum of the pmf for 6 successes or more

    ensemble = stats.binom(n_2, p_2)
    for i in range(n_2 + 1):
        pmf = ensemble.pmf(i)
        print(f"The probability the ensemble gets {i} right is {pmf:0.2f}.")
    
    p_ensemble = 1 - ensemble.cdf(5)
    print("The ensemble's recall is {0:0.2f}".format(p_ensemble))

    plot_pmf(ensemble, n_2)


    p_simulation_check = simulation_check(n_2, p_2, num_simulations=10000)
    print(f"Simulation check result: {p_simulation_check:0.2f}.")




