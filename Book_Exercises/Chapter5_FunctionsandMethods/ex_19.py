def remainders_5(numbers):
    return [number % 5 for number in numbers]


numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

# print(any(remainders_5(numbers_2)))     # True
# print(any(remainders_5(numbers_3)))     # False
# print(any(remainders_5(numbers_4)))     # False
# print(any(remainders_5(numbers_1)))     # True

print(all(remainders_5(numbers_1)))     # False
print(all(remainders_5(numbers_2)))     # True
print(all(remainders_5(numbers_3)))     # False
print(all(remainders_5(numbers_4)))     # True

print(remainders_5(numbers_1))          # [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0]
print(remainders_5(numbers_2))          # [1, 2, 3, 4, 1, 2, 3, 4]
print(remainders_5(numbers_3))          # [0, 0, 0]
print(remainders_5(numbers_4))          # []
