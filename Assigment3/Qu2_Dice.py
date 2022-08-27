import random
Sum = 0
while True:
    Dice = random.randint(1,6)
    Sum += Dice
    if Dice == 6:
        continue
    else:
       break
print('Total : ',Sum)