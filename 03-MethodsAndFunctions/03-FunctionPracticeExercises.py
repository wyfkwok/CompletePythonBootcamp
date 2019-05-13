def lesser_of_two_evens(a, b):
    if (a % 2 == 0) and (b % 2 == 0):
        if a < b:
            return a
        else:
            return b
    elif a > b:
        return a
    else:
        return b

print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(5, 2))

def animal_crackers(word):
    two_words = word.split()
    if (two_words[0].lower())[0] == (two_words[1].lower())[0]:
        return True
    else:
        return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

def makes_twenty(x, y):
    if (x == 20) or (y == 20) or (x + y >= 20):
        return True
    else:
        return False

print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 4))
print(makes_twenty(-9, 20))

# *args and *kwargs (Arguments and Keyword Arguments)
# Arbitrary number of arguments
def my_func(*args):
    return(sum(args)) * 0.05

print(my_func(40, 60))
print(my_func(40, 60, 100))
print(my_func(40, 60, 100, 1))
print(my_func(40, 60, 100,1, 34))

print(my_func(40, 60, 100,1, 34))

def my_func2(*args):
    for item in args:
        print(item)

my_func2(40, 60, 100,1, 34)

def my_func3(**kwargs):
    # You can see that kwargs is just a dictionary
    print(kwargs)

    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit.')

my_func3(fruit='apple',veggie='lettuce')

# It is the ** that identifies the arbitrary number of key word arguments, not kwargs
def my_func4(**jelly):
    print(jelly)

my_func4(jam='grape',juice='cherry')

def my_func5(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))

# I would like 10 eggs
my_func5(10, 20, 30, fruit = 'orange', food = 'eggs', animal = 'dog', plant = 'flower')