def divisors(n):
    return [ele for ele in range(1, n + 1) if n % ele == 0]
print(divisors(65380))