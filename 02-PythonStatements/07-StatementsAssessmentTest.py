# 1. Use for, .split(), and if to create a Statement that will print out words that start with 's':
print('Answer to problem 1:')
st = 'Print only the words that start with s in this Sentence'

for word in st.split():
    if (word.startswith('s') or word.startswith('S')):
        print(word)

for word in st.split():
    if (word[0] == 's' or word[0] == 'S'):
        print(word)


# 2. Use range() to print all the even numbers from 0 to 10.
print('\nAnswer to problem 2:')
my_list = []
for x in range(0,11):
    if (x % 2 == 0):
        print(x)
        my_list.append(x)
print(my_list)

my_list = []
my_list = [x for x in range(0,11) if x %2 == 0]
print(my_list)

print(list(range(0, 11, 2)))


# 3. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print('\nAnswer to problem 3:')
my_list = []
my_list = [x for x in range(1, 51) if x % 3 == 0]
print(my_list)


#4. 
print('\nAnswer to problem 4:')
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
        if (len(word) % 2 == 0):
                print(word)


# 5. Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
print('\nAnswer to problem 5:')
my_list = []
for x in range(1,101):
    if (x % 3 == 0) and (x % 5 == 0):
        my_list.append('FizzBuzz')
    elif (x % 3 == 0):
        my_list.append('Fizz')
    elif (x % 5 == 0):
        my_list.append('Buzz')
    else:
        my_list.append(x)

for y in my_list:
    print(y)
    

# 6. Use List Comprehension to create a list of the first letters of every word in the string below:
print('\nAnswer to problem 6:')

st = 'Create a list of the first letters of every word in this string'
my_list = []
my_list = [x[0] for x in st.split()]
print(my_list)