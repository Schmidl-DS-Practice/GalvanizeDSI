def write_out_num(n):
    """[summary]

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    another = []
    dic = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
        6:'six', 7:'seven', 8:'eight', 9:'nine'}
    for let in str(n):
        if int(let) in dic.keys():
            another.append(dic[int(let)])
    dash = '-'.join(another)
    return dash
print(write_out_num(5002398))
print(write_out_num(2020))
print(write_out_num(15))
print(write_out_num(5280))