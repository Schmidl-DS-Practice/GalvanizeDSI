from scipy.stats import gamma, poisson
import numpy as np

class Bayes_Poisson():
    '''
    Bayes_Poisson - A Poisson PMF that supports a Bayesian update mechanics
    automatically tracks states as update occur
    '''
    def __init__(self, prior_lambda, prior_strength=1.):
        self.alpha = [prior_lambda*prior_strength]
        self.beta = [prior_strength]

    def pmf(self, x, step_n=-1):
        '''
        pmf
        * pars *
        x (int) -> number of observations in a time window
        step_n (int, default -1) -> variable for history tracking.  
        -1 is the current values for alpha and beta
        * returns *
        PMF for the poisson distribution for x observations
        '''
        return poisson.pmf(x, self.alpha[step_n]/self.beta[step_n])

    def update(self, observation_arr):
        '''
        update - updates internal parameters alpha and beta
        * pars *
        observation_arr (array of integers) -> data of observed counts
        * returns *
        None
        '''
        self.alpha.append(self.alpha[-1] + np.sum(observation_arr))
        self.beta.append(self.beta[-1] + len(observation_arr))

    def prior_pdf(self, x, step_n=-1):
        '''
        prior_pdf - returns the PDF of the current priors for lambda
        x (float) -> value of lambda
        step_n (int, default -1) -> variable for history tracking.  
        -1 is the current values for alpha and beta
        * returns *
        PDF for the Gamma distribution for potential lambda values
        '''
        return gamma.pdf(x, self.alpha[step_n], scale=1./self.beta[step_n])

    def prior_cdf(self, x, step_n=-1):
        return gamma.cdf(x, self.alpha[step_n], scale=1./self.beta[step_n])

    def get_lambda(self, step_n=-1):
        return self.alpha[step_n]/self.beta[step_n]

    def get_credible_region(self, percent_confidence=.9, step_n=-1):
        remaining = (1.-percent_confidence)/2.
        return gamma.ppf(remaining, self.alpha[step_n], scale=1./self.beta[step_n]), gamma.ppf(1 - remaining, self.alpha[step_n], scale=1./self.beta[step_n])