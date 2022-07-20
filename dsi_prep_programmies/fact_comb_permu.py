def factorial(n):
    #number of poss orderings of n items
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def permutations(n, k):
    '''all diff ways to choose, without replacement, a diff order of
    a subset of things '''
    return factorial(n) / factorial(n - k)

def combinations(n, k):
    '''like permutations, except now order doesn't matter. how
    many ways can we combine a ceratin size subset of these things?'''
    return factorial(n)/(factorial(n-k)*factorial(k))

def main():

    n = 18
    k = 5

    print(combinations(n, k))

if __name__ == "__main__":
    main()