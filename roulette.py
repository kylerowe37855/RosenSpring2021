import random
def roll():
    roll = []
    rednums = [1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36]
    blacknums = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,29,31,33,35]
    num = random.randint(0,36)
    roll.append(num)
    if num == 0:
        roll.append("green")
        return roll
    elif num in rednums:
        roll.append("red")
        return roll
    elif num in blacknums:
        roll.append("black")
        return roll

print(roll())
