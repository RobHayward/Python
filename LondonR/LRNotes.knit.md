---
title: "London R Python"
output: 
  html_document: 
    theme: journal
---

## Section 1: Introduction

1. sudo privides super-user priviledges. 
2. "apt-get" will install from the internet.  
3. "apt-get update" will update all the current packages over the internet. 
4. Negative indexing in python starts from the other end.
5. Indexing starts from zero. 
6. Subsets a:b start from a and run up to (but do not include) b
7. Full slicing takes three parameters: object(start, stop, step)

## Dictionaries
Can hold any combination of python objects but is indexed by ordered position they are indexed by keys. They are created with the curley brackets notation. {}

```
D = {'name' : 'John', 'age' : 32, 
            'height': 1.76, 'workdays': ['Mon', 'Wed', 'Fri']}
```            
Therefore D['age'] returns 32 and D['workdays'][1] returns 'Mon' as it is indexing a list within a dictionary.

D['tel'] = 012732456 adds a new value.

Data structure | Description | Mutable| Ordered | Example
--------------|-------------|---------|---------|-----------
String | An ordered sequence of characters| No | Yes| s = 'my cool string'
List | An ordered collection of elements | Yes | Yes| l = ['spam', 'ham', 'jam']
Dictionary | An unordered collection of keys| Yes | No | nums = {'john : 01295, 'mary': 23452}

## Control flow
Indentation is essential in python. 

###If statements
``` 
x = 5
if x > 0: 
  print 'x is positive'
elseif x < 0:  # optinal and multiple elsif braanches possible
  print 'x is negative'
else: # Also optional 
  print 'x is zero'
```
