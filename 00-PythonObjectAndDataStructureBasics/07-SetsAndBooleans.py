# Sets are unordered collections of unique elements

my_set = set()
my_set.add(1)

print(my_set)

my_set.add(2)
print(my_set)

# Sets only accept unique values.  Will not add 2 again.
my_set.add(2)
print(my_set)

my_set.add('2')
print(my_set)

my_list = [4, 4, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3]

# Cast the list as a set.
# It may look like they are in order, but sets really have no order.
x = set(my_list)
print(x)

# Turn the string into a set of unique letters
print(set('Mississippi'))

# Booleans bitches!

print(type(True))
print(type(False))

# We can use None as a placeholder for an object that we don't want to reassign yet
b = None
print(b)
print(type(b))


