# add = lambda x: [i+1 for i in x]
nums = [1,2,3,4,5]
# print(add(nums))  # output : [2, 3, 4, 5, 6]

result = map(lambda x: x+1, nums)
print(tuple(result))


# map(function, iterable) applies the function to each element.
# It returns a map object (iterator). (result is a map object)
# You usually convert it using list(), tuple(), or loop through it.

nums = [97, 98, 99]
result = list(map(chr, nums))

print(type(result), result)
