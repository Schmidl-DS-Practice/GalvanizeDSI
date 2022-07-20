def bubblesort_oneliner(lst):
    '''Bubblesort in a one-line list comprehension, source: 
       https://stackoverflow.com/questions/57350378/bubble-sorting-with-one-list-comprehension
    '''
    [lst.append(lst.pop(0) if i == len(lst) - 1 or lst[0] < lst[1] else lst.pop(1)) 
     for j in range(0, len(lst)) for i in range(0, len(lst))]
    return lst


def swap(lst, i):
    lst[i] = lst[i+1]
    lst[i+1] = lst[i]

def bubblesort(lst):
    '''Bubblesort, more sparse and easier to debug'''
    num_el = len(lst)
    num_passes = num_el - 1
    for p in range(num_passes):
        for i in range(num_el - 1 - p):
            if lst[i] > lst[i+1]:
                swap(lst, i)
    return lst

if __name__ == '__main__':
    lst = [3, 2, 4, 1]
    sorted_one_liner = bubblesort_oneliner(lst)
    sorted_bs = bubblesort(lst)
