#  create a new tuple from(1, 2, 3, 4, 5). The new tuple should be in reverse order from the original. It should also exclude the first and last members of the original. The result should be the tuple(4, 3, 2).

tuple1 = (1, 2, 3, 4, 5)

list1 = list(tuple1)

reverse = list1.reverse()

print(list1)
list1.pop()
list1.remove(5)
print(tuple(list1))

