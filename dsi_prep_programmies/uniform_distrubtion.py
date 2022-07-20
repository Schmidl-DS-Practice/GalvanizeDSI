# discrete uniform in the range from 25-125

from random import choice

def get_uniform_value(uniform_distr):
    return choice(uniform_distr)

uniform = list(range(25, 125+1))

print(get_uniform_value(uniform))
