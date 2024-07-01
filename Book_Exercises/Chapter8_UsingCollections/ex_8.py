text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

for char in text:
    print(char)
    print(text.find(char))
    print(text.index(char))

