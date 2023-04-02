```
#include <stdio.h>

int main()
{
    printf("Hello");
    return 0;
}
```
> To run the program in terminal write gcc (file name) a.exe file will be created in the folder
in terminal wirte a and then press tab


`c fille in vs code --> Compiler (gcc)--> file.exe`

A compiler is a computer program which converts a c program in machine lang so that it can be eaily understood by the computer
>C program is written in plain text. The compiler perform checks and converts into an executable

## Library functions

C lang has lot of library fuction which is used to carry out certain task `printf` to print value on screen

## Variable Constants and Variables

Rules for naming variables in C

     1. First char must be an alphabet or underscore
     2. No commas, blanks allowed
     3. No symbols allowed
     4. Vairiable name are case sensitive

 Rules applicable to all C programs
 
1. Every progrma execution starts from main () function
2. All statements are terminated with a ;
3. Instruction are Case- Sensitive
4. Instruction are executesd in the same order in which    they are written

 ## Inputs
 ```
    int a, b;
    printf("Enter value of a \n");
    scanf("%d", &a); //& is the address where the value of %d is stored
    printf("Enter value of b \n");
    scanf("%d", &b);

    printf("The sum fo a and b is %d", a + b);
    return 0;
```
## Variables

1. `%d `for intgers
2. `%f `for real value
3. `c% `for character

```
    int a = 3;
    float b = 7.9;
    char c = 'df';
    printf("hi %d", a);
    return 0;
```
## Arithmatic Operators
```
    int z = 1;
    int x = 4;
    printf("The value of z+x is %d", z + x);
    printf("The value of z+x is %d", z - x);
    printf("The value of z+x is %d", z * x);
    printf("The value of z+x is %d", z / x);
```
## Conditional Instruction
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
    else if (/* condition */)
    {
        /* code */
    }
```

## Relation operator
1. `>`
2. `<`
3. `==`
4. `>=`
5. `<=`
6. `!=`

## Logical operator 
1. && (and)
2. ||(Or)
3. ! (not)

## Loop Controle instructions
Loops are used to do things over and over again

>  There are three type of loops While loop/do-While loop/for loop
```
    // While

    while (/* condition */)
    {
        /* code */
    }
```
```
    // ?for
    for (size_t i = 0; i < count; i++)
    {
        /* code */
    }
```
```    
    // ?do while
    do
    {
        /* code */
    } while (/* condition */);
```
## Function and recursions
In order to manage bigger programm we can break code into
pices in this way it is easy to reuse code so we use function
> Fuction is block of code which perform perticular task
```
    void display(); // Function Prototype
    int main()
    {
        int a;
        display(); // Fuction call
        return 0;
    }
```
```
    void display()
    { // Fuction definition
        printf("This is display");
    }
```
## Types of function

1. Library functions : Commanly required functions grouped in liberary
2. User defined function : function define function
## Pointers
A pointer is a variable which stores the address of another variable
> The address of (&) operator: The address is used to obtain the adress of a given variable
1.  Format specifierv for printing adress is (`%u`)
 2. The value at adress operator (`*`)
    the value at address or operator is used to obtain the value
3. present atv a given memory address it is denoted by (`*`) 

 ## How to declare a pointer?
 ```
    int t = 3;
    int *j = &t; // j will store the adress of t
    printf("value of t is %d", t);
    printf("adress of t %u" & t);
    return 0;
```
 ## Arrays
 It is simalar item collection
```
    int marks[4];
    marks[0] = 35;
    marks[1] = 32;
    marks[2] = 34;
    marks[3] = 36;
```
array index starts with 0.The memory will store the value in form of bytesif arcetecture of system is 4 byte and 3 values are stored then 12 bytes  4 byte for each intiger

## Multi dimetion Array
```
    int stud = 3;
    int sub = 5;
    int marks[3][5]; // 3 rows and 5 coloums
```
# Strings
1D array termintaed by a null (\0)
```
    char str[] = {'h', 'b', 'c', '\0'};
    // gets (): for multi word string
    // puts (): output of string
```
## Structures
    struct c
    {
        /* data */
    };

## File I/o
Ram read the file before it is shown to the public
Ram is volatile and its content is loss once programm is terminated in order to persist the data foreve we use file
> A file is data stored in a storage device .A c program can talk to the file by reading conten from it and writing content to it.

File Pointer : A file is a structure which need to be created for opening a file
```
    FILE *ptr;
    ptr = fopen("filename.exe", "mode");
```
##  Dynamic Memory Allocation
> C is a language with fixed rules of programming change the size of an array is not allowed

Dynamic memory allocation is a way to allocate memory to a data structure during runtime we can us DMA function available in C to allocate and free memory during run time
 Malloc()function: It takes number of bytes to be allocate as an input and returns a pointer of type void
```
{
    int *cgt
        cgt = malloc(6 * sizeof(int));
}
```
