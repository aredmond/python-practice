### Define Vars
"""
1. Define a integer
2. Define a second integer
3. Print both integers
4. Type cast a integer variable from 1 or 2 into a float and print it.
"""
dog = 6
cat = 9
print(dog)
print(cat)
print(float(cat))


rock = 12
stone = 7
print(rock, stone)
print(float(rock))

### Use the following built in fuctions
"""
1. type()
2. print()
3. range()
4. int()
5. str()
6. float()
7. len()
"""


type(cat)
print(dog)
print(list(range(0,10)))
int(12.675)
str('kangaroo')
float(67)
len(["rabbits","cows","chickens","robots"])


print(type("cats")) # print type string
print(list(range(1,100,2))) # Print every other number from 1-100
int_as_string = str(15)
int_as_float = float(15)
float_as_int = int(3.14159)
print(len([1,4,19]))

### List Challenges
"""
1. Define a list with 1 string, 1 int and 1 float
2. Print the 3rd element of your list
3. Define a emply list
4. Reverse the order of the list from 1., do it 2 different ways
5. Create a list of numbers from 0-9
```
numlist = list(range(10))
```
6. Output only the first 3 elements of numlist
7. Output only the last 3 elements of numlist
8. Output every other element of numlist
9. Output numlist backwards
10. Loop through numlist and print every element
"""
multi_type_list = ['salmon',62,78.32]   #Define a list with 1 string, 1 int and 1 float
print(multi_type_list[2])   #Print the 3rd element of your list
empty_list = []             #Define a emply list
multi_type_list.reverse()   #Step 4
print(multi_type_list)      #Step 4
multi_type_list[::-1]       #Step 4
print(multi_type_list)      #Step 4
numlist = list(range(10))   #Create a list of numbers from 0-9
print(numlist)              #Create a list of numbers from 0-9
print(numlist[:3])          #Output only the first 3 elements of numlist
print(numlist[-3:])         #Output only the last 3 elements of numlist
print(numlist[::2])         #Output every other element of numlist
print(numlist[::-1])        #Output numlist backwards


### Dict Challenges
"""
1. Define a dict with 2 key pairs make sure one of the keys is 'fuel'
2. Print the value for key 'fuel' of the dict from 1.
3. Use help to find a built in function for dicts creates a set-like object with all the keys. hint help(dict1)
4. Define another dict with 2 or more key pairs
5. Add a key pair to the dictionary from step 4.
6. Define a empty Dict
7. Combine dicts from 1 and 2 into one new dict
8. Loop through all element of the dict from 2. and print the keys and values
"""
# 1.
dict1={
    "mileage": 32,
    "fuel": 23,
    "driver": "caleb"
}

# 2.
print(dict1['fuel'])
print(dict1.get("fuel"))

# 3.
help(dict1)  ## Looking for .keys()
dict1.keys()

# 4.
dict2={
    "age": 42,
    "gender": "M",
    "Name": "caleb"
}

# 5.
dict2['new_key'] = 'new_value'

# 6.
empty_dict={}

# 7.
dict3 = dict1.copy()
dict3.update(dict2)
# 7. another way
z = {**dict1, **dict2}
print(z)

# 8.
for key,val in dict2.items():
    print(key, "=>", val)


### Tuple Challenges
"""
1. Create a tuple with 3 elements
2. Create a list with the same elements as 1.
3. Append the same value to the list and the tuple showing how the append fails with the tuple
"""

# 1. 
tup = (1, 'cat', 13)
list1 = [1, 'cat', 13]
list1.append('cow')
tup.append('cow') ### ERROR
