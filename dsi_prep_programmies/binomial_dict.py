def factorial(flips):
    prod = 1
    for num in range(1, flips+1):
        prod *= num
    return prod

def combinations(flips, num_heads):
    return int(factorial(flips) / (factorial(flips-num_heads) * factorial(num_heads)))


def prob_heads_k_times(flips, num_heads, p = 0.5):
    return combinations(flips, num_heads) * (p**num_heads)*((1-p)**(flips-num_heads))

def binomial_dict(flips):
    '''Returns a dictionary which shows the probability for each
    possible value of k given n. Each value of k should be
    represented by a dictionary key, and the values should represent
    each probability associated with its key.
    It is ok to assume that only valid numbers will be passed into
    the function. There is no need to handle exceptions or edge
    cases.
    Parameters
    ----------
    n : int
        The number of Bernoulli Trials
    Returns
    -------
    d : dict
        A dictionary which has keys that represent all possible
        values of k as keys, and the associated probability stored
        as the values
    '''
    dic = {}
    for i in range(flips + 1):
        dic[i] = prob_heads_k_times(flips, i, 0.50)
    # dic[another_fact] = prob_heads
    return dic

print(binomial_dict(10))
print(binomial_dict(20))
print(binomial_dict(15))





