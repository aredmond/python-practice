# Functions, loops, and ifs Python Kata

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
    str_to_return = "This is a {} string.".format('fancy')
    return str_to_return

print(function_with_return_2())

# 3. 
def function_with_return_3(str_adjective): 
    str_to_return = "This is a {} string.".format(str_adjective)
    return str_to_return

print(function_with_return_3('automated'))

# 4.
def function_with_return_4(str_adjective, end_phrase='This is the end.'):
    str_to_return = "This is a {} string. {}".format(str_adjective, end_phrase)
    return str_to_return

print(function_with_return_4('longer'))
print(function_with_return_4('custom', end_phrase='THIS ENDING IS ALL CAPS!'))
print(function_with_return_4('custom', 'Python is smarter than my code.'))

## 2. If Basics

"""
1. Define the following
```
a = 24
b = 214
c = 0
```
2. Create a if statement that succeeds after comparing a and b, have it print something on success
3. Add an else if (elif) statement that DOES NOT execute after comparing a and c, have it print something as well.
4. Add an and statement to the if comparison that causes the if to fail (not execute) forcing the elif to be checked.
5. Add an or statement to the elif that will succeed
6. Add and else statement, change the values so that the else block is executed
7. Write an if that checks if the string "cat" is contained in the string "cats in hats".
8. Reverse 6 with a not and check for "bat" vs "cat"
9. Write a one line if else statement
"""

# 1. 
a = 24
b = 214
c = 0

# 2.
if a < b:
    print("A is less than B")

# 3.
if a < b:
    print("A is less than B")
elif a < c:
    print("A is less than C")

# 4.
if a < b and a > b:
    print("A is less than B")
elif a < c:
    print("A is less than C")

# 5.
if a < b and a > b:
    print("A is less than B")
elif a < c or c == 0:
    print("A is less than C or C is equal to 0")

# 6.
c = 1

if a < b and a > b:
    print("A is less than B")
elif a < c or c == 0:
    print("A is less than C or C is equal to 0")
else:
    print("Last Resort")

# 7.
if "cat" in "cats in hats":
    print("Its There!")

# 8.
if "bat" not in "cats in hats":
    print("Its Not There!")

# 9.
print("IF WORKED") if a < b else print("ELSE")
print("IF WORKED") if not a < b else print("ELSE")

## 3. Looping Basics

"""
1. Write a for loop using the range function and ensure 10 loops occur.
2. Finish the following code with a while loop, insure 10 loops
```
i = 0
## while goes here
    i += 1
    print(i)
```
3. Introduce an if statement that will cause the while to break (stop looping not error) after 3 loops
4. Change the if statement to issue a continue before the print statement for every other loop
"""

# 1.
for i in range(10):
    print(i)

# 2.
i = 0
while i < 10:
  i += 1
  print(i)

# 3.
i = 0
while i < 10:
    if i > 2:
        break
    i += 1
    print(i)

# 4.
i = 0
while i < 10:
    i += 1
    if (i % 2) == 0:
        continue
    print(i)