import random
def flip_coin_random(n):
    '''
    A function that will randomly flip a coin using the random.random() method

    parameters:
    n: int
    an integer that will be the number of flips

    returns:
    a dictionary with the head and tails counts and a list of the choices in the order
    that they were flipped
    '''
    dic = {'heads': 0, 'tails': 0}
    random_lst = []
    for _ in range(n):
        if random.random() >= 0.5:
            dic['heads'] += 1
            random_lst.append('h')
        else:
            dic['tails'] += 1
            random_lst.append('t')
    return dic, random_lst

def flip_coin_integer(n):
    '''
    A function that will randomly flip a coin using the random.randint() method

    parameters:
    n: int
    an integer that will be the number of flips

    returns:
    a dictionary with the head and tails counts and a list of the choices in the order
    that they were flipped
    '''
    dic = {'heads': 0,'tails': 0}
    integer_lst = []
    for _ in range(n):
        randint_flip = random.randint(0, 1)
        if randint_flip == 1:
            dic['heads'] += 1
            integer_lst.append('h')
        else:
            dic['tails'] += 1
            integer_lst.append('t')
    return dic, integer_lst
            

print(flip_coin_random(100))
print(flip_coin_integer(100))