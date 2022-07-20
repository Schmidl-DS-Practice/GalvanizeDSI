def factorial_iteration(n):
    result = 1
    if n == 0:
        return result 
    else:
        for i in range(1, n+1):
            result *= i
    return result

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


if __name__ == "__main__":
    n = 5

    res_it = factorial_iteration(n)
    res_rec = factorial_recursive(n)

    print(f"\nFactorial of {n}:")
    print(f"iteration: {res_it}")
    print(f"recursion: {res_rec}")

        
