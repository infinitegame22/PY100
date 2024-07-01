info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

print(info.replace(':', '+'))
print(info)

parts = info.split(':')
result = '+'.join(parts)
print(result)

