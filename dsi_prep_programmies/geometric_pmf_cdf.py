def geometric_pmf_before(p, k):
    '''
    A function that calculated the geometric PMF before
    the first success

    parameters:
    p: float
        the probability
    k: int
        number of trials

    returns:
        a probability as a float
    '''
    #Y = k
    return ((1-p)**k)*p

def geometric_pmf_including(p, k):
    '''
    A function that calculated the geometric PMF up to
    and including the first success

    parameters:
    p: float
        the probability
    k: int
        number of trials

    returns:
        a probability as a float
    '''
    #X = k
    return (1-p)**(k-1)*p

def geometric_pmf_dic(p, k):

    '''dictionary of geometric_pmf_before'''

    geometric_d = {}
    for i in range(k+1):
        geometric_d[i] = geometric_pmf_before(p, k)
    return geometric_d

def geometric_cdf_before(p, k):
    '''
    A function that calculated the geometric CDF before
    the first success

    parameters:
    p: float
        the probability
    k: int
        number of trials

    returns:
        a probability as a float
    '''
    #Y < k
    return 1-(1-p)**(k+1)


def geometric_cdf_including(p, k):
    '''
    A function that calculated the geometric CDF up to
    and including the first success

    parameters:
    p: float
        the probability
    k: int
        number of trials

    returns:
        a probability as a float
    '''
    #X <= k
    return 1-(1-p)**k

def geometric_cdf_dic(p, k):

    '''dictionary of geometric_cdf_before'''

    geometric_cdf_d = {}
    for i in range(k+1):
        geometric_cdf_d[i] = geometric_cdf_before(p, k)
    return geometric_cdf_d

def geometric_cdf(p, k):

    '''this is the sum of the geometric_pmf_before'''

    proba_ = 0
    for r in range(k):
        proba_ += geometric_pmf_before(p, k)
    return proba_