filename = 'test.txt'
filename2 = 'test2.txt'

# Create a file and write in it
my_file = open(filename, 'x')
my_file.write('This is a test file.\nThis is the second line.\nThis is the third line.')
my_file.writelines(['This is a fourth line.', 'This is a fifth line.'])
my_file.write('\nThis is the sixth line.\n')
my_file.close()

# Have to close and re-open the file in read mode. 
my_file = open(filename, 'r')
print(my_file.read())

# readlines() puts the contents into elements of a list
my_file.seek(0)
contents = my_file.readlines()
print(contents)

my_file.close()

# Using with statement, we don't need explicit close()
with open(filename, mode = 'r') as filehandle:
    contents = filehandle.read()
    print(contents)

# Mode 'w+': write and read.
# Overwrite existing file or creates new one.
with open(filename2, mode = 'w+') as my_second_file:
    my_second_file.write('Wacka, wacka!')
    my_second_file.seek(0)
    print(my_second_file.read())

# Mode 'a': append
with open(filename2, 'a') as f:
    f.write('\nFozzy Bear was here.')

with open(filename2, 'r') as f:
    print(f.read())

# Delete the test files
import os
os.remove(filename)
os.remove(filename2)