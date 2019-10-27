s = 'agatacaca'

# first method
reverse_s = s[::-1]
print(reverse_s)

# second method
reverse_s = ''
for i in range(len(s) - 1, -1, -1):
    reverse_s += s[i]
print(reverse_s)
