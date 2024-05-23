obj = 42
obj = 'ABcd' # reassignment
obj.upper() # returns a copy
obj = obj.lower() # returns a copy
print(len(obj)) # returns an integer
obj = list(obj) # returns a list
obj.pop() # mutates
obj[2] = 'X' # mutates
obj.sort() # mutates
set(obj)
obj = tuple(obj) # reassignment