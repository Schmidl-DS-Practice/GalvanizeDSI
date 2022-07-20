def median_of_whole_list(lst):
    sort_me = sorted(lst)
    if len(sort_me) % 2 == 1:
        return sort_me[len(sort_me) // 2 + 1-1]
    elif len(sort_me) % 2 == 0:
        return (sort_me[len(sort_me) // 2] + sort_me[len(sort_me) // 2-1]) / 2

def where_does_the_item_fall(lst):
    dic = {'<.50': [], '>.50': []}
    for item in lst:
        if item < median_of_whole_list(lst):
            dic['<.50'].append(item)
        if item > median_of_whole_list(lst):
            dic['>.50'].append(item)
    return dic

def median_of_lower_50(lst):
    sort_me = sorted(where_does_the_item_fall(lst)['<.50'])
    if len(sort_me) % 2 == 1:
        return sort_me[len(sort_me) // 2 + 1-1]
    elif len(sort_me) % 2 == 0:
        return (sort_me[len(sort_me) // 2] + sort_me[len(sort_me) // 2-1]) / 2

def median_of_upper_50(lst):
    sort_me = sorted(where_does_the_item_fall(lst)['>.50'])
    if len(sort_me) % 2 == 1:
        return sort_me[len(sort_me) // 2 + 1-1]
    elif len(sort_me) % 2 == 0:
        return (sort_me[len(sort_me) // 2] + sort_me[len(sort_me) // 2-1]) / 2

def each_quartile(lst):
    d = {'>=0.00, <=.25':[],'>.25, <=.50':[],'>.50, <=.75':[],'>.75, = 1.00':[]}

    for item in lst:
        if item <= median_of_lower_50(lst):
            d['>=0.00, <=.25'].append(item)
        elif item > median_of_lower_50(lst) and item <= median_of_whole_list(lst):
            d['>.25, <=.50'].append(item)
        elif item > median_of_whole_list(lst) and item <= median_of_upper_50(lst):
            d['>.50, <=.75'].append(item)
        else:
            d['>.75, = 1.00'].append(item)
    return d
print(each_quartile([1,3,2,5,4,6]))