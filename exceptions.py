# # Errors
# # a = 5 + '10' 
# # print(a)
# # a = 4
# # b = 0
# # print(a/b)

# # raising any expection
# x = 5
# # if x < 0:
# #     raise Exception('x should be positive')
# assert(x >= 0), 'x is not poisitive'

# # catching an error
# try:
#     a = 5/0
#     b = 2 + 3
#     print(a)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)

# # except ZeroDivisionError:
# #     print('An error occured')
# else:
#     print("everything is fine")
# finally:
#     print("cleaning up...")

class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_val(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooSmallError('Value is too small', x)
    
try:    
    test_val(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)