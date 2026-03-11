add= lambda a,b : a+b
print(add(5,6))

# lambda fun is a single line fun without a name, create using the lambda keyword

# add= lambda a,b : a+b
# add = fun name
# lambda = keyword
# a,b = parameters
# a+b = statement


Aprint = lambda a: print(a)
Aprint("azy")

add = lambda x: [i+1 for i in x]
nums = [1,2,3,4,5]
print(add(nums))  # output : [2, 3, 4, 5, 6]
