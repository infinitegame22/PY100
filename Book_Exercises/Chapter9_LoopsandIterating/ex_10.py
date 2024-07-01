import random

def random_num(num):
    return random.randrange(num + 1)

highest = 10
number = random_num(highest)
print(number)

while number != highest:
    number = random_num(highest)
    print(number)

while True:
    number = random_num(highest)
    print(number)
    if number == highest:
        break


