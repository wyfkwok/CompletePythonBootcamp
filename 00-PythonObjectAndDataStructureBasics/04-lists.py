my_list = [1,2,3]
my_list = ['STRING',100,23.57]
print(my_list)
print(f'The length of my_list is {len(my_list)}')

my_list = ['one','two','three']
print(my_list[0])
print(my_list[1:])

another_list = ['four', 'five']
print(my_list + another_list)

# You can mutate elements in a list unlike a string
new_list = my_list + another_list
new_list[0] = new_list[0].upper()
print(new_list)

new_list.append('six')
print(new_list)

new_list.insert(len(new_list), 'seven')
print(new_list)

# Pop off the last item in the list
popped_item = new_list.pop()
print(popped_item)
print(new_list)

# Pop off item at index 0
popped_item = new_list.pop(0)
print(new_list)

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

new_list.sort()
print(new_list)

# print(new_list.sort()) returns None, not the printed sorted list
# The sort() method just sorts the new_list object, and 
# returns a None type.
# Same with the reverse() method

return_type = new_list.reverse()
print(new_list)
print(type(return_type))

x = None
print(Thtype(x))

