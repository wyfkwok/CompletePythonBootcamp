# Write a brief description of all the following Object Types and Data Structures we've learned about:
#
# Numbers: Integers, floating point
#
# Strings:
# Strings are used in Python to record text information, such as name.
# Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence.
# For example, Python understands the string "hello' to be a sequence of letters in a specific order.
# This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).
# Strings are immutable, which means you cannot change their elements.
#
# Lists:
# Lists can be thought of the most general version of a sequence in Python.
# Unlike strings, they are mutable, meaning the elements inside a list can be changed!
#
# Tuples:
# In Python tuples are very similar to lists.
# However, unlike lists they are immutable meaning they can not be changed.
# You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar.
#
# Dictionaries:
# Key, value pairs.  Think of these Dictionaries as hash tables.
# That value can be almost any Python object.


# NUMBERS

# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25
num = 5 ** 2 * 4 / 2 + 55 - 4.75
print(num)


# Answer these 3 questions without typing code. Then type code to check your answer.
# What is the value of the expression 4 * (6 + 5) = 44
# What is the value of the expression 4 * 6 + 5  = 29
# What is the value of the expression 4 + 6 * 5 = 34
print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)

# What is the type of the result of the expression 3 + 1.5 + 4?  Float
print(type(3 + 1.5 + 4))

# What would you use to find a number’s square root, as well as its square?  Exponent
# square root: x ** .5
# square: X ** 2
print(4 ** .5)   # 2.0
print(5 ** 2)    # 25


# STRINGS

# Given the string 'hello' give an index command that returns 'e'.
s = 'hello'
print(s[1])

# Reverse the string 'hello' using slicing:
print(s[::-1])

# Given the string hello, give two methods of producing the letter 'o' using indexing.
print(s[-1])
print(s[4])

# Strings are immutable, so the following statement will fail.
# s[0] = 'y'


# LISTS

# Build this list [0,0,0] two separate ways.
# Method 1:
list1 = [0,0,0]
print(list1)

# Method 2:
list2 = [0]
list2.append(0)
list2.append(0)
print(list2)

# Method 3:
list3 = [0]*3
print(list3)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

# Sort the list
# Method 1:
list4 = [5,3,4,6,1]
list4.sort()
print(list4)

# Method 2:
list5 = [5,3,4,6,1]
print(sorted(list5))


# DICTIONARIES

# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
value = d['simple_key']
print(value)

d = {'k1':{'k2':'hello'}}
value = d['k1']['k2']
print(value)

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
value = d['k1'][0]['nest_key'][1][0]
print(value)

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
value = d['k1'][2]['k2'][1]['tough'][2][0]
print(value)

# Can you sort a dictionary? Why or why not?
# No! Normal dictionaries are mappings, not a sequence.


# TUPLES

# What is the major difference between tuples and lists?
# Tuples are immutable.  Lists are mutable.
# Tuples are in pairs.  Lists can be any number of elements.

# How do you create a tuple?
t1 = (2, 3)
print(t1)


# SETS

# What is unique about a set?
# Sets contain no duplicate elements

# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set5 = set(list5)
print(list5)
print(set5)
