import math
int = 4936

print('The one place is', int % 10)
print('The tens place is', math.floor(int//10 % 10))
print('The hundreds place is', int // 100 % 10)
print('The thousands place is', int // 1000)