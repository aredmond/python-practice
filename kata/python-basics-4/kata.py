# Concepts for week 4

## Read and Write to files
"""
1. Create a `sample.txt` file with a couple lines in it.
2. Using the `with` statement open the file and store its contents to a variable, print it to the screen.
3. Write a new file `sample_write.txt` to the disk using python, make sure it has a min of 3 lines of text in it.
4. Use wget to pull down `https://releases.hashicorp.com/packer/1.4.0/index.json`, open it as a file and load it as a dict. HINT (import json and use json.load)
"""

# 1. See sample.txt
# 2.
with open('sample.txt') as f:
    sample_content = f.read()
print(sample_content)

# 3.
multi_line_str = """
This is one line
This is a second
and three is a charm
"""
with open('sample_writing.txt', 'w') as w:
    w.write(multi_line_str)

# 4.
import json
with open('index.json') as f:
    index_dict = json.load(f)
print(index_dict['builds'][0]['url'])

## Using *arg and **kwargs
"""
1. create a function with 2 arguments and 2 key word arguments
2. create a list of 2 sample arguments and a dict with 2 sample key pairs and unpack them into the function in step 1.
3. Create a function that takes `*arg` as a parameter, have the function add all arguments passed to it an output the result. Test the function with a list of ints unpacked with `*`
4. EXTRA: Create a function wrapper that takes a function, `*arg` and `**kwargs` as parameters then executes the function
5. EXTRA: Create a Class inheriting from a different class, call super in __init__ and pass `*arg` and `**kwargs`
"""

# 1.
def myfuction(a, b, c=14, d=55):
    print(str(a), str(b), str(c), str(d))

# 2.
arg_list = [12, 20]
kwarg_dict = {'c': 100, 'd': 200}

print('*'*40)
myfuction(1, 2)
print('*'*40)
myfuction(1, 2, c=3, d=4)
print('*'*40)
myfuction( *arg_list, **kwarg_dict)
print('*'*40)

# 3. 
def my_arg_function(*args):
    added_int = 0
    for arg in args:
        added_int += arg
    print(added_int)

list_of_ints = list(range(10,20))
my_arg_function(*list_of_ints)

## Lambda Expressions
"""
1. Write a simple lambda function takes one `int` argument and outputs its square x**2
2. Using a lambda in the return line create a function that returns a function, include one argument
3. In one line write a lambda and pass arguments
"""

# 1.
func = lambda x: x**2
print('lambda function:', func(4))

# 2.
def multiplier(n):
    return lambda x: x*n

doubler = multiplier(2)
mult_by_5 = multiplier(5)
print(doubler(10))
print(mult_by_5(50))

# 3.
(lambda x, y: print(f'{x} x {y} =', x*y))(4, 10)

## Try Except Blocks
"""
1. print a variable that does not exist to generate a NameError exception
2. Wrap the code in a Try Except block and print a string when the exception is thrown
3. Add a finally statement to the end of the block from step 2, have it print one more line.
"""

# 1.
#  print(thisIsNotAVar) <-- gen NameError

# 2.
try:
    print(thisIsNotAVar)
except:
    print('That var does not exist, sorry.')

print('*'*40)
# 3.
try:
    print(thisIsNotAVar)
except NameError as e:
    print('That var does not exist, sorry.')
finally:
    print('Maybe I should do something about that.')
    thisIsNotAVar= 'hat'