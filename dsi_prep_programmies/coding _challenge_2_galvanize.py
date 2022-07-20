def sigmoid(x):
  '''
  Returns the result of passing a number into the sigmoid
  logistic function. Assumes the value of e to be 2.71828

  Parameters
  ----------
  x: number
    the number to pass into the sigmoid logistic function

  Returns
  -------
  result: number
    result of the sigmoid logistic function
    '''
  e = 2.71828
  s = 1/(1 + e**(-x))
  return s

#s = 1.0 for x >=37
print(sigmoid(0.01))
print(sigmoid(0.1))
print(sigmoid(0.25))
print(sigmoid(0.5))
print(sigmoid(36))
print(sigmoid(37))