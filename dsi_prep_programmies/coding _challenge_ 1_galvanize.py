def rec_dig_sum(n):
  '''
  Returns the recursive digit sum of an integer.

  Parameter
  ---------
  n: int

  Returns
  -------
  rec_dig_sum: int
  the recursive digit sum of the input n
  '''
  summie = 0
  n_to_str = str(n)
  if type(n) != int:
    return 'not an integer, try again'
  elif n_to_str[0] == '-':
    summie = int(n_to_str[0] + n_to_str[1])
    n_to_str = n_to_str[2:len(n_to_str)]
  for ele in n_to_str:
    summie += int(ele)
  if summie > 9:
    return rec_dig_sum(summie)
    
  return summie

print(rec_dig_sum(12345))
print(rec_dig_sum(-6273451))
print(rec_dig_sum('moose'))
print(rec_dig_sum([1,2, 'hmm']))
print(rec_dig_sum((1,2,3,4,'cow')))
print(rec_dig_sum(12.34))
print(rec_dig_sum(-59))
print(rec_dig_sum(46))
print(rec_dig_sum(-9))
print(rec_dig_sum(7))
print('-------------------------------')

def distr_of_rec_digit_sums(low=0, high=1500):
  '''
  Returns a dictionary representing the counts
  of recursive digit sums within a given range.

  Parameters
  ----------
  low: int
    an integer, 0 or positive, representing
    the lowest value in the range of integers
    for which finding the recursive digit sum
  high: int
    a positive integer greater than low, the
    inclusive upper bound for which finding
    the recursive digit sum

  Returns
  -------
  dict_of_rec_dig_sums: {int:int}
    returns a dictionary where the keys are
    the recursive digit sums and the values
    are the counts of those digit sums occurring
  '''
  
  rec_dic = {}
  if high <= low or low < 0:
    return 'high must be greater than low; low must be positive'

  #tested to work with below two lines
  #if low < 0:
    #return 'low must be positive'

  for n in range(low, high + 1):
    if rec_dig_sum(n) not in rec_dic:
      rec_dic[rec_dig_sum(n)] = 1
    else:
      rec_dic[rec_dig_sum(n)] += 1
  
  return rec_dic

print(distr_of_rec_digit_sums())
print(distr_of_rec_digit_sums(0, 24))
print(distr_of_rec_digit_sums(5, 100))
print(distr_of_rec_digit_sums(20, 50))
print(distr_of_rec_digit_sums(1,5000))
