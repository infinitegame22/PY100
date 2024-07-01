pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()      # returns a dict_keys object
del pets['Dog']         # changes the dict_keys object
pets['Snake'] = 'Sssss'
print(keys)             # dict_keys(['Cat', 'Bird', 'Snake'])

