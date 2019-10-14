list1 = [1, 2, 3]
list2 = [-3, 3, 13]
addition_list = []
for i, j in zip(list1, list2):
    addition_list.append(i + j)
print(addition_list)