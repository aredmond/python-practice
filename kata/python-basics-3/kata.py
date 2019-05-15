# Modules and Classes

## 1. Modules
"""
1. Create a python file named test_module.py
2. Add a function to the test_module file that takes one argument and prints it to the screen
3. Create a second python file (ill call the file module_consumer.py) and import the test_module, execute the function created in step 2
4. Add a dictionary with 2 key value pairs to test_module, call a value of the dictionary from the module_consumer script
5. Shorten the name of test_module during import in module_consumer
6. import the built in module datetime and print the time and date. Hint (datetime.datetime.now().ctime())
7. Using `from`, import only the datetime class under the datetime module
8. Import only the dictionary from step 4 and print a value
"""

# 1. See test_module.py
# 2. See test_module.py
# 3. 
import test_module

test_module.hello("Andrew")

# 4. See test_module.py
cat_name = test_module.cat_dict['name']
print(cat_name)

# 5. 
import test_module as tm
tm.hello("Fluffy")

# 6. 
import datetime

dt = datetime.datetime.now()
print(dt.ctime())
print(dt.date())
print(dt.year, dt.month, dt.day)

# 7. 
from datetime import datetime
dt = datetime.now()
print(dt.microsecond)

# 8.
from test_module import cat_dict
print(cat_dict['breed'])

## 2. Classes
"""
1. Create an empty class
2. Add an integer property to the class (use x as the variable name) [properties are just variables inside a class]
3. Create a object from the class and print the objects variable defined in step 2
4. Create a new class with a init function, have it take in two arguments and define those arguments as variables of the class
5. Like in step 3 create an object of the class and print both the variables
6. Add a function to the class from step 4 and call the function with a new object
7. Create a new class that inherits from the class in step 4, create a object and insure the inheritance took
8. Override the init function (do this to class from step 7)
"""

# 1.
class SampleClass:
    pass

# 2.
class SampleClass:
    x = 14

# 3.
sc1 = SampleClass()
print(sc1.x)

# 4.
class car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# 5. 
c1 = car("Honda", "Accord")
print(c1.make, c1.model)

# 6. 
class car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def print_car(self):
        print('Make:', self.make, 'Model:', self.model)

c2 = car('Subaru', 'Outback')
c2.print_car()

# 7. 
class honda(car):
    pass

h1 = honda('Honda', 'Civic')
h1.print_car()

# 8.
class subaru(car):
    def __init__(self, model):
        self.make = 'Subaru'
        self.model = model

s1 = subaru('Crosstrek')
s1.print_car()



