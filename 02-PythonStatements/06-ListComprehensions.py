# Brute force method
my_string = 'hello'
my_list = []

for letter in my_string:
    my_list.append(letter)

print(my_list)

# List Comprehension
# It's like a flattened out For loop
my_list = [letter for letter in my_string]
print(my_list)

my_list = [x for x in 'word']
print(my_list)

my_list = [x for x in range(0, 11)]
print(my_list)

# Square the numbers in the list
my_list = [num**2 for num in range(0, 11)]
print(my_list)

# Put only the even numbers in the list
my_list = [x for x in range(0, 11) if x % 2 == 0]
print(my_list)

celcius = [0, 10, 20, 34.5]
fahrenheit = [ ((9/5) * temp + 32) for temp in celcius ]
print(fahrenheit)

# If Else statement in List Comprehension
# It is NOT very readable!!!
# Sometimes List Comprehension is not the best method
result = [x if x % 2 == 0 else 'ODD' for x in range(0, 11) ]
print(result)

# This is much more readable!
result = []
for x in range(0, 11):
    if (x % 2 == 0):
        result.append(x)
    else:
        result.append('ODD')
print(result)


# Nested Loops in List Comprehension
my_list = []
my_list = [ x * y for x in [2, 4, 6] for y in [1, 10, 1000] ]
print(my_list)

# More readable version
my_list = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        my_list.append(x * y)
print(my_list)