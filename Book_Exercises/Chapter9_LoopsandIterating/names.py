names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
# index = 0
#
# while index < len(names):
#     upper_name = names[index].upper()
#     upper_names.append(upper_name)
#     index += 1
#
# print(upper_names)
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']

for name in names:
    upper_name = name.upper()
    upper_names.append(upper_name)
    # Deleted: index += 1

print(upper_names);
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name == 'Max':
        continue

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names);
# ['CHRIS', 'KARIS', 'VICTOR']

