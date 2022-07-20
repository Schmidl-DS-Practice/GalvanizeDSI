def factorial(flips):
    prod = 1
    for num in range(1, flips+1):
        prod *= num
    return prod

def combinations(flips, num_heads):
    return int(factorial(flips) / (factorial(flips-num_heads) * factorial(num_heads)))

#flips = n; num_heads = k
def prob_heads_k_times(flips, num_heads, p = 0.5):
    return combinations(flips, num_heads) * (p**num_heads)*((1-p)**(flips-num_heads))

print(prob_heads_k_times(10, 10, p = 0.5))
print(prob_heads_k_times(10, 9, p = 0.5))
print(prob_heads_k_times(10, 8, p = 0.5))
print(prob_heads_k_times(10, 7, p = 0.5))
print(prob_heads_k_times(10, 6, p = 0.5))
print(prob_heads_k_times(10, 5, p = 0.5))
print(prob_heads_k_times(10, 4, p = 0.5))
print(prob_heads_k_times(10, 3, p = 0.5))
print(prob_heads_k_times(10, 2, p = 0.5))
print(prob_heads_k_times(10, 1, p = 0.5))
print(prob_heads_k_times(10, 0, p = 0.5))