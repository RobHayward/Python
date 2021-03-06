---
title: "Automate"
author: "Rob Hayward"
date: "26 December 2015"
output: 
  html_document: 
    highlight: kate
    number_sections: yes
    theme: united
    toc: yes
---

#Introduction

There are two methods

* Interactive shell 
* Text editor

There are different classes

* integer
* floating points
* strings

There are 

* Statements
* Expressions (evaluates)

Objects can be switched from one class to another. For example, 

* str(26)
* int(124)
* float(1)

##Boolean operators

Operator|Evaluates to
--------|------
True and True| True
True and False| False
False and True| False
False and False| False

Operator|Evaluates to 
--------|-----------
True or True|True
True or False|True
False or True|True
False or False|False

Operator|Evaluates to 
------|------
Not True|False
Not False|True

## Control statements
Programmes can be evaluated at [Python Tutor](https://pythontutor.com/visualize.html). Blocks of code are determined by indentation.  

Order of the `if...elif` statements is important.  The first true will be activated. The values 0, 0.0 and the empty string are considered false values. You can check with `bool()`.

If there is an infinite loop, CNTR-C will end. `break` can also be used to break the programme. `continue`  can also be used within a loop. 

`range` is an object that will run from first to last number.  For example, `range(2, 4)` will run from 2 to 4.  Third argument would be the step function. 

#Functions
Each python instillation comes with a group of modules or built in functions. For example, the `math` module has maths functions and the `rand` module has functions for random variables. `import`  will import the module. 

```
import(rand)
random.randint(0, 1)
```

If you type, 
```
from rand import *
```

This will import all the functions from the random module. Now it is not necessary to type rand. before the function.  There are modules with the standard library but also third party libraries.  These are imported with `pip`. 

## Writing own functions
`def` is used to define a function. 

```
def hello():
    print('Howdy')
    print('Howdy!!')
    print('Howdy!!!')

hello()
hello()
hello()
```

Functions aim to remove the need to duplicate. 

* The function will take *arguments* that are specified by the user. They are called *parameters* when they are given in the function. Function calls can be part of expressions because they evaluate to a value returned by the function call. When creating a function with the `def` statement, you can specify what should be returned with the `return` statement. 

`None` is a special value returned by print.  It is a lack of a value. Every function has a return value. `key word arguments` can be added to functions to change the behaviour. 

Variables inside a function can have the same name as a variable outside a function.  

* Global scope: available throughout
* Local scope: available in the function

These scopes are containers of variables.  Variables that are either *global* or *local*.  The global is created when the program starts and is destroyed when it is closed; the local is created when a function is called and destroyed when it is returned.

Local variables cannot be used in the global scope. However, local variable can use global variables.  Python will assume that the variable is local so long as it is assigned.  If you want Python to take the global variable after the name has been assigned in a function, it is necessary to use  `global xxxxx `. 

The benefit of having global and local variables is that it separates functions from the rest of the code. If something goes wrong in the function, it is confined to the function. 

##Handling errors
To stop program ending on an error, it is possible to use `try` and `except`.  This will continue in the case of an error being thrown.  See example in `error.py`

### Input validation
```
print('How many cats do you have?')
numCats = input()
try:
  if int(numCats) >= 4:
    print('That is a lot of cats')
  else: 
    print('That is not that many cats.')
except ValueError:
  print('You did not enter a number')
```

Input is validated as a number.   

# Lists
Contains multiple values in an ordered sequence. It contains items. Individual items can be taken from the list with indexation `[]`.  Also a *slice* of several values can be taken. `list` function will turn something like a string into a list.  `in` function will determine whether an item is in list (returning a boolean). `not in` is the opposite. 

One good method is to use for loops and lists.  For example, 
```
supplies = ['pens', 'penciles', 'rubber', 'board']
for i in range(len(supplies)):
  print('index' + str(i) + 'in supplies is: ' + supplies[i])
```

This allows i to be the index number and the place in the supplies list. 

###Multiple Assignment
If there is a list `cat` with items `fat`, `orange` and `loud`.  These can be assigned to other variables with 
```
size, colour, disposition = cat
```

This can be used to perform **swap variables** 

###Augmented Assignment Operators
```
spam = 42
spam = spam + 1
spam
```

is the same as 
```
spam += 1
```
# Methods
This is the same as a function but it is called on a specific value. For example, `index` is a method that will find the index of a particular list.  However, you have to call that method on the object `listname.index`.  Each data type has its own set of methods. 

To add new values to a lit use the `append()` and `insert()` methods. Methods only apply to a particular data type. `sort()` is a useful list method. Key words may change behaviour. For example, `reverse = TRUE` will change the behaviour of sort. Cannot sort strings and integers.  AscII-betical sort will put capitals before lower case. 

A list can be seen as a single character string.  Many of the functions can be used.  While strings can be index but they are immutable (cannot be changed). To change strings, there is a need to create a new string.

Immutable objects (like lists) stand alone and the list themselves just contain references to the list. Therefore, if the list is assigned to another name and a change in made in the list under that name, the list referred to by the original name will also change. Therefore, if a list is used and changed inside a function, this will also change the global value.   Immutable variables like strings and duple do not face this problem. 

A fundamental change can be made with a `deep copy`.  This is in the book. 

##Dictionaries
Like lists dictionaries contain different data types but use something other than integer for index. They are called keys. A key-value pair. 

Three methods of getting information
```
list(eggs.keys())
list(eggs.values())
list(eggs.items())
```
It is usually best to test whether key exists before trying to return its value. this will prevent an error message. 

List of methods for dictionaries 

* `dictionary.get(<what you want?, what to return if not there)`
* `setdefault()` this will set the key if it does not already exist.

## Data structures
Dictionaries are good ways of managing data. 

Look at tic-tac-toe function, 

`type` will determine object type. 

# Strngs
Need double quote sometimes. 

```
"That is Alic's hat"
```
Escape characters allow the use of otherwise illegal characters. For example, 

``` 'Say hi to Bob\'s mother' ``` 

```print('Hello \nWhat is you name \nI\'m fine)```

A *raw-string* will print all the characters as they are.  For example, 

```r'This is Calva\'s cat' ```

A multi-line string can also be made with three (double) quotations. For example, 

``` 
"""Deal Alice
Eve's cat has been arrested. """ 
````
## More strings

There are a number of function

Function| Use
---|---
x.lower() | changes x to lower case
x.upper() | changes x to upper
x.islower()| Checks if x is lower case
x.isupper()| checks if x is upper case
isalpha()| letters only
isalnum()| letters and numbers only
isdecimal()| Numbers only
isspace()| Space only
istitle()| title-case only
.title()| Changes something to title
join()| Will join strings together (join can be specified)
.split()| Splits a string
ljust()| left justified (length of string and filling can be specified)
rjust()| right justified
center()| Centre
strip()| Strip (white space, or specified)
rstrip()| right strip (white space, or specified)
lstrip()| left strip (white space, or specified)
replace()| replace one string with another
paperclip.copy()|copy to clipboard (need to install paperclip)
paperclip.paste()| paste to the clipboard (need to install paperclip)

##String formatting
Insteady of catonating strings with quotes and plus, it is possible to use the *string formatting* function.  This uses `%s` for insertion. These are called *conversion specifiers*.  

#Running python from the command line
The first line of python programmes should be a *shebang* line. 

This is 

* `#! python 3` for windows
* `#! /usr/bin/env python 3` for linux

On windows press `windows key +R` to being up the *run dialog*. Type `cmd` to bring up the command prompt window. 

*Batch files* or *Script file*

Environemnt variables are set from *advanced system settings* in the *control panel*.  If the path to the folder with the batch file is specified, this will automatically search that folder for the file. This saves specifiying the whole path. 

Function arguments can be specified in the command line. 
