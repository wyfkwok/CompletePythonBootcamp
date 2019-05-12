# In VSCode, Ctrl+F5 to start without debug.

print("I'm going for a run")
print('I\'m going for a run')

print('hello \n world')

str_length = len('I am hungry')
print(str_length)

mystring = "Hello World"
print(mystring[1])
print(mystring[-1])

# Slicing
mystring = 'abcdefghijk'
print(mystring[2:])
print(mystring[:3])    # Up to, but not including position 3
print(mystring[3:7])   # Start at position 3.  Up to, but not including position 7
print(mystring[2:5])
print(mystring[::])
print(mystring[::2])   # Step size 2
print(mystring[::3])
print(mystring[2::2])
print(mystring[2:7:2]) # Start at 2.  Up to, but not including 7.  Step size 2.
print(mystring[::-1])  # From beginning to end, take a backward step size of -1.  A.k.a. reversing a string.

# String properties
name = 'Sam'
# name[0] = 'P'   # Will result in error.  Strings are immutable.

last_letters = name[1:]
print('P' + last_letters)

x = 'Hello World'
x = x + " it is beautiful outside!"
print(x)

letter = 'z'
print(letter * 10)

print(2 + 3)
print('2' + '3')

# String methods
x = 'Hello World'
print(x.upper())
print(x.lower())
print(x.split())

# Use split() to create a list out of a string
x = 'Hi this is a string'
print(x.split())
print(x.split('i'))

# Formatting strings
print('This is a string {}'.format('INSERTED'))
x = 'brown'
print('The {} is {} and {}'.format('fox', x,'quick'))
print('The {2} {1} {0}'.format('fox', x ,'quick'))
print('The {0} {0} {0}'.format('fox', x ,'quick'))
print('The {q} {b} {f}'.format(f='fox', b="brown", q='quick'))

result = 100/777
print(result)
print("The result was {}".format(result))
print("The result was {r:1.4f}".format(r = result))    # {value:width.precision f}
print("The result was {r:10.3f}".format(r = result))   # {value:width.precision f} more white space

result = 104.12345
print("The result was {r:1.5f}".format(r = result))
print("The result was {r:1.2f}".format(r = result))

# Formatted string literals, f-strings.  New to Python 3.6
name = 'Jose'
print(f'Hello, my name is {name}')
name = 'Sam'
age = 3
print(f"{name} is {age} years old")

num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
# With f-strings, precision refers to the total number of digits, not just those following the decimal.
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

# f-strings do not pad to the right of the decimal, even if precision allows it
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

# If this becomes important, you can always use .format() method syntax inside an f-string
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")