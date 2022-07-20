from math import e

def factorial(k):
    prod = 1
    for num in range(2, k+1):
        prod *= num
    return prod

#lmbda = alpha * t
def poisson_pmf(lmbda, k):
    return (lmbda**k)*(e**-lmbda)/factorial(k)

print(poisson_pmf(6, 10))
print(poisson_pmf(5.25, 10)) #is this right?
print(poisson_pmf(60, 30))
print(poisson_pmf(8, 2))


def poisson_cdf(lmbda, k):
    poisson_accu = 0
    for i in range(k+1):
        poisson_accu += poisson_pmf(lmbda, k)
    return poisson_accu


def poisson_dic(lmbda, low_k, high_k):
    poisson_d = {}
    for k in range(low_k, high_k + 1):
        poisson_d[k] = poisson_cdf(lmbda, k)
    return poisson_d
