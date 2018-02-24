# Use the in keyword to iterate over an iterable

## Harmful Way

my_list = ['Vicky', 'Keer', 'VIKS']
index = 0
while index < len(my_list):
	print(my_list[index])
	index += 1


## Idiomatic Way

my_list = ['Vickee', 'Keer', 'Viks']
for element in my_list:
	print(element)
