from random import random

def bernoulli(p):
    num = random()
    if num <= p:
        return '1, that is a success'
    else:
        return '0, oh that is a failure'


def geometric(p):
    lst = []
    for _ in range(100000000):
        trial = bernoulli(p)
        lst.append(trial)
        if trial == 1:
            break

    return lst, len(lst) -1
print(geometric(0.5))

