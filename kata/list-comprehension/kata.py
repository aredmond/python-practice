###  Define Some lists
"""
1. Write the definition of a list comprehension in sud code
2. Break the definition down by rewriting it as a normal for loop
3. Expand number 1 and number 2 using conditionals
4. Define a list from 0 to 9 using a for loop
4b. Define a list from 0 to 9  using a list comprehension
5. Define a list of the squares of 0 to 9  using a for loop
5b. Define a list of the squares of 0 to 9  using a list comprehension
6. Do the same as number 5 but only add the even squares to the list using a for loop
6b. Do the same as number 5 but only add the even squares to the list using a list comprehension
"""

# 1.
values = [expression for item in collection]

# 2.
values = []
for item in collection:
    values.append(expression)

# 3.
values = [expression for item in collection if condition]

values = []
for item in collection:
    if condition
        values.append(expression)

# 4.
simple_list = []
for item in range(10):
    simple_list.append(item)

# 4b.
simple_list = [ item for item in range(10)]

# 5.
squares = []
for x in range(10):
    squares.append(x*x)

# 5b.
squares = [ x*x for x in range(10)]

# 6.
even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x*x)
# 6b.
squares = [ x*x for x in range(10) if x % 2 == 0]