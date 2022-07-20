from random import choice

def flip_a_coin(num):
    coin_dic = {'heads': 0, 'tails': 0}
    choice_lst = []

    for _ in range(num):
        random_h_t = choice(('h', 't'))
        if random_h_t == 'h':
            coin_dic['heads'] += 1
            choice_lst.append('h')
        else:
            coin_dic['tails'] += 1
            choice_lst.append('t')

    return coin_dic, choice_lst

print(flip_a_coin(10))