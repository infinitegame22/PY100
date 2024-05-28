def number_range(integer):
    if integer in range(0, 51):
        print(f'{integer} is between 0 and 50')
    elif integer in range(51, 101):
        print(f'{integer} is between 51 and 100')
    elif integer > 100:
        print(f'{integer} is greater than 100')
    elif integer < 0:
        print(f'{integer} is less than 0')


number_range(50)
number_range(100)
number_range(1000)
number_range(-1)
