def multiply(a, b):
    return a * b


first_num = input('Enter the first number: ')
second_num = input('Enter the second number: ')
print(f'{first_num} * {second_num} = {multiply(float(first_num), float(second_num))}')
