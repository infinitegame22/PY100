my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

string_list = []

for i in my_list:
    if i%2 == 0:
        string_list.append('even')
    else:
        string_list.append('odd')


print(string_list)

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd'

result = [ odd_or_even(number)
           for number in my_list ]
print(result)