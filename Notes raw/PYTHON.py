#Basics

print:It is a function that print(" ")
 input ():IT allows to input data
 len():It Gives length of function [EG -print(len(input("What is your name")))]
 type():It gives you type of fuction EG-print(type("hi"))

#!Data Types:Types of data that can be stored 

#?String: Charracter(Stored in Double Quotation)
x="apple"
#?Intrgers: Whole numbers
num =134
#?Flote: Decimal number
flot=13.145
#? F-String :you can insert variable into a string
days=365
print(f"there are {days}in year")

# !Arithmatic operators
# + ADD ,- Substract ,* Multiply /Divide,**Exponent

#!Functions

def my_function():
    print("Hi")
    name=input("name")
    print("Hi")
    #?Calling function 
    my_function()

#!Variable :It is giving a name to a function so that we can use as per our need        EG- 

name=input("What is your name")
    print(name)

#!If/else/and/or/not statement:When there is a condition we use such kind of statement             EG-

height=int(input("What is your height"))
if height>=120:
    print("You can enjoy the ride")
else: print("sorry you cant enter the ride")

#!NESTED IF/ELSE:Basically if else statement in another if else statmente               EG-

Height = int(input("Enter your height"))
Weight = int(input("Enter your Weight"))
BMI=float(Weight//Height**Height)
if BMI<=18.5:
    print("Under Weight")
elif BMI>=18.5<=25:
    print("Normal Weight")
elif BMI>=25<=30:
    print("Over Weight")
else:print("Obse")

#!And/Or/Not

#?AND
s=34
if s<35 and s>32 
print("hi")
#?OR
age=13
if age<16 or age>200
print("You can drive")
#?Not 
if not 3>2:
    print("Hi")

#!RANDOMNESS MODULE:It is the module to generate random                                EG-

import random
random_integer=random.randint(1,10)
print(random_integer)

#?IF you want to create your own module then make a file and import that module
import #*Name 

#!LISTS:In order to store data we need to have a list it make it easy to organize data  EG-

fruits=[item1,item2]
#*There id things in list check out  the list data structure type to know abot it

#!LOOPs:Thing that happen over and over again

#?While Loops:Keep repeting itself until statement is true
m=1
while n<100:
    m+=1

#?for loop-  EG-

fruits=["Apple", "Banana", "mango"]
for fruit in fruits:
    print(fruit)

#?BreakL:Break from a loop
 break
#?Continue
continue

#!Range
for number in range(a,b):
print (number)

#!Classes 
#?Creating a class in python
class MyClass:
#?Creating a object from a class
class fruit:
    pass    


