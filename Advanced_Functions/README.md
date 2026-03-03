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
