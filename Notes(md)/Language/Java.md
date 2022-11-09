# Java Programming

# <p style="text-align: center;"> Index </p>

1. Intro
2. Download
3. Syntax
4. Datatypes
5. RULES FOR CODES
6. TAKING USER INPUT
7. FIVE GROUP OF OPERATOR
8. Preacedence and Associativity
9. BINARY NUMBER SYSTEM
10. String
11. Escape sequence
12. IF/ELSE/ELSE
13. Switch Statements
14. LOOPs
15. INTRODUCTION TO OBJECT ORRIENTED PROGAMMING(OOP)
16. Access modifier and constructors

---

## Intro

- Java is a popular programming language, created in 1995 by James Goslin.
- It is a purely object-oriented programming language
- (Object-Oriented programming (OOP) ( _programming that relies on the concept of classes and objects_. ).
- It is owned by Oracle, and more than 3 billion devices run Java.

> How does java work?

- Java is compiled into a byte code then it is interpreted into machine code.

**It is used for:**

1. Mobile applications (especially Android apps)
2. Desktop applications
3. Web applications
4. Web servers and application servers
5. Games
6. Database connection

> Why Use Java?

- It is easy to learn and simple to use
- It is open-source and free
- It is secure, fast, and powerful
  It has huge community support (tens of millions of developers)
- Java is an object-oriented language that gives a clear structure to programs and allows code to be reused, lowering development costs
- As Java is close to C++ and C#, it makes it easy for programmers to switch to Java or vice versa.

---

# Download Java

1. First go to the browser then download JDK (_java development kit=Collection of tools for developing and running java program_)
2. Download IDE (Integrated development environment )[ eg .Intelege Idea]a.k.a JRE=helps in execution of programs developed in java

---

# Syntax

The basic structure of the Java program

1. Package: they are a group of classes (package com.apple;)
2. <mark>public static void main(String[] args)</mark> _It is the entry point to an application_

### Naming convention

1. For class we use Pascal Convension ( first and subsequent letter must be capital eg:Main )
2. For function and variable we use Calmel Convention(here first letter is small and the subsequnt characters are uppercase Eg: main,myScanner

### Comment(//)

## Datatypes

(THESE ALL ARE CALLED PRIMITIVE DATA TYPE)
Just as we follow some rules in grammer in progamming we follow syntex to write code .

- A variable is a container which stores some value it can be changed as we need (it gets temprorily stored in computer).
- Java isstattically typed we need to define variable before we use it .
  > There are four major data type DATATYPE

### INTEGER DATA TYPE (INCREASING ORDER OF SIZE)

1. `(byte)` value range from -128 to 127 it can hold one byte
2. `(short)`It holds two byte
3. `(int)`it can hold 4 bytes
4. `(long)`it can hold 8 bytes

### CHARECTER DATATYPE

1. `(char)`for charecters; eg:apple,@

- it can old 2 bytes

### DECIMAL DATATYPE

1. `(floot)` it can old 4 bytes
2. `(double)`it can old 8 bytes

### BOOLEAN DATATYPE

1. `(bool)` true or false
   // In order to store value we need to first find which data type it belongs then find it min and max value

### Non premitive data type or Refrance data type

1. LITERALS : A constant value that can be assigned to a variable is call literal

- eg:boolean literal = false,
- character literal : 'A'
  > Long we need to put (L) eg : long =123456745678L

> For flote and double we need to add (f/F)for flote and for double(D/d) eg:101.1f, 1.4d

# RULES FOR CODES

1. insert (;) after every line
2. `Systeme.out.println ()` =print
3. whenever a brackets or cotes start it will end

### There are two type of type casting

TYPE CASTING[WIDENING]automatic
Type casting is when you want to assign value of one data type to another data type  
You can change any variable into any variable except (bool)
Code eg:
byte x=5;
int y=x;
System.out.println(y);
int k=4;
double p =k;

## MANUAL TYPE CASTING

When we have to manualy enter data its called manual type casting
code eg:
double mydouble=2.4554;
int myint=(int)mydouble;
System.out.println(mydouble);
System.out.println(myint);

## TAKING USER INPUT

Scanner

```
import java.util.Scanner;
Scanner sc= new Scanner(System.in);
int x=sc.nextInt();
```

# FIVE GROUP OF OPERATOR

1. **Arathamatic operator**

| Operator    | Example |
| ----------- | ------- |
| Add         | x`+`y   |
| Substract   | x`-`y   |
| Multiply    | x`*`y   |
| Divide      | x`/`y   |
| Modulus     | x`%`y   |
| Exponential | x`**`y  |
| Qutiont     | x`//`y  |

2. **Bitwise operator( work on bit )**
   {and =&,or=|,right shift=>> (value decreases by double),left shift=<<(value become double ){ IT WORKS ON BIT LEVEL} [ in bitwise operator both condition are checked ]

3. _Assignment operator_
   (assign value,= is also assignment operator )
   Operator | Function |
   | --- | ------|
   | = | x=y |
   | += | x=x+y |
   | -= | x=x-y |
   | *= | x=x*Y |
   | /= | x= x/y|
   | **= |x=x**Y |

4. **Comparison operator**

| Operator | Function              | Example |
| -------- | --------------------- | ------- |
| ==       | Equal to              | x`==`y  |
| !=       | Not Equal to          | x`!=`y  |
| >        | Greater than          | x`>`y   |
| <        | less than             | x'<'y   |
| >=       | Greater than equal to | x`>=`y  |
| <=       | less than equl to     | x`<=`y  |

5. **Logical operators**[sometime logical operator are also called boolean operator]

| Operator | Example              |
| -------- | -------------------- | --- | ----- |
| and      | x<5 `&&` x<7         |
| or       | x<5 `                |     | ` x<3 |
| not      | `!`(x < 5 && x < 10) |

---

## Preacedence and Associativity

> It basically tell which calculation work first

> **Precedence** :It says which equation is solved first
>
> eg:If there is a problem where there is both addition and multiplicatio then first multiplication is carried out then addition

> **Associativity** :It tells ;if there is same precidance equation
>
> eg:If there is both addition and division then weather it should go from left to right or right to left

_resulting data type after the arithamatic operation_

> Whenever we do any arithmatic operation in which we use multipal arithmatic operator then result satisfy both operator
>
> eg:If we do addition of int and flote we get flote

---

# BINARY NUMBER SYSTEM

{FROM BINARY TO>> DECIMAL}

EG. 1010

{ DECIMAL TO>>BINARY}

1.eg. 13 remove LCM

divide by2
||||
|--|--|--|
2|13|1
2|6 |0
2|3 |1
2|0 |1

2.start counting from downwards even include the last remender
13=1101

> How And Operation is stored in binary.

EG.

int a=4;

int b= 6;

int c=a&b;

System.out.println(c)

ans=4

For the given example first 4 is converted into binary _100_,and then 6 is converted into binary _110_

(TRUTH TABLE FOR & OPERATION)

| X   | Y   | AND                                                         |
| --- | --- | ----------------------------------------------------------- |
| 0   | 0   | 0                                                           |
| 0   | 1   | 0 BASICLY IF THERE IS ANY 0 THEN ITS AND OPERATOR IS ALSO 0 |
| 1   | 0   | 0                                                           |
| 1   | 1   | 1                                                           |

|     |     |     |
| --- | --- | --- |
| 1   | 0   | 0   |
| 1   | 1   | 0   |
|     |     |     |
| 1   | 0   | 0   |

> THERFORE THE AND (&) OPERATOR WILL STORE 4 BECAUSE THE ANS CAME 100

> FOR OR(|)OPERATOR HOW IT IS STORE

EG.

int a= 7;

int b=11;

int c=a|b:

System.oup.println(c)

ans=15

> For given example first 7 is converted into binary[0111],then11 is converted[1011]

( TRUTH TABLE FOR|OR OPERATION)
X|Y|OR|
|--|--|--|
0|1|1|
1|0|1 BASICLY IF THERE IS ANY 1 ITS OR OPERATOR IS ALSO 1|
0|0|0|
1|1|1|

|     |     |     |     |
| --- | --- | --- | --- |
| 0   | 1   | 1   | 1   |
| 1   | 0   | 1   | 1   |

---

|     |     |     |     |
| --- | --- | --- | --- |
| 1   | 1   | 1   | 1   |

THEREFORE THE OR (|)OPERATOR WILL STORE 15

# String

A string is a sequence of character
A string is started as follows
#string is a class but it can be used as premetive data type
#string is imutable it cannot be change but we can make new string

How to write string: String name = new String("pratham"); or String name = (" app")
**DIFFERENT WAY TO PRINT IN JAVA\***

1. System.out.println(); {print in new line}
   2.System.out.print(); {print in same line}
2. System.out.printf();for printing in use %d
   for float use %f
   for char use %c
   for string %s
   eg: System.out.printf("%d and %f",a,b);
3. System.out.format();

# STRING METHOD

String method operates on Java string. they can be used to find length of string ,covert into lower case etc.

1. `name.length()`:it is to find length of string

```
String a= ("Happy");
int b= a.length();
System.out.println(b);
```

2. `name.toLowerCase();` convert all capital letter into small letter

```
String name = ("HAPPY");
String ball = name.toLowerCase();
System.out.println(ball);
```

3. `name.toUpperCase()`:converts all samll letter to capital letter

```
String name = ("happy");
String ball = name.toLowerCase();
System.out.println(ball);
```

4. `name.trim()`:Spaces between the string is removed

```
String nonTrimmedString = " Pratham ";
nonTrimmedString.trim();
System.out.println(nonTrimmedString.trim());
```

5. `name.substring():` It give string the charecter that are associated with no till the end

```
String name = "Prathm";
System.out.println(name.substring(1));
```

{Here 1 is the start and if we put comma and antoher no it will be the end }\*index start from 0\

6. `name.replace `: It replace the char or int

```

String name = "Prathm";
System.out.println(name.replace(oldChr:'r',newChr:'t'));

```

7. `name.startsWith()/name.endsWith()`:{It basically says true or false weather name starts with the thing you wrote in bracket}

```
String name = "Pratham";
System.out.println(name.startsWith("Prat"));

```

8. `name.charAt()`:it give the charecter of the index at index which you put in bracket

```
String name = "Pratham";
System.out.println(name.charAt(3));

```

9. `name.indexOf()`: it basicaly returns the index of the thing you tiped in brackets

```
String name = "Pratham";
System.out.println(name.indexOf("P"));

```

10. `name.lastIndexOf()`: it gives last index where the last character is situated

```
String name = "Pratham";
System.out.println(name.lastIndexOf("a"));

```

11. `name.equals()`:it check wether he sname are equal or not (as String are case specific if the capital or small letter are o similar it will print falls)

```
String name = "Pratham";
System.out.println(name.equals("Pratham"));
```

12. `name.IgnoreCase()`:it egnores the letter is capital or small but it should be equal to the String

```
String name = "Pratham";
System.out.println(name.equalsIgnoreCase("prATham"));

```

---

## Escape sequence

Sequence of charrecter after "\"

- `n\`=new line
- `\t`= new tab
- `\"`=double cotation
- `\\`= backslash

# IF/ELSE/ELSE

1. `if:(condition){ }`
2. `if else: if(condition){ }else{ }`

## Relation ship operator in java

These are used to evaulate the condition

1. `==` equal to 2.` [!=]`not equal to 3.` >` 4.` <` 5.` <=` 6.`>=`

### NESTED IF ELSE STATEMENT

It is statement more if else statement in single statement

### TERNARY OPERATOR

a big code can be written in a small code
conditon?/condition?:
?=if
:=or

# Switch Statements

It is type of conditional statement .It is used when we have to make choices between multipal alternatives

```
switch(variable/ expression){
case value1:
//statements
beak;
case value2:
//satements
break; <<-- it use for if the any condition come true then another statement is not checked or work
...
default <<--it is use for if any of the condition is not true then this statement is run
//statements
}
```

---

# LOOPs

> loops are used when we want to repeate a set of statement again and again we use loops until a condition is satisfide

THERE ARE THREE TYPES OF LOOP

**1.for loop**

```
for(Statement1;Statement2;Statement3;){
code to be executed
}
```

- Statement1: initialisation,executed once
- Statement2: condition,check every time before th loop
- Statement3: reinitialisation,executed(every time)after the code block has been executed

```
for (int i=1;i<=4;i++){
System.out.println(i);
}
```

**2.while loop**
It keeps executing the code till the condition is true.If the condition is never false it will make an infinite loop

eg:

```
int i = 1;
while (i<=4){
System.out.println(i);
i++;
}
```

**3.do while loop:**
It is similler to while loop but here code is run and then the condition is checked.
eg:

```

int i = 0;do {
System.out.println(i);
i++;
}
while (i<=4);{
System.out.println(i);
}
```

---

# Array

> Arreay is the collection of similer type of data.The indexing of the array starts from 0., i.e 1st element will be stored at the 0th index, 2nd element at 1st index, 3rd at 2nd index, and so on.

```
int marks []= new int[3];{
marks[0]=52;
marks[1]=54;
marks[2]=13;
System.out.println(marks[1]);
```

There are three ways to write the array
here are three main ways to create an array in Java

1.  Declaration and memory allocation
    int [] marks = new int[5];

             1. Declaration and then memory allocation
             int [] marks;
             marks = new int[5];
             Initialization
             marks[0] = 100;
             marks[1] = 60;
             marks[2] = 70;
             marks[3] = 90;
             marks[4] = 86;

           1. Declaration, memory allocation and initialization together
            int [] marks = {98, 45, 79, 99, 80};

          marks[5] = 96; - throws an error
            System.out.println(marks[4]);
        }

}

### length of an array

To find length of an array we need to add marks.length

```
int marks []= {65,45,34,};
       System.out.println(marks.length);
```

### for each loop

eg:int marks []= {65,45,34,};

            System.out.println(marks.length);
            for(int element: marks){
            System.out.println(element);

Multidimensional array

A 2-D Array

```

int [][]house;
house = new int [2][3];
house[0][0] = 101;
house[0][1] = 102;
house[0][2] = 103;
house[1][0] = 201;
house[1][1] = 202;
house[1][2] = 203;

```

        System.out.println("Printing a 2-D array using for loop");
        for(int i=0;i<house.length;i++){
            for(int j=0;j<house[i].length;j++) {
                System.out.print(house[i][j]);
                System.out.print(" ");
            }
            System.out.println("");

# INTRODUCTION TO OBJECT ORRIENTED PROGAMMING(OOP)

OPP tries to map a code instructions to real making the code more short and simple

> What is opp?

It is solving a problem with object

> DRY:dont repete yourself:In progaming we dont repete the same code again and again but find the shortest code to solve the problem

**CLASS**:class is an blueprint to creat an object
**OBJECT**;an object is an initilazition of the class.
How to moddle a problem in OPP
Noun-->>class
Adjective -->>Attributes
Verb-->>Method

# OOP Terminology

1. **Abstraction:** It means hiding the internal detailes(show only essential information)
2. **Encapsulation :** Putting all the componants togeather(sensitive data is hidden)
3. **Inheritance:** The act of deriving new things from existing things
4. **Polymorphism:** One entity many forms
   > creat a custom class

`public class MY{it id; String name;}`

---

# Access modifier and constructors

**Access modifiers**:Access modifiers are keywords used to specify the accessibility of a class (or type) and its members.

> These are the key words

Four type of access modifier

1. private
2. default ,
3. protected
4. public

**getter and setter**

- **Getter** :Returns the value
- **Setter:** Sets value /update value

**constructures:** Member used to initilize a object in java while creating it

---

# Inheritance

- Inheritance is used to borrow properties and method from an existing class
- Declaring inheritance in java.Superclass, subclass( subclass extends to superclass)
