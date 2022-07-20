def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))


def binomial_dis_pmf(n, k, p):
    return combinations(n, k) * (p**k)*((1-p)**(n-k))

print(binomial_dis_pmf(1000, 3, 0.005))
print(binomial_dis_pmf(1000, 4, 0.005))
print(binomial_dis_pmf(1000, 5, 0.005))
print(binomial_dis_pmf(1000, 6, 0.005))

'''this function must be ammended depending on the question.
if exactly one use binomial pmf. leave alone for < k. if > k do
1 - cdf_accum '''
def cdf_binomial_distr(n, k, p):
    cdf_accum = 0
    for i in range(k):
        cdf_accum += binomial_dis_pmf(n, i, p)

    return cdf_accum
print(1 - cdf_binomial_distr(1000, 10, 0.005))