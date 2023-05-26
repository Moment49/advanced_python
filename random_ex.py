import random
import secrets
import numpy as np

# a = random.random()
# a = random.uniform(1, 10)
# a = random.randint(1, 10)
# a = random.randrange(1, 10)
# a = random.normalvariate(0, 1)
# print(a)

# mylist = ['A', 'B', 'C', 'D']
# a = random.choice(mylist)
# a = random.sample(mylist, 2)
# a = random.choices(mylist, k=3)
# random.shuffle(mylist)
# print(mylist)
# print(a)

# Secrets
# mylist = ['A', 'B', 'C', 'D']
# a = secrets.choice(mylist)
# print(a)
# a = secrets.randbelow(10)
# print(a)
# a = secrets.randbits(4)
# print(a)

# numpy
# a = np.random.rand(3, 3)
np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))

# a = np.random.randint(0, 10, (3, 4))
# arr = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])
# print(arr)
# np.random.shuffle(arr)
# print(arr)
# print(a)

