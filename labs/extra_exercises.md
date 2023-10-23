---
layout: minimal
title: Extra Exercises
description: &desc 23 October, 2023 - Extra Exercises
summary: *desc
nav_order: 1
parent: Labs
grand_parent: Leiden ITP
---


# {{ page.title }}
{: .no_toc .mb-2 }

{{ page.description }}
{: .fs-6 .fw-300 }

1. TOC
{:toc}

Welkom, to the extra exercise page. Here, extra exercises will be posted for you to practice. These exercises are not mandatory and can range from very easy to very hard. This can also happen within one exercise, the first function might be very easy and the last very hard. The idea is that at the end of ITP, you should be able to solve all of them. Behind easy exercise, you can find the range of difficulty in the file.

Note, It can happen that some of these exercises will be used in the lab. 

The exercises are divided per Topic, but also per Syntax that you can practise. 

# Opening Exercise

Start by downloading the zip file from brightspace using [this link]. Unzip the files.

Now open PyCharm, select open, and select the folder you just created (when unzipping). The folder contains folders for each topic. In the topic folders, you can find the Python files with the exercises.

# updating your folders with new exercises

When you already downloaded an older zip file and there are new exercises follow these instructions: Go to brightspace and download the zip folder again using [this link]. Now, unzip the files in the same folder as where you unzipped them the first time. **VERY IMPORTANT WHEN YOUR FILEMANAGER ASKS YOU WHAT TO DO WITH DUPLICATE FILES CHOOSE SKIP NEW FILES AND/OR NOT OVERWRITE OLD FILES!**

# Topic

## Standard Python Library Functions

This topic covers all standard Python library functions that might be useful. All exercises in this topic exist of making your own basic function with a certain functionality and slowly building towards more advanced implementations. The last function always asks you to use the standard Python library function. Note, that your implementations only mimic the standard Python library functions, often they are implemented smart and/or handle more inputs. 

### abs (easy -> hard)

Open abs.py, here you will implement absolute values, see [wiki](https://en.wikipedia.org/wiki/Absolute_value) for more information.

### all (easy)

Open all.py, here you will implement the `all()` function. This checks if all values in an iterable are True. 

### any (easy)

Open any.py, here you will implement the `any()` function. This checks if a value in an iterable is True. 

### bool (very easy)

Open bool.py, here you will implement the `bool()` function. This checks if a value is True.

### chr and ord (easy)

Open chr_and_ord.py, here you will use the `ord` and `chr` functions to convert ASCII values to characters and vice versa.

### combine map and filter (medium -> very hard)

Open combine_map_and_filter.py, here you will combine what you have learned in the map exercise and the filter exercise. It is recommended to do those exercises first. 

### dict (very easy)

Open dict.py, here you will practice various ways of initializing a `dict`.

### divmod (very easy)

Open divmod.py, here you will implement `divmod`. This is a useful function when dealing with 2D array indices.

### filter (easy -> very hard)

Open filter.py, here you will implement `filter` using various syntaxes. Each function uses a bit more advanced syntax until you reach using `filter` itself. This is a good exercise to see how various `for loops` work and that a function like `filter` is just an advanced for loop. 

This exercise also shows you that there are many ways to code the same functionality. However, they are not all as "good". Generally, the "goodness" of a block of code can be measured in two ways: speed and readability. Speed is a bit too advanced to get into at this point, however, during the exercise question yourself which code has a clearer functionality. For example, a for loop only signals that it loops over an iterable object, but can be anything. So, if there is a good alternative, a for loop is most likely not the most clear/readable choice.

### isinstance (easy)

Open isinstance.py, here you will implement the `isinstance()` function. `isinstance`
can be used to check if an object is of a certain type.

### map (easy -> very hard)

Open map.py, here you will implement `map` using various syntaxes. Each function uses a bit more advanced syntax until you reach using `map` itself. This is a good exercise to see how various `for loops` work and that a function like `map` is just an advanced for loop. 

This exercise also shows you that there are many ways to code the same functionality. However, they are not all as "good". Generally, the "goodness" of a block of code can be measured in two ways: speed and readability. Speed is a bit too advanced to get into at this point, however, during the exercise question yourself which code has a clearer functionality. For example, a for loop only signals that it loops over an iterable object, but can be anything. So, if there is a good alternative, a for loop is most likely not the most clear/readable choice.

### min max and intervals (easy)

Open min_max_intervals.py, here you will implement `min`, `max` and how to make sure that a value is between an interval. In other words, how to make sure that `x >= min value`, `x =< max value` and `left boundary <= x <= right boundary`.

### reversed (medium)

Open reversed.py, here you will implement `reversed`. Reversed is a good function when you want to loop through an object in the reversed order.

### sorted (very hard)

Open sorted.py, here you will implement `sorted`. Sorted is a good function when you want to loop through an object in the sorted order.

### sum (easy)

Open sum.py, here you will implement `sum`. Sum is a good function when you want to know the total of a list. However, every object that implemented the operator `+=` can be used. Thus, a 2D list can also be "flattened" to a 1D list using sum.

### zip (easy)

Open zip.py, here you will implement `zip`. Zip can interleave iterables together into a generator (list) with tuples that contain the i'th element from each iterable. Zip is a very useful function when you want to create a dictionary from two lists or want to loop over two or more lists at the same time.

Examples of zip:
```python
>>> list(zip([1, 2, 3]))
[(1, ), (2, ), (3, )] # (1, ) is a tuple with one object (1) is just parentheses around the int 1.
>>> list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]
```


## Useful Python Functions

# Syntax

## complex arithmetic

For info on complex numbers, see [wiki](https://en.wikipedia.org/wiki/Complex_number). Just skip this part of the exercise, if you did not get complex numbers with calculus.

In the following exercises, you can practice with complex numbers:

- abs (easy -> hard)

## dictionaries

In the following exercises, you can practice with dictionaries:

- dict (very easy)

## (helper) functions

In the following exercises, you can practice with (helper) functions:

- combine map and filter (medium -> very hard)
- filter (easy -> very hard)
- map (easy -> very hard)
- sorted (very hard)

## isinstance

`isinstance` returns True if the object argument is an instance of the classinfo argument, or of a (direct, indirect, or virtual) subclass thereof. If an object is not an object of the given type, the function always returns False. In other words, `isinstance` checks if your variable is an object of a certain class.

It is recommended that you first do the isinstance.py exercise.

In the following exercises, you can practice with the isinstance function:

- abs (easy -> hard)
- isinstance (easy)

## list comprehensions

In the following exercises, you can practice with list comprehensions:

- combine map and filter (medium -> very hard)
- filter (easy -> very hard)
- map (easy -> very hard)

## logic (boolean)

In the following exercises, you can practice with booleans and if statements:

- any (easy)
- all (easy)
- bool (Very easy)
- min max and intervals (easy)

## loops

In the following exercises, you can practice with for loops:

- any (easy)
- all (easy)
- chr and ord (easy)
- combine map and filter (medium -> very hard)
- filter (easy -> very hard)
- map (easy -> very hard)
- reversed (medium)
- sorted (very hard)
- sum (easy)
- zip (easy)

In the following exercises, you can practice with while loops:

- sorted (very hard)

## slicing

In the following exercises, you can practice with slicing:

- reversed (medium)

## Ternary Operator

The idea of a ternary operator is that you can have two outcomes depending on a rule. While Python does not officially have a ternary operator (like C#, C++, java, etc.), there is a common way of writing them. You should use a ternary operator when the value of a variable should be A in the case of ... or otherwise B. It replaces the following code:
```python
if SomeCondition:
    value = 10 #this can be any value
else:
    value = 20
```

The problem with the code above is that an `if` `else` statement can do anything, while the ternary statement signals to the reader that a value is assigned according to some condition. The code above as a ternary statement in Python looks as follows:
```python
value = 10 if SomeCondintion else 20
```

In the following exercises, you can practice with ternary operators:

- abs (easy -> hard)




