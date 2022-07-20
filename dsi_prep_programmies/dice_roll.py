import random

def roll_any_dice(rolls, sides):
    counts = {num:0 for num in range(1, sides+1)}
    probs = {num:0 for num in range(1, sides+1)}
    total_rolls = 0
    for _ in range(1, rolls + 1):
        counts[random.randint(1, sides)] += 1
        total_rolls += 1
    for num,v in probs.items():
        probs[num] = counts[num]/total_rolls
    
    return counts, probs

print(roll_any_dice(100, 6))
#print('--------------------------')
#print(roll_any_dice(1000, 10))
#print('--------------------------')
#print(roll_any_dice(50, 12))
#print('--------------------------')
#print(roll_any_dice(70, 4))