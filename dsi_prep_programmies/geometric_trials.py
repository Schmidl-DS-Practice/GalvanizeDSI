from random import random

def bernoulli(p = 0.5):
    if random() < p:
        return 1
    else:
        return 0

def geometric(p = 0.5):
    lst = []
    for _ in range(100000):
        trial = bernoulli()
        lst.append(trial)

        if trial == 1:
            break
    return len(lst) - 1

def geometric_samples_dict(p = 0.05,  num_samples = 10000):
    dic = {}
    for _ in range(num_samples):
        num_trials = geometric()
        if num_trials not in dic:
            dic[num_trials] = 0
        dic[num_trials] += 1
    return dic

dic = geometric_samples_dict(p = 0.05,  num_samples = 10000)
for k,v in sorted(dic.items()):
    print(f'{k}:{v}')

def geometric_samples_proba_dict(p=0.5, num_samples=10000):
    dic = geometric_samples_dict(p, num_samples)
    new_d = {}
    for k, v in dic.items():
        new_d[k] = v/num_samples
    return new_d

print(geometric_samples_proba_dict(p=0.5, num_samples=10000))