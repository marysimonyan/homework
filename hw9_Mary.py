"""
Homework 9
Mary Simonyan
"""

"""
problem 1
"""


def func(set1, i):
    if i in set1:
        set1.discard(i)
        return set1
    else:
        return set1


print(func({'1', '2', '3', '4'}, '5'))

"""
problem 2
"""
s1 = {'a', 'b', 'c', 'd'}
s2 = {'a', 'b', 'c', 'e', 'f'}

items = s1.intersection(s2)
ls = list(items)
s1 = s1.difference(s2)
s2 = s2.difference(items)
print(s1)
print(s2)

"""
problem 3
"""
test_list = [(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7)]

for i in test_list:
    if len(i) == 1:
        test_list.remove(i)
print(test_list)

"""
problem 4
"""
tuple1 = (1, 5)
tuple2 = (7, 2)

tup = []
for i in tuple1:
    for j in tuple2:
        tup += ((i, j), (j, i))

print(tup)

"""
problem 5
"""
tp = (4, 20)
print(float(str(tp[0]) + '.' + str(tp[1])))

"""
problem 6
incomplete
"""
list1 = [(4, 5, 20, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]


def func(i):
    return max(i)


list1.sort(func)
print(list1)


