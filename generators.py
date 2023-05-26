
import sys
# def my_generator():
#     yield 2
#     yield 3
#     yield 1
#     yield 4

# g = my_generator()
# # print(sum(g))
# print(sorted(g))

# # 1st yield value
# # value = next(g)
# # print(value)

# # # Next yield value
# # value = next(g)
# # print(value)

# # # 3rd next yield value
# # value = next(g)
# # print(value)

# # for i in g:
# #     print(i)

# # Another generator
# def countdown(num):
#     print("Starting...")
#     while num > 0:
#         yield num
#         num -= 1


# count_down = countdown(10)
# print(count_down)

# value = next(count_down)
# print(value)
# print(next(count_down))
# print(next(count_down))
# print(next(count_down))
# print(next(count_down))
# print(next(count_down))
# print(next(count_down))
# print(next(count_down))
# print(next(count_down))
# print(next(count_down))

# Example 
# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums


# def firstn_generator(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1

# # my_list = firstn(10)
# print(sys.getsizeof(firstn_generator(1000)))
# print(sys.getsizeof(firstn(1000)))

# print(next(my_list))
# print(sum(my_list))

# Fibonacci Spiral
def fibonacci(limit):
    a, b = 0, 1
    print(a, b)
    while a < limit:
        yield a
        a, b = b, a + b


x = fibonacci(13)
for i in x:
    print(i)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

#Generator Exp
