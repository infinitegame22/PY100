my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

my_list_iter = iter(my_list)
print(my_list_iter)

outer_index = 0
inner_index = 0

while outer_index < len(my_list):
  while inner_index < len(my_list[outer_index]):
    if my_list[outer_index][inner_index] % 2 == 0:
      print(my_list[outer_index][inner_index])
    inner_index += 1
  inner_index = 0
  outer_index += 1

