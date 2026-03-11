# zip() is used to combine elements from multiple iterables (lists, tuples, etc.) into pairs or tuples.
# It groups elements index by index.
# zip(iterable1, iterable2, ...)

list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd', 'e']

result = zip(list1,list2)
print(list(result))

# Multiple list

list4 = [1,2,3,4,5]
list5 = ['a', 'b', 'c', 'd', 'e']
list6 = ['A', 'B', 'C', 'D', 'D']

result1 = zip(list4, list5, list6)
print(list(result1))

# unzip
list3 =  [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

a, b = zip(*list3)
print(a)
print(b)


# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
# [(1, 'a', 'A'), (2, 'b', 'B'), (3, 'c', 'C'), (4, 'd', 'D'), (5, 'e', 'D')]
# (1, 2, 3, 4, 5)
# ('a', 'b', 'c', 'd', 'e')

