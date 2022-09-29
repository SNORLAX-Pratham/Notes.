# Data Structures & Algorithm

Data structures: Arrangement of data so that they can be used efficiently in the memory.

Algorithm: Sequence of steps on data using an efficient data structure to solve a given problem

## Terminology

**Data Base:** Collection of info in permanent storage for faster retrieval and update.

**Data Warehouse:** Management of massive amount of legacy data (Data that is imp but not currently needed) for better analysis

**Big Data:** Analysis of large and complex data that traditional data processing applications cannot deal with.

## Memory layout in C Programming

When code starts it is copied into the main memory
Initialized and uninitialized data segments hold the Initialized and uninitialized global variables

**Stacks**: hold the memory occupied by the function

**Heaps**: Contain data that is requested by the program as dynamic memory

---

# Time complexity and BigO Notation

**Time Complexity:** Study of efficent Alogo and time taken to execute an Alogo which grow with size of input

> A way of showing how run time of function increases as size of input increases

### Run time of a function

1. **Linear** : As size of file increases the time increases O(n)
2. **Constant**: As file size increases the time remain the same O(1)

#### Way to find fastest growing term

1. Find fastest growing value
2. Take out cofficiant of term

---

# Asymphotic Notations

> Givess idea how good an algo is comapred to others

### Type of asymphotic Notation

1. Big oh (O)
   : Upper band, describe runtime if exist +ve constant
2. Big Omega : lower band ,describe if exist +ve const
3. Big Theta : Gives better picture oofuntime (Most used , Asked)

---

# Best case / Worst case /Average analysis of algo

### For a give case there are theree outcome worst best avg

> Log : Number of time you can half an array of size (n) befor it gets exhausted

> Space complexity : While analyzing an algo we take care of both time and spave in mind

### Calculating Time complexity of algo (Tricks)

1. Drop non dominant term
2. Drop constant term
3. Break cod into fragments
