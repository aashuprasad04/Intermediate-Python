1. Default Arguments
2. Keyword Arguments
3. *args
4. **kwargs
5. Return Multiple Values
6. Variable Scope (LEGB Rule)
7. Recursion 


# 1. Default Arguments<br>
A Default Arguments is a fun parameter that has a default value. If you don't pass a value for that parameters whwen calling the function, python use the default.

#### Basic Syntax :
```py
def printName(name = "Guest"):
    print(f"hello {name}!")

printName("azy")        # hello azy!
printName()             # hello Guest!

```

# 2. Keyword Arguments<br>
- Normal (Positional) arguments : order matters here.
- But in Keyword Arguments order doesn't maater, all keyword argument safe.

#### Basic Syntax: 
```py
def PrintName(name , age):
    print(f"Name : {name} , Age : {age}")


PrintName(name="azy", age=19)
PrintName(age=20, name="roni")
```

# 3. *args<br>
- *args allows a function to accept any number or positional arguments.
- Is is not limited to numbers - you can pass
  - strings
  - lists
  - numbers
  - any type of data
- python stores all the value  in a tuple.

#### Example 01:
```py
def nums(*args):
    for a in args:
        print(a , end=" ")
    print()

nums(1,2,3,4 ,)     # Output ; 1 2 3 4 
nums("azy", "roni", "hezal")    # Output : azy roni hezal 
nums("azy", 19, "hezal", 17)    # Output : azy 19 hezal 17 

a = ("azy", 19, "harshit", 20)
nums(*a)    # Output : azy 19 harshit 20 
```

