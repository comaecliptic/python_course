elements = [1, 2, ('fruit', 5)]

# first method
back = elements[::-1]
print(back)

# second method
back = elements.copy()
back.reverse()
print(back)

# third method
back = []
for i in range(-1, -len(elements)-1, -1):
    back.append(elements[i])
print(back)