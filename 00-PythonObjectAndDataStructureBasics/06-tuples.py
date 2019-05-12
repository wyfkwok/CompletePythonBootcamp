t = (1, 2, 3)
my_list = [1, 2, 3]

print(type(t))
print(type(my_list))

t = ('one', 2, 3.3)
print(t[-1])

# How many times is 'a' in the tuple?
t = ('a', 'a', 'b')
print(t.count('a'))

# Return index of the first time it appears
print(t.index('a'))
print(t.index('b'))

my_list[0] = 'NEW'
print(my_list)

# Tuples are immutable...cannot change.
# t[0] = 'NEW'