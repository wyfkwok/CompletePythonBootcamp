# while test:
#     code statements
# else:
#     finale code statements

x = 0

while x < 5:
    print(f'The current value is {x}')
    x += 1    # No ++x or x++ in python because integers are immutable

# break:
# continue:
# pass:

x = [1, 2, 3]
for i in x:
    # If we  only have a comment in this loop, there will be an error.
    # Use 'pass' as a placeholder to not let python error.
    pass

# Example: continue
name = 'Sammy'
for letter in name:
    if (letter == 'a'):
        continue
    else:
        print(letter)

# Example: break
while (True):
    print('Yes!')
    break
