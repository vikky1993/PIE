# Use the enumerate function in loops instead of creating an “index” variable
##Harmful Way
my_container = ['Vikky', 'Keer', 'VIKS']
index = 0
for element in my_container:
	print('{} {}'.format(index, element))
	index += 1



##Idiomatic Way

my_container = ['Vikky', 'Keer', 'VIKS']
for index, element in enumerate(my_container):
	print('{} {}'.format(index, element))