# creation
groups_vocalists = {}

# filling with elements
groups_vocalists['Porcupine Tree'] = 'Steven Wilson'
groups_vocalists['Haken'] = 'Ross Jennings'
groups_vocalists['Opeth'] = 'Mikael Åkerfeldt'
groups_vocalists['Between the Buried and Me'] = 'Thomas Giles'
groups_vocalists['Riverside'] = 'Mariusz Duda'
groups_vocalists['Pink Floyd'] = ['Roger Waters', 'David Gilmour']
groups_vocalists['Tiamat'] = 'Johan Edlund'
groups_vocalists['Arena'] = 'Rob Sowden'

# element removal
del groups_vocalists['Porcupine Tree']
del groups_vocalists['Pink Floyd']

# element assessing
print(groups_vocalists['Between the Buried and Me'], end='\n\n')
groups_vocalists['Arena'] = 'Paul Manzi'

# iterating over elements
# first method
for group, vocalist in groups_vocalists.items():
    print(f'{group}: {vocalist}')
print('\n')

# second method
for group in groups_vocalists.keys():
    print(f'{group}: {groups_vocalists[group]}')
print('\n')

# third method
for group, vocalist in zip(groups_vocalists.keys(), groups_vocalists.values()):
    print(f'{group}: {groups_vocalists[group]}')
