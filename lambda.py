from functools import reduce
# add10 = lambda x: x+10
# print(add10(5))

# # Multiple arg
# mult = lambda x, y: x*y
# print(mult(2, 5))

# Higher order functions
# points2D = [(1,2), (15, 1), (5, -1), (10, 4)]
# points2D_sorted = sorted(points2D, key=lambda x: x[1])

# print(points2D)
# print(points2D_sorted)

# map()
a = [1, 2, 3, 4, 5, 6]
a = map(lambda x: x*2, a)
print(list(a))

# filter()
a = [1, 2, 3, 4, 5, 6]
a = filter(lambda x: x%2== 0, a)
print(list(a))

# reduce()
a = [1, 2, 3, 4, 5, 6]
sum_a = reduce(lambda x, y: x+y, a)
print(sum_a)