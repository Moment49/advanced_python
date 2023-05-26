from functools import reduce
from typing import Any
# 1 Python decorators
# def call_print(func):
#     """A function that calls another function"""
#     func()
    
# def print_text():
#     """Function to print a text"""
#     print("Hello World")

# call_print(print_text)

# 2 return function from another func
# def create_mult_x(x):
#     """Function to create an addition"""
#     def mult_y(y):
#         return x*y
#     return mult_y

# add = create_mult_x(10)

# print(add(10))

# 3 Decorators
def decor(func):
    def wrapper(*args, **kwargs):
        """A function to multiply"""
        print("Before the func")
        add_num = func(*args, **kwargs)
        # print(add_num)
        print("After the func")
        return add_num
    return wrapper


@decor
def add(a, b):
    """Function to add two numbers"""
    sum_a = reduce(lambda x,y: x+y, a)
    return sum_a + b

# add = decor(add(10))
# lis = [3, 4, 5]
# print(  add(lis, 6)  )
# print(add(10))

# Examples for decorators
# def invoice_decor(func):
#     def wrapper(*args):
#         """This is the wrapper function"""
#         print("***")
#         func(*args)
#         print("***")
#         print("END OF PAGE")
#     return wrapper


# @invoice_decor
# def invoice(num):
#     """Function to print an invoice"""
#     print(f"INVOICE# {num}")

# invoice(input("Enter an invoice num: "))


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.counter = 0
    def __call__(self, *args, **kwargs):
        print('Hello from call')
        self.counter += 1
        print(f"This is excuted {self.counter}")
        return self.func(*args, **kwargs)


@CountCalls
def print_name(name):
    print(f"Hello, {name}")

# cc = CountCalls(None)
# cc()    
print_name('Elvis')
print_name('Elvis')
print_name('Elvis')