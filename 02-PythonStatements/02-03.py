# if case1:
#     action1
# elif case2:
#     action2
# else:
#     action3

n = -2

if (n == 0):
    print(f"{n} is zero")
elif ((n % 2) == 0):
    print(f"{n} is even")
else:
    print(f"{n} is odd")


# for loops
my_list = [1, 2, 3]
for item in my_list:
    item *= 10
    print(item)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in my_list:
    if (num % 2):    # Notice 1 == True, 0 == False
        print(f'{num} is odd')
    else:
        print(f'{num} is even')

list_sum = 0
for num in my_list:
    list_sum += num
    print(f'The current sum is {list_sum}')
print(f'The total sum of the list is {list_sum}')

# Strings are just a list of letters, so lets inumerate through them
for letter in "Hawthorne":
    print(letter)

# _ is a commonly used if you don't intend to use the variable
for _ in "Hello":
    print("Cool!")

# Works for tuples too
tup = (1, 2, 3)
for item in tup:
    print(item)

# tuples in for loops
my_list = [(1,2), (3,4), (5,6), (7,8)]
print(f'The length of my_list is {len(my_list)}')
print("The tuples in my list are:")
for item in my_list:
    print(item)

print("---------")

# tuple unpacking
for (a,b) in my_list:
    print(a)
    print(b)

print("---------")

# It's more common to express the tuple without the parentheses
# in the for loop item
for a,b in my_list:
    print(a)

print("---------")

# Dictionary
d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
    print(item)

for key in d:
    print(d[key])

print("---------")

# Dictionary methods: .keys(), .values() and .items()
# Each of these methods return a dictionary view object

# Create a dictionary view object
print(d.items())

for k in d.items():
    print(k)

print("---------")

# Similar to tuple unpacking
# Get just the values
for key,value in d.items():
    print(value)

# Another way to get the values
for v in d.values():
    print(v)

# Here are the keys
for key in d.keys():
    print(key)


# If you want to obtain a true list of keys, values, or key/value tuples, you can cast the view as a list:
list_keys = list(d.keys())
print(list_keys)

print("---------")

# Remember dictionaries are unsorted.
# You may not get things back in the order you expect, especially with large dictionaries.
d = {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5, 'k6':6, 'k7':7, 'k8':8, 'k9':9, 'k10':10}
for value in d.values():
    print(value)

print(d.values())

# You can obtain a sorted list using sorted():
print(sorted(d.values()))