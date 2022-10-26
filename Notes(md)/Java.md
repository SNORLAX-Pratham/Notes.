                                                Java Programming

Java is a popular programming language, created in 1995 by James Goslin. It is a purely object-oriented programming language (Object-Oriented programming (OOP) is a programming paradigm that relies on the concept of classes and objects. ). It is owned by Oracle, and more than 3 billion devices run Java.

How does java work?
Java is compiled into a byte code then it is interpreted into machine code

It is used for:

1. Mobile applications (especially Android apps)
2. Desktop applications
3. Web applications
4. Web servers and application servers
5. Games
6. Database connection

Why Use Java?
Java works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc.)
It is one of the most popular programming languages in the world
It is easy to learn and simple to use
It is open-source and free
It is secure, fast, and powerful
It has huge community support (tens of millions of developers)
Java is an object-oriented language that gives a clear structure to programs and allows code to be reused, lowering development costs
As Java is close to C++ and C#, it makes it easy for programmers to switch to Java or vice versa.

How to download java

1. First go to the browser then download JDK (java development kit=Collection of tools for developing and running java program )
2. then download IDE (Integrated development environment )[ eg .Intelege Idea]a.k.a JRE=helps in execution of programs developed in java

The basic structure of the Java program

1. package: they are a group of classes (package com.apple;)
2. public static void main(String[] args) It is the entry point to an application

**Naming convention **

1. for class we use Pascal Convension ( first and subsequent letter must be capital eg:Main )
2. for function and variable we use Calmel Convention(here first letter is small and the subsequnt characters are uppercase Eg: main,myScanner
   **Comment**\*****
   whenever you put (//) it get comment the program does not run . In computer programming, a comment is a programmer-readable explanation or annotation in the source code of a computer program. They are added with the purpose of making the source code easier for humans to understand, and are generally ignored by compilers and interpreters. Multi line comments in Java start with /_ and end with _/. You can comment multiple lines just by placing them between /_ and _/.

DATA TYPES(THESE ALL ARE CALLED PRIMITIVE DATA TYPE)
just as we follow some rules in grammer in progamming we follow syntex to write code .A variable is a container which stores some value it can be changed as we need (it gets temprorily stored in computer). Java isstattically typed we need to define variable before we use it . There are four major data type 1:INTEGER DATA TYPE 2:CHARECTER DATATYPE 3: DECIMAL DATATYPE 4: BOOLEAN DATATYPE
@INTEGER DATA TYPE (INCREASING ORDER OF SIZE)
1.(byte)
value range from -128 to 127 it can hold one byte 2. (short)
It holds two byte
3.(int)
it can hold 4 bytes
4.(long)
it can hold 8 bytes
@CHARECTER DATATYPE
1.(char)for charecters; eg:apple,@
it can old 2 bytes
@DECIMAL DATATYPE
1.(floot) for
it can old 4 bytes
2.(double)
it can old 8 bytes
@BOOLEAN DATATYPE
1.(bool) for statement is true or false
// In order to store value we need to first find which data type it belongs then find it min and max value
[non premitive data type or refrance data type]
LITERALS : A constant value that can be assigned to a variable is call literal
eg:boolean literal = false,character literal : 'A'
for byet, short, int they are the key word but for long we need to put (L) eg : long =123456745678L;{ if we not put L it will be bye default be an integer }
for flote and double we need to add (f/F)for flote and for double(D/d) eg:101.1f, 1.4d
for character we need to add (' ') eg: char = 'happy'
for string literal we put (" ")
READING DATA FROM KEYBOARD: In order to read data from keyboard JAVA has scanner class .
Scanner S = new scanner (System.in);

********************\*\*\*********************RULES FOR CODES************************\*\*************************
1.insert (;) after every line
2.Systeme.out.println () =print
3.whenever a brackets or cotes start it will end

There are two type of type casting

TYPE CASTING[WIDENING]automatic
Type casting is when you want to assign value of one data type to another data type  
You can change any variable into any variable except (bool)
Code eg:
byte x=5;
int y=x;
System.out.println(y);
int k=4;
double p =k;

**********\***********MANUAL TYPE CASTING**********************\*\*\*\***********************
When we have to manualy enter data its called manual type casting
code eg:
double mydouble=2.4554;
int myint=(int)mydouble;
System.out.println(mydouble);
System.out.println(myint);

TAKING USER INPUT
Scanner

1. import java.util.Scanner;
   2.Scanner sc= new Scanner(System.in);
   3.int x=sc.nextInt();
   code eg:
   @SuppressWarnings("resource")
   Scanner sc = new Scanner(System.in);
   int principal= sc.nextInt();
   float rate = sc.nextFloat();
   int time= sc.nextInt();
   float simpleIntrest=principal*rate*time/100;
   System.out.println("the simple intrest is"+simpleIntrest);

********\*********FIVE GROUP OF OPERATOR******************\*\*\*\*******************
1.Arathamatic operator(for +-_)
[+]=addition
[-]=substraction
[_]= multiplication
[/]= division
[%]=it gives remainder 2. Bitwise operator( work on bit ){and =&,or=|,right shift=>> (value decreases by double),left shift=<<(value become double ){ IT WORKS ON BIT LEVEL} [ in bitwise operator both condition are checked ] 3. Assignment operator(assign value,= is also assignment operator ) 4. Comparison operator(VIP,use for comparison, there are 6types of comparison operator,they give boolien data type i.e.true or false ){while using = then use it two time because =is an assignment operator}

1. [==] equal to
   2.not equal to[!=]
   3.>
   4.<
   5.<=
   6.>=

5.Logical operators[sometime logical operator are also called boolean operator]
1.{&&}( AND) :if any one is false then then the condition is false
2.{ || }(OR): if any one is true then the condition is true
3.!(NOT): if we assign not to true then it will be false vice versa

**\***Preacedence and Associativity\*\*\*(It basically tell which calculation work first )
Precedence :It says which equation is solved first eg:if there is a problem where there is both addition and multiplicatio then first multiplication is carried out then addition
Associativity :It tells ;if there is same precidance equation eg; if there is both addition and division then weather it should go from left to right or right to left

**\***resulting data type after the arithamatic operation**\***

Whenever we do any arithmatic operation in which we use multipal arithmatic operator then result come in form in which both operator can come
eg:If we do addition of int and flote we get flote
NOTE:addition of boolean or caracter in arithamatic operator show nothing or error \***\*Increment and decrement**\*****
to adby one we can do i by (++b)or sustrating by one (--a)
eg: int a=45;
System.out.println(a++);
int b=a\*2;
System.out.println(b);

********\*\*\*\*********BINARY NUMBER SYSTEM****************\*****************

{FROM BINARY TO>> DECIMAL}
EG. 1010
1.start counting them from right hand side like0(0)1(1)0(2)1(3)
2.multiply binary digit by 2raise to the power of the count EG.0*2^0+1*2^1+0*2^2+1*2^3=10

{ DECIMAL TO>>BINARY}

1.eg.13 remove LCM
divide by2

2|13|1
2|6 |0
2|3 |1
2|0 |1

2.start counting from downwards even include the last remender
13=1101

{FOR (&AND) OPERATION HOW IT IS STORE}

EG.int a=4;
int b= 6;
int c=a&b;
System.out.println(c)
ans=4

for the given example first 4 is converted into binary[100],and then 6 is converted into binary[110]
(TRUTH TABLE FOR & OPERATION)
X |Y|AND
0 |0 |0
0 |1 |0 BASICLY IF THERE IS ANY 0 THEN ITS AND OPERATOR IS ALSO 0
1 | 0|0
1 |1 |1

1|0|0
1|1|0

---

1|0|0
THERFORE THE AND (&) OPERATOR WILL STORE 4 BECAUSE THE ANS CAME 100

{FOR [OR|]OPERATOR HOW IT IS STORE}
EG.int a= 7;
int b=11;
int c=a|b:
System.oup.println(c)
ans=15

for given example first 7 is converted into binary[0111],then11 is converted[1011]
( TRUTH TABLE FOR|OR OPERATION)
X|Y|OR|
0|1|1|
1|0|1| BASICLY IF THERE IS ANY 1 ITS OR OPERATOR IS ALSO 1
0|0|0|
1|1|1|

0|1|1|1|
1|0|1|1|

---

1|1|1|1|

THEREFORE THE OR (|)OPERATOR WILL STORE 15

******\*******String****\*****
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
   **\*\*\***STRING METHOD**\*\*\***
   String method operates on Java string. they can be used to find length of string ,covert into lower case etc.
   1.name.length():it is to find length of string
   eg:String a= ("Happy");
   int b= a.length();
   System.out.println(b);
4. name.toLowerCase();:convert all capital letter into small letter
   eg:String name = ("HAPPY");
   String ball = name.toLowerCase();
   System.out.println(ball);
   3.name.toUpperCase():converts all samll letter to capital letter
   eg:String name = ("happy");
   String ball = name.toLowerCase();
   System.out.println(ball);
   4.name.trim():Spaces between the string is removed
   String nonTrimmedString = " Pratham ";
   nonTrimmedString.trim();
   System.out.println(nonTrimmedString.trim());
   {If you removed trim from the code it will print string with space}
   5.name.substring(): It give string the charecter that are associated with no till the end
   eg: String name = "Prathm";
   System.out.println(name.substring(1)); {Here 1 is the start and if we put comma and antoher no it will be the end }\*index start from 0\

4.name.replace : It replace the char or int
eg:String name = "Prathm";
System.out.println(name.replace(oldChr:'r',newChr:'t'));
5.name.startsWith()/name.endsWith():{It basically says true or false weather name starts with the thing you wrote in bracket}
eg: String name = "Pratham";
System.out.println(name.startsWith("Prat"));
6.name.charAt():it give the charecter of the index at index which you put in bracket
eg:String name = "Pratham";
System.out.println(name.charAt(3));
7.name.indexOf(): it basicaly returns the index of the thing you tiped in brackets
eg:String name = "Pratham";
System.out.println(name.indexOf("P"));
8.name.lastIndexOf(): it gives last index where the last character is situated
eg: String name = "Pratham";
System.out.println(name.lastIndexOf("a"));
9.name.equals():it check wether he sname are equal or not (as String are case specific if the capital or small letter are o similar it will print falls)
eg:String name = "Pratham";
System.out.println(name.equals("Pratham"));
10.name.IgnoreCase():it egnores the letter is capital or small but it should be equal to the String
eg:String name = "Pratham";
System.out.println(name.equalsIgnoreCase("prATham"));
********\*\*\*\*********Escape sequence****\*\*****
Sequence of charrecter after "\"
n\=new line
\t= new tab
\"=double cotation
\\= backslash

********\*********IF/ELSE/ELSE IF********************\*********************
Syntex

1.if:(condition){ }
2.if else: if(condition){ }else{ }
3.shorthand If..Else[ Ternary Operator]
variabler=( condition)?expressionTrue:expressionFalse;

\***\*Relation ship operator in java\*\***
These are used to evaulate the condition

1. [==] equal to
   2.not equal to[!=]
   3.>
   4.<
   5.<=
   6.>=

**\***NESTED IF ELSE STATEMENT **\***
It is statement more if else statement in single statement
**\*\***TERNARY OPERATOR**\*\*\***
a big code can be written in a small code
conditon?/condition?:
?=if
:=or

****\*****SWITCH STATEMENT******\*\*\*\*******

it is type of conditional statement .It is used when we have to make choices between multipal alternatives
SYNTEX: switch(variable/ expression){
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

**\*\*\*\***LOOPS**\*\*\*\***
loops are used when we want to repeate a set of statement again and again we use loops until a condition is satisfide

THERE ARE THREE TYPES OF LOOP
1.for loop
\\\SYNTEX FOR for loop///
for(Statement1;Statement2;Statement3;){
code to be executed
}
\\what statement stand for//
Statement1: initialisation,executed once
Statement2: condition,check every time before th loop
Statement3: reinitialisation,executed(every time)after the code block has been executed
eg: for (int i=1;i<=4;i++){
System.out.println(i);
}

2.while loop:It keeps executing the code till the condition is true.If the condition is never false it will make an infinite loop
Syntex=while(condition ){code}
eg:int i = 1;
while (i<=4){
System.out.println(i);
i++;
}
3.do while loop:It is similler to while loop but here code is run and then the condition is checked.
eg:int i = 0;do {
System.out.println(i);
i++;
}
while (i<=4);{
System.out.println(i);
}
**\*\*\*\***ARRAY**\*\*\***
Arreay is the collection of similer type of data.The indexing of the array starts from 0., i.e 1st element will be stored at the 0th index, 2nd element at 1st index, 3rd at 2nd index, and so on.
Syntex;
eg: int marks []= new int[3];{
marks[0]=52;
marks[1]=54;
marks[2]=13;
System.out.println(marks[1]);
There are three ways to write the array
here are three main ways to create an array in Java 1. Declaration and memory allocation
int [] marks = new int[5];

         2. Declaration and then memory allocation
         int [] marks;
         marks = new int[5];
         Initialization
         marks[0] = 100;
         marks[1] = 60;
         marks[2] = 70;
         marks[3] = 90;
         marks[4] = 86;

       3. Declaration, memory allocation and initialization together
        int [] marks = {98, 45, 79, 99, 80};

      marks[5] = 96; - throws an error
        System.out.println(marks[4]);
    }

}
#length of an array
to find length of an array we need to add marks.length
eg: int marks []= {65,45,34,};

            System.out.println(marks.length);

##for each loop
eg:int marks []= {65,45,34,};

            System.out.println(marks.length);
            for(int element: marks){
            System.out.println(element);

**\***multidimensional array**\*\***
int [] marks; // A 1-D Array
int [][]house; // A 2-D Array
house = new int [2][3];
house[0][0] = 101;
house[0][1] = 102;
house[0][2] = 103;
house[1][0] = 201;
house[1][1] = 202;
house[1][2] = 203;

        // Displaying the 2-D Array (for loop)
        System.out.println("Printing a 2-D array using for loop");
        for(int i=0;i<house.length;i++){
            for(int j=0;j<house[i].length;j++) {
                System.out.print(house[i][j]);
                System.out.print(" ");
            }
            System.out.println("");

****\*****INTRODUCTION TO OBJECT ORRIENTED PROGAMMING(OOP)**\*\*\***
OPP tries to map a code instructions to real making the code more short and simple
What is opp?:It is solving a problem with object
DRY:dont repete yourself:In progaming we dont repete the same code again and again but find the shortest code to solve the problem
#CLASS:class is an blueprint to creat an object
#OBJECT;an object is an initilazition of the class.
How to moddle a problem in OPP
Noun-->>class
Adjective -->>Attributes
Verb-->>Method
**\*OOP Terminology\*\***
1.Abstraction:It means hiding the internal detailes(show only essential information)
2.Encapsulation :Putting all the componants togeather(sensitive data is hidden)
3.Inheritance:The act of deriving new things from existing things
4.Polymorphism:One entity many forms
**\*\***How to creat a custom class**\*\*\*\***
public class MY{
it id;  
String name;}
**\*\*\***Access modifier and constructors**\*\***
Access modifiers:Access modifiers are keywords used to specify the accessibility of a class (or type) and its members.
Four type of access modifier
1.private,2.default ,3. protected 4.public (these are the key words )
#getter and setter
Getter ->Returns the value
Setter ->Sets value /update value
#constructures:Member used to initilize a object in java while creating it
**\***Inheritance****\*****
Inheritance is used to borrow properties and method from an existing class
Declaring inheritance in java
Superclass, subclass( subclass extends to superclass)
