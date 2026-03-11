# reduce() is part of the functools module.
# reduce() repeatedly applies a function to elements of a list to produce a single result.

# from functools import reduce
# reduce(function, iterable)

# function → function with two arguments
# iterable → list, tuple, etc.
# It returns one final value


from functools import reduce 

List = [1,2,3,4,5]

result = reduce(lambda x,y : x+y, List)
print(result)   # Output : 15

# With Initial value
result1 = reduce(lambda x,y : x+y, List, 10)
print(result1)  # Output : 25
