# List <br>
A List in Python is a collection data type used to store multiple values in a single variable.
- List is ordered
- List is changeable (mutable)
- List allow duplicate values
- List can store different data types

```py
List = [] # Empty List
List01 = [10,20,30,40]
print(List01)   # Output : [10, 20, 30, 40]

# Example with diff data types
List02 = [101, 'Aashu Prasad', '5.5', True]
print(List02)   # Output : [101, 'Aashu Prasad', '5.5', True]
```

```py
myList = []

# append
myList.append('apple')  #['apple']
myList.append('orange') #['apple', 'orange']

# extend
myList.extend([5,10])   #['apple', 'orange', 5, 10]

# insert :insert in a  Specific position
myList.insert(0, 1) #[1, 'apple', 'orange', 5, 10]

# remove
myList.remove('apple') #[1, 'apple', 'orange', 5, 10]

# pop : pop element via index if index are not available that are remove last element
myList.pop(2) #[1, 'orange', 10]
myList.pop()    # [1, 'orange']

# clear
myList.clear() #[]

# index() : get element index
myList.extend([1,2,2,3,4,5])  #[1, 2, 2, 3, 4, 5]
print(myList.index(2)) #1

# count()
print(myList.count(2)) # 2

# sort()
myList.sort()   #[1, 2, 2, 3, 4, 5]

# reverse()
myList.reverse()    #[5, 4, 3, 2, 2, 1]

# copy
myList01 = myList.copy()
print(myList01) #[5, 4, 3, 2, 2, 1]

print(len(myList))  #6
print(max(myList))  #5
print(min(myList))  #1
print(sum(myList))  #17


print(myList)

```
