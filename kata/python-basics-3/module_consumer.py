"""
Create a new class with a init function, have it take in two arguments and define those arguments as variables of the class
Like in step 3 create an object of the class and print both the variables
Add a function to the class from step 4 and call the function with a new object
"""


class myclass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x} {self.y}' 

    def print_stuff(tennis):
        print(f'{tennis.x} {tennis.y}')

mc = myclass(14, 19)
# mc.print_stuff()
print(mc)