def say_hello():
    '''
    DOCSTRING: This is where the function's Document String (docstring) goes
    '''
    print('hello')

say_hello()

def greeting(name):
    print('Hello %s' %(name))

greeting('Jose')

# Default value of parameter
def greeting2(name = 'Jesus'):
    print('Hello %s' %(name))

greeting2()
greeting2('Sally')


def greeting3(name = 'NAME'):
    return 'Hello ' + name

print(greeting3())
result = greeting3('Scrouge McDuck')
print(result)

# Find out if the word "dog" is in a string
def dog_check(mystring):
    # if 'dog' in mystring.lower():
    #     return True
    # else:
    #     return False

    # Better way
    return 'dog' in mystring.lower()

print(dog_check('Woof dog'))
print(dog_check('Dog ran away!'))


def add_num(num1, num2):
    return num1 + num2

print(add_num(4, 5))

print(add_num('one', 'two'))


def is_prime(num):
    '''
    Naive method to check if prime
    INPUT:  number
    OUTPUT: string stating number is or is not a prime
    '''
    for n in range(2, num):
        if num % n == 0:
            print(num, ' is not a prime')
            break
    # Note how the else lines up under for and not if.
    # This is because we want the for loop to exhaust all
    # possibilities in the range before printing our number is prime.    
    else:   # If never mod zero, then prime
        print(num, ' is prime!')

is_prime(113)


#==========
# Better prime function
# Returns True if prime or False if not a prime
#==========
import math

def is_prime2(num):
    '''
    Better method of checking if num is a prime.
    '''
    if num % 2 == 0 and num > 2:
        return False

    for i in range (3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True

print(is_prime2(18))

def pig_latin(word):
    first_letter = word[0]

    # Check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + word[0] + 'ay'

    return pig_word

print(pig_latin('fuck'))