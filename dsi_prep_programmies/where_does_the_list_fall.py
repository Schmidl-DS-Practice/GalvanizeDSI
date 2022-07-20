def median(lst):
    sort_me = sorted(lst)
    if len(sort_me) % 2 == 1:
        return sort_me[len(sort_me) // 2 + 1-1]
    elif len(sort_me) % 2 == 0:
        return (sort_me[len(sort_me) // 2] + sort_me[len(sort_me) // 2-1]) / 2
    
def where_does_the_item_fall(lst):
    dic = {'>=.50': [], '<=.50': []}
    for item in lst:
        if item <= median(lst):
            dic['<=.50'].append(item)
        if item >= median(lst):
            dic['>=.50'].append(item)
    return dic
print(where_does_the_item_fall([1,3,2,5,4]))