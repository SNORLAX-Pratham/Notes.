# **Python Notes**

## <p style="text-align: center;"> Index </p>

1. Basics Syntax
2. Comment
3. Variable
4. Data Types
5. Operators
6. Lists
7. Dictionaries
8. If...Else
9. While Loops
10. For Loops
11. Functions
12. Arrays
13. Classes/Objects

---

## Basics Syntex

Print

```
print= ("Hellow world")
```

Input

```
input("Ask input from user")

```

Length:Gives length of function

```
len()
```

Type: Give type of function

```
type("I am character")
```

---

## Commment

```
# or /* Multi Line comment */
```

---

## Variable

Whoes value can be changed

```
x= 13
y= apple
```

### _Casting a Variable_

```
x=int(3)
y=char("apple")

```

### _Assigning Multipal value to same variable_

```
x,y,z= apple, mango,banana
x,y,x= lion
```

---

## Data Type

Ways in which data can be stored
|Data Type|Code|Example|
|---|---|---|
|String|`str`|` x=("Hellow world")`|
|Integer|`int`|` x=45`|
|Float|`float`|` x=65.627`|
|Complex|`complex`|` x=4i`|
|Boolena|`bool`|` x=true`|

---

## Operators

### _Arithmatic operators_

| Operator    | Example |
| ----------- | ------- |
| Add         | x`+`y   |
| Substract   | x`-`y   |
| Multiply    | x`*`y   |
| Divide      | x`/`y   |
| Modulus     | x`%`y   |
| Exponential | x`**`y  |
| Qutiont     | x`//`y  |

### _Comparison Operator_

| Operator | Function              | Example |
| -------- | --------------------- | ------- |
| ==       | Equal to              | x`==`y  |
| !=       | Not Equal to          | x`!=`y  |
| >        | Greater than          | x`>`y   |
| <        | less than             | x'<'y   |
| >=       | Greater than equal to | x`>=`y  |
| <=       | less than equl to     | x`<=`y  |

### _Logical Operator_

| Operator | Example               |
| -------- | --------------------- |
| and      | x<5 and x<7           |
| or       | x<5 or x<3            |
| not      | not(x < 5 and x < 10) |

---

## List

```
list=[cats,dogs,lemur]
```

---

## Dictionaries

```
Dictionaries={
apple:fruit
ball:toy
}
```

## If-else

We can do nesting in the if else statement

```
if x<=12
    print("This is a condition")
elif
    print("another statement")
else
    print("This is a statement")

```

---

## While Loop

```
m=1
while n<100:
    m+=1
```

## For Loop

```
fruits=["Apple", "Banana", "mango"]
for fruit in fruits:
    print(fruit)
```

### ` break` to break from a loop

---

# Functions

def my_function():
print("Hi")
name=input("name")
print("Hi")
_Calling function_
` my_function()`

## Array

Arrays are used to store multiple values in one single variable

```
fruits=[apple,mango,banana]
```

---

## Classes

Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

```
class MyClass:
  x=5

```

### _**init**()_

The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in **init**() function
All classes have a function called **init**(), which is always executed when the class is being initiated.
Use the **init**() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

```
