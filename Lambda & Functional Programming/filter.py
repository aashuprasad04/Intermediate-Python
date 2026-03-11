# filter(function, iterable)

# function → a function that returns True or False (often a lambda)
# iterable → list, tuple, set, etc.


# filter() returns a filter object (iterator) in Python 3.
# Convert it to list() or set() to see values.
# Often used with lambda for short conditions.



List = [1,2,3,4,5]

result = list(filter(lambda x : x%2==0, List))
print(result)
