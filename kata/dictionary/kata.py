import random

## Create a dictionary with the letters as the keys and numbers as the values
## in deceding order list this: {"a": 26, "b": 25, "c": 24 ..., "z": 1}
def create_dict_from_string(str_seed, is_random=False):
    numOc = len(str_seed) # Number of chars in str_seed
    if is_random:
         list_of_random_numbers = random.sample(range(1, numOc+1), numOc)
         return dict(zip(str_seed, list_of_random_numbers))
    else:
        list_of_nums = [i for i in range(numOc, 0, -1)]
        return dict(zip(str_seed, list_of_nums))

sample_dict = create_dict_from_string("abcdefghijklmnopqrstuvwxyz", is_random=True)
print(sample_dict)

# Sort the dictionary by value and only print the first 10 elements
print("First sort using dict.get as key")
sorted_sample_dict = sorted(sample_dict, key=sample_dict.get, reverse=True)
for e in sorted_sample_dict[:10]:
    print(e, sample_dict[e])

# Way number 2
print("Second sort using lambda x: x[1] as key")
sorted_sample_dict_2 = sorted(sample_dict.items(), key=lambda x: x[1], reverse=True)
for e in sorted_sample_dict_2[:10]:
    print(e[0], e[1])

# Sort by key
print("Sort by key")
sorted_sample_dict_3 = sorted(sample_dict)
for e in sorted_sample_dict_3[:10]:
    print(e, sample_dict[e])

# dict3 = dict1.copy()
# dict3.update(dict2)
# # 7. another way
# z = {**dict1, **dict2}
# print(z)

# # 8.
# for key,val in dict2.items():
#     print(key, "=>", val)
