# range() operator
for i in range(10):
    print(i)
print("-------------------------")

# Start at 3
for i in range(3,10):
    print(i)
print("-------------------------")

# Steps of 2
for i in range(0, 10, 2):
    print(i)

# range()is a generator.
# Cast range to a list to use it.
my_list = list(range(0, 10, 2))
print(my_list)

index = 0
for letter in "abcde":
    print('At index {} the letter is {}'.format(index, letter))
    index += 1

index = 0
word = "abcdefg"
for letter in word:
    print(word[index])
    index += 1

# Example: enumerate
# We'll get back tuples
for item in enumerate(word):
    print(item)

for index,value in enumerate(word):
    print(f'Index {index}: Value {value}')

# Example: zip together two lists
my_list1 = [1, 2, 3, 4, 5]
my_list2 = ['a', 'b', 'c']
my_zipped = zip(my_list1, my_list2)

# This will print that you have a zip item in a memory space
print(my_zipped)

# Note: number of tuples is equal to the smallest list.
# The extra elements in the larger list are not used.
for item in my_zipped:
    print(item)

for item in zip(my_list1, my_list2):
    print(item)

my_list3 = [100, 200, 300]

for item in zip(my_list1, my_list2, my_list3):
    print(item)

# Again casting to list will make a list of tuples from zip
print(list(zip(my_list1,my_list2,my_list3)))

# Tuple unpack the zip
for a,b,c in zip(my_list1, my_list2, my_list3):
    print(b)


# Example: in operator
print('Is x in [1,2,3] ?')
if ('x' in [1, 2, 3]):
    print('True')
else:
    print('False')

# Is key1 in the dictionary?
print(('key1' in {'key1':1, 'key2':2}))

# Is 2 in the dictionary's values?
d = {'key1':1, 'key2':2}
print((2 in d.values()))

# Is 'key4' in the dictionary's keys?
print(('key4' in {'key1':1, 'key2':2, 'key3':3}.keys()))

# min and max functions
my_list = [10, 20, 30, 40, 50, 100]
print(min(my_list))
print(max(my_list))

# Import from random library the shuffle function
from random import shuffle

# Note: shuffle returns none, so don't use it for assignments (=)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(my_list)
print(my_list)

from random import randint

# Return random integer from 0 to 100
print('Here\'s a random number: {}'.format(randint(0, 100)))
print("-------------------------")

# User input
# Note: input is always considered a string!
num = input('Enter a number: ')
print(num)
print(type(num))

# Cast the input to the number type you want
print(float(num))
print(int(num))