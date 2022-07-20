from scipy.stats import norm

# LOC=MEAN DEFAULT IS 0; SCALE=STD DEFAULT IS 1
normal = norm.cdf(53, loc=46.8, scale=1.75)
print(normal)
# IF HAVE A ZSCORE
zscore = norm.cdf(.543)
# print(zscore)

# PERCENTILES
# .9 = 90TH PERCENTILE
percentile = norm.ppf(.9, loc=1.25, scale=.46)
# print(percentile)