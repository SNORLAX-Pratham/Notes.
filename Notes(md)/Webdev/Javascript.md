```


/*Java Script
JavaScript can "display" data in different ways:
•	Writing into an HTML element, using innerHTML.
•	Writing into the HTML output using document.write().
•	Writing into an alert box, using window.alert().
•	Writing into the browser console, using console.log()

JavaScript console API
//Javascript console API (Used to print in console )*/
console.log("Hi");
console.warn("okk");
console.error("NOT");

/*JavaScript Variable
Variables: They are used to store data in container*/
var number = 34;
console.log(number);


/* Multiline Comment*/

/*Data type in js */
var string1 ="This is a String";
var num =445;

/* Objects in js*/
var marks ={
    object1:1,
    object2:2,
}

/* Boolean data types*/
var a = true;
var b =false;
console.log(a,b)

/* Ther are two type of data type in JS
1. Primitive data types : Undefined,null,number,string,boolean,Symbole
2. Referance data types : Arrays And objects
*/

/*Arrays in JS*/
var arr =[1,2,3,4,5]

//Operator in JS
  //Arithmatic operators
  var g =10;
  var h =12;
  console.log("The value of g+h is ",g+h);
  console.log("The value of g-h is ",g-h);
  console.log("The value of g*h is ",g*h);
  console.log("The value of g/h is ",g/h);

  //Functions:function is a block of code designed to perform a particular task

  function  avg(a,b){
    return(a+b)/2;
  }
  c= avg(2,3);
  console.log(c);

  //Conditions in JS
   var age= 12;
   if(age>10){
    console.log("Above 10")
   }
   else if(age<10){
    console.log("Nothing")
   }
   else{

   }


   //Loops

   //Forloops
   var a= [1,2,3,4];
   console.log(a);
   for(var i=0;i<a.length;i++){
    console.log (arr[i])
   }
   //for esch loop
   array.forEach(element => {

   });

   //While loop
   while (condition) {

   }

   //Break/Continue
   var a= [1,2,3,4];
   console.log(a);
   for(var i=0;i<a.length;i++){
    console.log (arr[i])
    break
   }

//Dates
let mydate= new Date();
console.log (mydate.getTime);
```
