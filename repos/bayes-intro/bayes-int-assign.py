import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#Part1
#1: the probability of choosing a die. 1/5 = 0.20

#2: the probability of rolling a value on the n-sided die given
#choosing a die with probability 0.20

#3: probabiliy you picked n-sided die | rolled an 8
#p_8 = (1/5)*0 + (1/5)*0 + (1/5)*(1/8) + (1/5)*(1/12) + (1/5)*(1/20)
#p_four_give_eight = 0 '''p(4)p(8|4)/p(8)'''
#p_six_give_eight = 0 '''p(6)p(8|6)/p(8)''' 
#p_8_give_eight = ((1/8)*(1/5)) / p_8 '''p(8)p(8|8)/p(8)'''
#p_12_give_eight = ((1/12)*(1/5)) / p_8 '''p(12)p(8|12)/p(8)'''
#p_20_give_eight = ((1/20)*(1/5)) / p_8'''p(20)p(8|20)/p(8)'''

#4: the proportion would be different. the prob of one die would be quite low.
#while the prob of another die would be quite high

#5: the second because it would allow you to eliminate two of the dice.

#6:
# p_4 = 0.08
# p_6 = 0.12
# p_8_ = 0.16
# p_12 = 0.24
# p_20 = 0.40
# p_8 = (p_4)*0 + (p_6)*0 + (p_8_)*(1/8) + (p_12)*(1/12) + (p_20)*(1/20)

# p_four_give_eight = 0
# p_six_give_eight = 0
# p_eight_give_eight = ((1/8*(p_8_)) / p_8) 
# p_12_give_eight = ((1/12)*(p_12) / p_8)
# p_20_give_eight = ((1/20)*(p_20) / p_8)

#all three die have an equal chance. When they were all a 1/5 chance the 8-sided
#die was more likely.

#7: 
