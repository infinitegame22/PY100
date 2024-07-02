# falsy values
if None or False:
    print('None')
else:
    print('True')

if {} or [] or '' or () or set() or range(0):
    print('None')
else:
    print('True')

if 0 or 0.0 or 0j:
    print('None')
else:
    print('True')

