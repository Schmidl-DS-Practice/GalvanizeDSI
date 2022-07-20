from abc import ABC
from time import time


def timeit(fn):
    def timed(*args, **kw):
        ts = time()
        fn(*args, **kw)
        te = time()

        return te - ts

    return timed


class SortTester(ABC):
    """
    Abstract base class for our sorting classes

    Allows for the calling of a sort, a stack count sort, and a timed sort
    """
    def __init__(self):
        pass

    @classmethod
    def this_sort(cls, input_list):
        pass

    @timeit
    def timed_sort(self, input_list):
        return self.this_sort(input_list)


class InsertSort(SortTester):
    """
    InsertSort - Class implementation of insert sort

    Usage:
    >>> lst = [4, 1, 2, 3]
    >>> my_sorter = InsertSort()
    >>> my_sorter.this_sort(lst)
    >>> print(lst)
    [1, 2, 3, 4]
    >>> my_sorter.timed_sort(lst)
    """
       

    @classmethod
    def this_sort(cls, input_list):
        '''
        YOUR CODE
        '''
        for i in range(1, len(input_list)):
            j = i
            
            while j > 0:
                if input_list[j-1] > input_list[j]:
                    input_list[j-1], input_list[j] = input_list[j], input_list[j-1]
                    j -= 1

                else:
                    break



class BubbleSort(SortTester):
    
    @classmethod
    def this_sort(cls, input_list):
        '''
        YOUR CODE
        '''
        n = len(input_list)
        while len(input_list) > 0:

            new_n = 0 #what?

            for i in range(1, len(input_list)):
                if input_list[i-1] > input_list[i]:
                    input_list[i-1], input_list[i] = input_list[i], input_list[i-1]
                    new_n = i #what?
            n = new_n   # len(input_list) = new_n-------why not work?

            

class HeapSort(SortTester):
    
    @classmethod
    def this_sort(cls, input_list):
        '''
        YOUR CODE
        '''
        pass


