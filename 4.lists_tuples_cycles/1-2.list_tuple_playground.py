# list manipulations
# creation
my_list = []
# adding elements
my_list.append(1)
my_list.append('element')
my_list.append(True)
# concatenation with another list
my_list += [False, 'another_element', 13]
# removing elements
my_list.remove(False)
my_list.remove('another_element')
# changing elements
my_list[1] = 10
# counting element appearances
print(my_list.count(42))
# counting list length
print(len(my_list))

# tuple manipulations
# creation
my_tuple = (1, 'element', True)
# counting element appearances
print(my_tuple.count('element'))
# counting tuple length
print(len(my_tuple))