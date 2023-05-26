# from collections import Counter
from collections import namedtuple
# from collections import OrderedDict
# from collections import defaultdict
# from collections import deque

# a = "aaaaaabbbbccc"
# my_counter = Counter(a)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# # print(my_counter.most_common(1)[0][0])
# print(list(my_counter.elements()))

# namedtuple
point = namedtuple('point', 'x,y')
print(point(1, 5))
# pt = point(1, -4)
# print(pt.x, pt.y)

# OrderedDict
# ordered_dict ={}
# ordered_dict['a'] = 1
# ordered_dict['c'] = 3
# ordered_dict['b'] = 2

# print(ordered_dict)

# DefaultDict
# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3

# print(d['a'])
# print(d['d'])

# deque
# d = deque()

# d.append(1)
# d.append(2)
# d.appendleft(3)
# print(d)

# d.pop()
# d.popleft()
# print(d)
# d.extend([4, 5, 6])
# print(d)

# d.rotate(1)
# print(d)