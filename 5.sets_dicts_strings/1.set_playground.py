# creation
first_set = set()

# element adding
first_set.add(42)
first_set.add('sample_string')
first_set.add(True)

# set operations
second_set = {42, True, 'definitely_a_string'}
print(first_set.union(second_set))
print(first_set.intersection(second_set))
print(first_set.difference(second_set))
print(first_set.symmetric_difference(second_set))
print(second_set in first_set)
