# C++ Notes

## <p style="text-align: center;"> Index </p>

1. Installation
2. Introduction
3. Syntax
4. User input
5. Arathmatic Operator
6. Conditional Statement (If/Else/Elif)
7. Switch Statements
8. Loops
9. Array
10. Pointer Concept
11. Object And Classes
12. Function

---

## Installation

1. Download Mingw
   - In Installation manager download download all file
   - Add Mingw to path Enviroment variable
     - This pc -> Properties -> Advance system settings -> Enviroment variable -> Add path -> Add bin path to enviroment
2. Downlaoad vs code
3. Downlaoad Extentions

---

## Syntax

```
#include <iostream>
using namespace std;
int main()
  {
  cout << "Lets start";
  return 0;
  }
```

> #include `<iostraeam>`header file library that lets us work with input and output objects
> `using namespace std;` we can use names for objects and variables from the standard library.

`int main()` This is called a function. Any code inside its curly brackets {} will be executed.

`{cout << "Hello world"; }` Print content in console.

## User input

How to take input from user

```
int g;
cin >> g;
```

## Arathmatic Operator

```
    int s = 2;
    int f = 7;
    cout << "s+f is" << s + f << endl;
    cout << "s-f is" << s - f << endl;
    cout << "s*f is" << s * f << endl;
    cout << "s/f is" << s / f << endl;
```

---

## Conditional Statement (If/Else/Elif)

### 1. If Else

```
   if (/* condition */)
   {
       /* code */
   }
   else
       (/* condition */)
       {
           /* code */
       }
```

### 2. Elseif

```
    elseif

    else if (/* condition */)
    {
        /* code */
    }
     else

```

---

---

## And(&) Or(||) Not(!)

## Switch Statements

```
  switch (expression)
    {
    case /* constant-expression */:
        /* code */
        break; // If you dont put break then it will execute all the code bellow

    default:
        break;
    }
```

## Loops

### 1. While

```
 while (/* condition */)
    {
        /* code */
    }
```

### 2. DoWhile

```
do
    {
        /* code */
    }
 while (/* condition */);

```

### 3. For Loop

```
for (condition)
    {
        /* code */
    }
```

---

## Array

Collection of data

```
 int arr[2] = {
        1,
        2,
    };
```

## String

## ` string name = "Laptop";`

## Pointer Concept

```
 int a = 34;
    int *ptra; // the * star stores the data of the int in ptra

    ptra = &a; //& is used to laocate adress of the data

```

## Object And Classes

```
 class C
    {private: /* data */
     public:C(/* args */);
        ~C();
    };
    C::C(/* args */)
    {
    }


```

## Function

```
int add(int l, int n)
{
    int y;
    y = l + n;
    return y;
}

```
