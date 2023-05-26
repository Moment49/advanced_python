myList = ['bananas', 'oranges','apples']
myList.append('lemon')
print(myList)

#Insert
myList.insert(1, 'blueberry')
print(myList)

# Remove pop()
item = myList.pop()
print(item)
print(myList)

# remove
myList.remove('oranges')
print(myList)

# sort
num = [4, 10, 3, 5, 2]
num.sort()
print(num)

# sorted
new_num = sorted(num)
print(new_num)

# concat
num_2 = [8, 43, 5, 2]
new_3 = num + num_2
print(new_3)