name = input('Type your name: ')
age = int(input('Type your age: '))
height = float(input('Type your height in centimeters: '))

template1 = f'My name is {name:>10}.'
template2 = f'I am {age:3} years old.'
template3 = f'I am {height / 100:.2f} meters tall.'
table = f'|{name:^10}|{age:^4}|{height /100:^6.2f}|'

for t in [template1, template2, template3]:
    print(t)

print(table)
