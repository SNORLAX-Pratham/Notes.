# Java Script

- Programming Lang of Web
- Ecma Script: It is script on which JS is based on.

---

JavaScript can "display" data in different ways:

- Writing into an HTML element, using innerHTML.
- Writing into the HTML output using `document.write()`
- Writing into an alert box, using `window.alert()`
- Writing into the browser console, using `console.log()`

## JavaScript console API

> Javascript console API (Used to print in console ) -`console.log("Hi");` -`console.warn("okk");` -`console.error("NOT");`

## JavaScript Variable

Variables: They are used to store data in container

- Type of variable var,let,const
- `var` is globle scoped

  ```
  var a=2;
  console.log(a)
  ```

- `Let `and `const` block scoped
  ```
  let a=2;
  console.log(a)
  ```
  ```
  const a=2;
  console.log(a)
  ```

`/* Multiline Comment*/` `// Single Line Comment`

## Data type in Js

### Premitive Datatype

| Data Type | Code                    |
| --------- | ----------------------- |
| Null      | `let a = null;`         |
| Number    | `let b = 145;`          |
| String    | `let c = "Pratham"`     |
| Symbol    | `let d = Symbol("he")`  |
| Undefined | `let e = undefined;`    |
| Boolean   | `let f = true;`         |
| BigInt    | `let g = BigInt("567")` |

To Find Datatype
`console.log(typeof a)`

> Referance data types : Arrays And objects

## Objects/Non-Premitive in Js

```
var fruits ={
object1:Mango,
object2:Banana
}
console.log(object1)

```

# Arrays

```
let arr =[1,2,3,4,5]
```

# Operator in JS

### Arithmatic operators

```
let a =1;
let b=2;
console.log("a+b=",a+b);  // Add
console.log("a-b=",a-b); // Sub
console.log("a/b=",a/b); // Divide
console.log("a*b=",a*b); //Multiply
console.log("a**b=",a**b); // Exponant
console.log("a%b=",a%b); //Modulus
console.log("a++=",a++); //Incriment
console.log("a--=",a--); // Decrement
```

### Assignment Operator

Equal To EG-

```
let a =3 ;
b=a;
console.log(b)

```

| Operator | Function |
| -------- | -------- |
| =        | x=y      |
| +=       | x=x+y    |
| -=       | x=x-y    |
| \*=      | x=x\*Y   |
| /=       | x= x/y   |
| \*\*=    | x=x\*\*Y |

### Comparison Operator

| Operator | Function              | Example |
| -------- | --------------------- | ------- |
| ==       | Equal to              | x`==`y  |
| !=       | Not Equal to          | x`!=`y  |
| >        | Greater than          | x`>`y   |
| <        | less than             | x'<'y   |
| >=       | Greater than equal to | x`>=`y  |
| <=       | less than equl to     | x`<=`y  |

### Logical operators

sometime logical operator are also called boolean operator

| Operator | Example              |
| -------- | -------------------- | --- | ----- |
| and      | x<5 `&&` x<7         |
| or       | x<5 `                |     | ` x<3 |
| not      | `!`(x < 5 && x < 10) |

# Functions:

> Function is a block of code designed to perform a particular task

```
  function  avg(a,b){
    return(a+b)/2;
  }
  c= avg(2,3);
  console.log(c);
```

# Conditions in JS

```
   var age= 12;
   if(age>10){
    console.log("Above 10")
   }
   else if(age<10){
    console.log("Nothing")
   }
   else{

   }
```

# Loops

**Forloops**

```
   var a= [1,2,3,4];
   console.log(a);
   for(var i=0;i<a.length;i++){
    console.log (arr[i])
   }
```

**for each loop**

```
   array.forEach(element => {

   });
```

**While loop**

```
   while (condition) {

   }
```

**Break/Continue**

```
   var a= [1,2,3,4];
   console.log(a);
   for(var i=0;i<a.length;i++){
    console.log (arr[i])
    break
   }
```

# Dates

```
let mydate= new Date();
console.log (mydate.getTime);
```
