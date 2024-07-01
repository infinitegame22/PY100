def check_if_3(list):
    for i in list:
        if i == 3:
            return True
    return False


numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(check_if_3(numbers1))
print(check_if_3(numbers2))
print(check_if_3(numbers3))
print(check_if_3(numbers4))
print(check_if_3(numbers5))

