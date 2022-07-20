from collections import Counter
from scipy import stats

def mean(lst): #population and sample
    """[summary]

    Args:
        lst ([type]): [description]

    Returns:
        [type]: [description]
    """
    return sum(lst)/len(lst)

def median(lst):
    """Finds the media of a list

    Args:
        lst (list): List of numbers

    Returns:
        int: The median of the list
    """
    # len(lst) = odd
    if len(sorted(lst)) % 2 != 0:
        idx = len(sorted(lst)) // 2
        return sorted(lst)[idx]
    #len(lst) = even
    else:
        this = len(sorted(lst)) // 2
        that = this - 1
        return sorted(lst)[this] + sorted(lst)[that] / 2

def mode(lst):
    """[summary]

    Args:
        lst ([type]): [description]

    Returns:
        [type]: [description]
    """
    count_values = Counter(lst)
    num_appear = max(list(count_values.values()))
    the_mode = [k for k, v in count_values.items() if v == num_appear]
    from_scipy = stats.mode(lst)
    print(f'Using Scipy: {from_scipy}')
    if len(the_mode) == len(lst):
        return 'No mode found'
    else:
        return the_mode[0], num_appear, count_values

def pop_var(lst):
    """[summary]

    Args:
        lst ([type]): [description]

    Returns:
        [type]: [description]
    """
    sum_ = 0
    for item in lst:
        sum_ += (item - mean(lst))**2
    return sum_/len(lst)

def samp_var(lst):
    """[summary]

    Args:
        lst ([type]): [description]

    Returns:
        [type]: [description]
    """
    sum_ = 0
    for item in lst:
        sum_ += (item - mean(lst))**2
    return sum_/(len(lst) - 1)

def pop_std(lst):
    return pop_var(lst)**0.5

def samp_std(lst):
    return samp_var(lst)**0.5

def main():
    lst = [3, 14, 19, 25, 14]
    mean_lst = mean(lst)
    median_lst = median(lst)
    mode_lst = mode(lst)
    print(f'Mean of list: {mean_lst}')
    print(f'\nMedian of list: {median_lst}')
    print(f'\nMode of list: {mode_lst}')

if __name__ == '__main__':
    main()
