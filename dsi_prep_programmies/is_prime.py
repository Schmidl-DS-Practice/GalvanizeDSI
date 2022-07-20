import timeit
starttime = timeit.default_timer()

def is_prime(num):
    if num <= 0:
        return False #'nope'
    elif num == 1:
        return False #'no'
    elif num == 2 or num == 3:
        return 'yay'
    for n in range(3, int(num**0.50 + 1), 2):
        if num % n == 0:
            return False #'again no'
    return 'sure is'

def get_nth_prime(n):
    start = 3
    s_list = [2]
    s_diff = []
    count = 1
    dic = {}
    if n == 1:
        return 2
    while count != n:
        if is_prime(start):
            s_list.append(start)
            count += 1
            start  += 2
    for prime_n, prime_v in enumerate(s_list, 1):
        dic[prime_n] = prime_v
        if len(s_list) == prime_n:
            break
            a = s_list[prime_n] / s_list[prime_n - 1]
            s_diff.append(a)
    return dic, s_diff

print(get_nth_prime(50), '\n')
print("The time the function took to run is :", timeit.default_timer() - starttime)