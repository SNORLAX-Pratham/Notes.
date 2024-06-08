
# Python Notes

## <p style="text-align: center;"> Index </p>

## 1. Basics Syntax
## 2. Comment
## 3. Variable
## 4. Data Types
## 5. Operators
## 6. Lists
## 7. Dictionaries
## 8. If...Else
## 9. While Loops
## 10. For Loops
## 11. Functions
## 12. Arrays
## 13. Classes/Objects


## Basics Syntax

### Print
```python
print("Hello world")
```

### Input
```python
input("Ask input from user: ")
```

### Length: Gives length of function
```python
len("Example")
```

### Type: Give type of function
```python
type("I am a character")
```

---

## Comment

### Single line comment
```python
# This is a single line comment
```

### Multi-line comment
```python
'''
This is a
multi-line comment
'''
```

---

## Variable

### Whose value can be changed
```python
x = 13
y = "apple"
```

### Casting a Variable
```python
x = int(3)
y = str("apple")
```

### Assigning Multiple values to same variable
```python
x, y, z = "apple", "mango", "banana"
x, y, x = "lion", "tiger", "lion"
```

---

## Data Types

### Ways in which data can be stored

### String
```python
x = "Hello world"
```

### Integer
```python
x = 45
```

### Float
```python
x = 65.627
```

### Complex
```python
x = 4 + 1j
```

### Boolean
```python
x = True
```

---

## Operators

### Arithmetic operators
```python
x = 10
y = 5
print(x + y)  # Add
print(x - y)  # Subtract
print(x * y)  # Multiply
print(x / y)  # Divide
print(x % y)  # Modulus
print(x ** y) # Exponential
print(x // y) # Quotient
```

### Comparison Operator
```python
print(x == y)  # Equal to
print(x != y)  # Not Equal to
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to
```

### Logical Operator
```python
print(x < 5 and x < 7)
print(x < 5 or x < 3)
print(not(x < 5 and x < 10))
```

---

## List
```python
list_example = ["cats", "dogs", "lemur"]
```

---

## Dictionaries
```python
dictionaries_example = {
    "apple": "fruit",
    "ball": "toy"
}
```

---

## If-Else
```python
x = 10
if x <= 12:
    print("This is a condition")
elif x > 12:
    print("Another statement")
else:
    print("This is a statement")
```

---

## While Loop
```python
n = 1
while n < 100:
    print(n)
    n += 1
```

---

## For Loop
```python
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(fruit)
```

### Using `break` to exit from a loop
```python
for fruit in fruits:
    if fruit == "Banana":
        break
    print(fruit)
```

---

## Functions
```python
def my_function():
    print("Hi")
    name = input("Enter your name: ")
    print("Hi", name)
```

### Calling function
```python
my_function()
```

---

## Arrays

### Arrays are used to store multiple values in one single variable
```python
fruits = ["apple", "mango", "banana"]
```

---

## Classes

### Python is an object oriented programming language.
### Almost everything in Python is an object, with its properties and methods.
### A Class is like an object constructor, or a "blueprint" for creating objects.
```python
class MyClass:
    x = 5
```

### `__init__()`

#### To understand the meaning of classes we have to understand the built-in `__init__()` function.
#### All classes have a function called `__init__()`, which is always executed when the class is being initiated.
#### Use the `__init__()` function to assign values to object properties, or other operations that are necessary to do when the object is being created:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
