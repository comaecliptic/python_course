while True:  
    triangle_sides = input(
        "Enter lengths of triangle sides separated by space. Type 'exit' to escape.\n"
    )
    if triangle_sides == 'exit':
        print('Goodbye!')
        break
    triangle_sides = [float(x) for x in triangle_sides.split()]
    print(triangle_sides)
    if len(triangle_sides) != 3:
        print('There must be exactly three sides!', end='\n\n')
        continue
    elif sum(triangle_sides) - max(triangle_sides) <= max(triangle_sides):
        print('Follow the Triangle Rule!', end='\n\n')
        continue
    triangle_sides_set = set(triangle_sides)
    if len(triangle_sides_set) == 1:
        print('This triangle is equilateral.', end='\n\n')
    elif len(triangle_sides_set) == 2:
        print('This triangle is isosceles.', end='\n\n')
    else:
        print('This triangle is scalene.', end='\n\n')
