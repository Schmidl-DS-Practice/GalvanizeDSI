# the wikipedia example for a 4 number permutation shows a pattern of swapping 
# alternating between 1 swap 2 and 1 swap 3 done two times followed by 1 swap 2 
# and 1 swap 4 this pattern repeats with n swap 4 from 1 to 3 ending with one 
# final iteration of 1 swap 2 1 swap 3 1 swap 2 1 swap 3 1 swap 2

#first attempt will be recreate pattern from the 4 in wikipedia, i.e. p(4, 1) = 24

def swap_1_2(lis, count):
  lis_ = lis.copy()
  
  lis_[0] = lis[1]
  lis_[1] = lis[0]
  print(lis_)

  count += 1

  return lis_, count

def swap_1_3(lis, count):
  lis_ = lis.copy()

  lis_[0] = lis[2]
  lis_[2] = lis[0]
  print(lis_)

  count += 1

  return lis_, count

def swap_alternating(lis, count, length):
  for i in range(length - 2): #do it 2 times for both and one more of 1_2
    lis, count = swap_1_2(lis, count)
    lis, count = swap_1_3(lis, count)
  lis, count = swap_1_2(lis, count)

  return lis, count


def swap_n_last(lis, count, n, length):
  lis_ = lis.copy()

  lis_[n] = lis[-1]
  lis_[-1] = lis[n]
  print(lis_)

  count += 1

  return lis_, count 

def heaps(lis):
  length = len(lis)
  count = 0
  print(str(length)+'!')
  print(lis)
  for n in range(length): #will do the n_last swap 3 times
    lis, count = swap_alternating(lis, count, length)
    lis, count = swap_n_last(lis, count, n, length)
  print(count)

lis = ['a', 'b', 'c', 'd']
heaps(lis)