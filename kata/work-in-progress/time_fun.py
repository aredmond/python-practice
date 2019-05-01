import time


## Class implemention
class timer:
    """Class for timing function execution
    """
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    
    def __enter__(self):
        self.my_time = time.time()
        self.func(*self.args, **self.kwargs)

    def __exit__(self, exc_type, exc_val, exc_tb):
        current_time = time.time()
        time_elapsed = current_time - self.my_time
        print('Execution Time:', time_elapsed)

## Decorator implemention

def timer_decorator(func):
    start_time = time.time()
    def wrapper(*args, **kwargs):
        results =  func(*args, **kwargs)
        exec_time = time.time() - start_time
        print('Execution Time:', exec_time)
        return results
    return wrapper

@timer_decorator
def count_to_1000_decorated():
    """Function with no argument for timer validation
    """
    for x in range(1000):
        if not x % 100: 
            print(x)

@timer_decorator
def print_nums_decorated(range_num):
    """Function with an argument for timer validation
    """
    for x in range(range_num):
        if not x % 257: 
            print(x)

def count_to_1000():
    """Function with no argument for timer validation
    """
    for x in range(1000):
        if not x % 100: 
            print(x)

def print_nums(range_num):
    """Function with an argument for timer validation
    """
    for x in range(range_num):
        if not x % 257: 
            print(x)

print('*'*5,'class timer', '*'*40)
with timer(count_to_1000) as t:
    pass

with timer(print_nums, 10000) as t:
    pass
    
print('*'*5,'decorator timer', '*'*40)
count_to_1000_decorated()
print_nums_decorated(10000)