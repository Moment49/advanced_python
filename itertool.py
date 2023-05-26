# from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import count, cycle, repeat
from itertools import groupby
import operator

# a = [1, 2]
# b = [3]
# prod = product(a,b, repeat=2)
# print(list(prod))

# permutation
# a = [1, 2, 3]
# perm = permutations(a)
# print(list(perm))

# combinations
# a = [1, 2, 3, 4]
# comb = combinations(a, 1)
# print(list(comb))
# comb_wr = combinations_with_replacement(a, 2)
# print(list(comb_wr))

# Accumlate
a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=operator.mul)
acc = accumulate(a, func=max)
print(list(acc))

# Groupby
persons = [{'name': 'Tim', 'age': 23}, {'name': 'melvin', 'age': 33},
           {'name': 'john', 'age': 73}]


group_obj = groupby(persons, key=lambda x: x['age'])
for key, val in group_obj:
    print(key, list(val))

# a = [1, 2, 3, 4]
# group_obj = groupby(a, key=lambda x: x<3)
# print(group_obj)
# for key, val in group_obj:
#     print(key, list(val))

# Inifinity
a = [1, 2, 3]

# for i in cycle(a):
#     print(i)
    
# for i in count(10):
#     print(i)
# #     if i == 15:
#