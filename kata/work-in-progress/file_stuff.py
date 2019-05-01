import keyboard
from time import sleep

with open('sample_file.txt') as f:
    read_file = f.read()

print('*'*4, 'read:', '*'*40) 
print(type(read_file))
print(read_file)
print('*'*51) 

with open('sample_file.txt') as f:
    read_file_lines = f.readlines()

print('*'*4, 'readlines:', '*'*35) 
print(type(read_file_lines))
print(read_file_lines)
print('*'*51) 

"""
Create a genorator that spits one line of a file out at a time.
"""

## Basic Genorator

def my_gen(file_name):
    with open(file_name) as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

inter = my_gen('sample_file.txt')

## While input key is not x
## Must be root for this to work
while True:
    while True:
        if keyboard.is_pressed('x'):
            print("x pressed, stopping.")
            break
    print(next(inter))
    sleep(1)


    