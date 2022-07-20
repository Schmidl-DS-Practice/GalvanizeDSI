def divisible_by(arr, int1, int2):
    '''
    INPUT: NUMPY ARRAY, INT, INT
    OUTPUT: NUMPY ARRAY
    
    arr in a numpy array of integers.  int1 and int2 are integers.  Return
    an array of the integers in arr that are divisible without remainder by both 
    int1 and int2. 

    For example:
    In [1] arr_out = divisible_by(np.array([0, 24, 3, 12, 18, 17]), 3, 4)
    In [2] arr_out
    Out[2] np.array([0, 24, 12])
    '''
    return arr[(arr%int1==0) & (arr%int2==0)]


def bubble_sort(arr):
    '''
    INPUT: LIST
    OUTPUT: LIST OF LISTS

    Implement the bubble sort algorithm to sort arr.  However, upon on each swap,
    append the new list as the next row in a list containing all the swaps.
    The original list should be the first row in the list detailing the swaps.

    For example:
    In [1] arr = [7, 4, 2, 5]
    In [2] bs = bubble_sort(arr)
    In [3] bs
    Out[3]
    [[7, 4, 2, 5],
     [4, 7, 2, 5],
     [4, 2, 7, 5],
     [4, 2, 5, 7],
     [2, 4, 5, 7]]

    ''' 
    arr_lst = []
    arr_lst.append(arr.copy())
    for i in range(len(arr), 0, -1):
        for j in range(1, i):
            if arr[j - 1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
                arr_lst.append(arr.copy())
    return(arr_lst)


def fizz_buzz():
    '''
    INPUT: None 
    OUTPUT: LIST

    Write a program that appends the numbers from 1 to 100 into list. But for 
    multiples of three append “Fizz” instead of the number and for the multiples
    of five append “Buzz”. For numbers which are multiples of both three and five
    append “FizzBuzz”.

    The first five elements of your list should be:
    lst = [1, 2, "Fizz", 4, "Buzz", ....]
    '''
    lst = [] 
    for i in range(1, 101):
        div3 = i % 3 == 0
        div5 = i % 5 == 0
        div3and5 = div3 and div5
        if div3and5:
            lst.append("FizzBuzz")
        elif div3:
            lst.append("Fizz")
        elif div5:
            lst.append("Buzz")
        else:
            lst.append(i)
    return lst


def fibonacci():
    '''
    INPUT: None
    OUTPUT: LIST
    
    Write a function that computes the list of the first 20 Fibonacci numbers.
    By definition, the first two numbers in the Fibonacci sequence are 0 and 1,
    and each subsequent number is the sum of the previous two. As an example, 
    here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
    '''
    lst = [0, 1] 
    for i in range(2,20):
        lst.append(lst[i-2] + lst[i-1])
    return lst


def linear_regression(X_train, y_train, X_test, y_test):
    '''
    Fit a linear regression model with X_train and y_train using
    scikit-learn, and return the beta coefficients. Then calculate and
    return the R^2 value using X_test and y_test.

    Parameters
    ----------
    X_train: NumPy Array (size: N x P)
    y_train: NumPy Array (size: N x 1)
    X_test: NumPy Array (size: M x P)
    y_test: NumPy Array (size: M x 1)
   
    Returns
    -------
    tuple of floats, float
    The tuple contains the beta coefficients of the fit model, and the
    remaining float is the R^2 value of the test data using that model.
    
    Note
    ----
    The R^2 statistic, also known as the coefficient of determination, is a
    popular measure of fit for a linear regression model.  If you need a
    refresher, this wikipedia page should help:
    https://en.wikipedia.org/wiki/Coefficient_of_determination
    '''
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    return regr.coef_, regr.score(X_test, y_test)


def markets_per_state():
    '''
    INPUT: NONE
    OUTPUT: STRING (of SQL statement)

    Return a SQL statement which gives the states and the
    number of markets for each state which take WIC or WICcash.
    '''

    return '''SELECT State, COUNT(1)
              FROM farmersmarkets
              WHERE WIC='Y' OR WICcash='Y'
              GROUP BY State;'''

