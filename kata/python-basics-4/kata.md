# Concepts for week 4

* Read and Write to files
* Using *arg and **kwargs
* Lambda Expressions
* Try Except Blocks

# Week 4

## Read and Write to files

1. Create a `sample.txt` file with a couple lines in it.
2. Using the `with` statement open the file and store its contents to a variable, print it to the screen.
3. Write a new file `sample_write.txt` to the disk, make sure it has a min of 3 lines of text in it.
4. Use wget to pull down `https://releases.hashicorp.com/packer/1.4.0/index.json`, open it as a file and load it as a dict. HINT (import json and use json.load)


## Using *arg and **kwargs

1. create a function with 2 arguments and 2 key word arguments
2. create a list of 2 sample arguments and a dict with 2 sample key pairs and unpack them into the function in step 1.
3. Create a function that takes `*arg` as a parameter, have the function add all arguments passed to it an output the result. Test the function with a list of ints unpacked with `*`
4. EXTRA: Create a function wrapper that takes a function, `*arg` and `**kwargs` as parameters then executes the function
5. EXTRA: Create a Class inheriting from a different class, call super in __init__ and pass `*arg` and `**kwargs`

## Lambda Expressions

1. Write a simple lambda function takes one `int` argument and outputs its square x**2
2. Using a lambda in the return line create a function that returns a function, include one argument


## Try Except Blocks

1. print a variable that does not exist to generate a NameError exception
2. Wrap the code in a Try Except block and print a string when the exception is thrown
3. Add a finally statement to the end of the block from step 2, have it print one more line.


