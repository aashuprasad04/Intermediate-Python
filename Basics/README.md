# Topic Covered
1. dictionary


## 1. dictionary<br>
- Dictionary is a built-in-data type that stores data in key-value pairs.
- Syntax:
  ```py
  dic = {key1: value1, key2: value2}
  ```
- Dictionary are
  - unordered
  - mutable
  - indexed by keys, which means you cna change their content after creation, and each key must be unique.

#### 1. Key feature of Python Dictionaries: 
- Key-Value pairs: Every item has a key and value.
   ```py
   my_dict = {"name": "Alice", "age": 25, "city": "New York"}
   ```
     - Key: "name", "age", "city"
     - Value: "Alice", 25, "New York"

#### 2. Mutable: you can add, remove, or update items:
  - add
    ```py
    myDic = {}
    print(myDic)    #Output = {} 

    myDic['name'] = "azy"
    print(myDic)    #Output =  {'name': 'azy'}

    myDic.update({'age':'19', 'city':'bihar'})
    print(myDic)    #Output = {'name': 'azy', 'age': '19', 'city': 'bihar'}
    ```

  - update
    ```py
    myDic = {'name': 'azy', 'age': '19', 'city': 'bihar'}
    print(myDic)    #{'name': 'azy', 'age': '19', 'city': 'bihar'}

    myDic['name'] = 'roni'
    print(myDic)    #{'name': 'roni', 'age': '19', 'city': 'bihar'}
    ```

- remove
  ```py
      myDic = {'name': 'azy', 'age': '19', 'city': 'bihar'}
      print(myDic)    #{'name': 'azy', 'age': '19', 'city': 'bihar'}

      removed_value1 = myDic.pop('name')
      print(removed_value1)   #   azy
      print(myDic)    #   {'age': '19', 'city': 'bihar'}


      # popitem() removes the last inserted key-value pair from a dictionary
      #  and returns it as a tuple (key,value)

      removed_value2 = myDic.popitem()
      print(removed_value2)   # ('city', 'bihar')
      print(myDic)    # {'age': '19'}

  ```
