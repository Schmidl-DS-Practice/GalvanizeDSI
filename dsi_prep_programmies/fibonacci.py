def fibonacci(fibo):
    i = 1
    fib = []
    if fibo == 1:
        fib = [0]
    if fibo >= 2:
        fib = [0, 1]
        while i < (fibo - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci(10))

# recursion
# def fib(n):
#     if n == 0:
#         result = 0
#     elif n == 1:
#         result =  1
#     else:
#         result = fib(n-1) + fib(n-2)
#     return result

# print(fib(5))
