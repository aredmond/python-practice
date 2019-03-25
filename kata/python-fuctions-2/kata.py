# Fuctions Python Kata

## 1. Basics
"""
1. Create a empty function
2. Add a return statement
3. Add a argument
4. Add another argument with a default value
"""
# 1.
def empty_function():
    pass

# 2.
def function_with_return_2():
    str_to_return = "This is a {} sting.".format('fancy')
    return str_to_return

print(function_with_return_2())

# 3. 
def function_with_return_3(str_adjective): 
    str_to_return = "This is a {} sting.".format(str_adjective)
    return str_to_return

print(function_with_return_3('automated'))

# 4.
def function_with_return_4(str_adjective, end_phrase='This is the end.'):
    str_to_return = "This is a {} sting. {}".format(str_adjective, end_phrase)
    return str_to_return

print(function_with_return_4('longer'))
print(function_with_return_4('custom', end_phrase='THIS ENDING IS ALL CAPS!'))
print(function_with_return_4('custom', 'Python is smarter than my code.'))