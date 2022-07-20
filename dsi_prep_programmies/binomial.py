# probably of 5 successes in 20 trials, p=0.3

def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))


def binomial_pmf(n, k, p=0.005):
    return combinations(n, k) * (p**k) * ((1 - p)**(n - k))

print(binomial_pmf(1000, 3))

# def binomial_dict(n, p=0.5):
#     d = {}
#     for k in range(0, n+1):
#         d[k] = binomial_pmf(n, k, p)

#     return d

# d = binomial_dict(20, 0.3)

# for k, v in d.items():
#     # print(f'{k}: {"*" * int(v*160)}')
#     print(f'{k}: {v}')