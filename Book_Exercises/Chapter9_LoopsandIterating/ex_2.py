age = int(input("What's your age? "))
print(f'You are {age} years old')
print()

for year in range(10, 50, 10):
    print(f'In {year} years, you will be '
          f'{year + age} years old.')


