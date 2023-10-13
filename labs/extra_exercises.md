---
layout: minimal
title: Extra Exercises
description: &desc 13 October, 2023 - Extra Exercises
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

Welkom, to the extra exercise page. Here, extra exercise will be posted for practising. These exercise are not mandatory and can range from very easy to very hard. This can also happen within one exercise, the first function might be very easy and the last very hard. The idea is that at the end of ITP you should be able to solve all of them. Behind easy exercise you can find the range of difficulty in the file.

Note, It can happen that some of these exercise will be used in the lab. 

The exercises are divided per Topic, but also per Syntax that you can practise. 

# Opening Exercise

Start by downloading the zip file from brightspace using [this link]. Unzip the files.

Now open PyCharm and select open and select the folder you just created (when unzipping). The folder contains folders for each topic. In the topic folders you can find the python files with the exercises.

# updating your folders with new exercises

When you already downloaded an older zip file, but there are new exercises. Go to brightspace and download the zipfolder agian using [this link]. Now, unzip the files in the same folder as where you unzipped it the first time. **VERY IMPORTANT WHEN YOUR FILEMANAGER ASKS YOU WHAT TO DO WITH DUPLICATE FILES CHOOSE SKIP NEW FILES AND/OR NOT OVERWRITE OLD FILES!**

# Topic

## Standard Python Library Functions

This topic covers all standard python library functions that might be useful. All exercise in this topic exist of making your own basic function with a certain functionality and slowly building towards more advanced implementations. The last function always asks you to use the standard python library function.

### abs (Easy -> Hard)

Open abs.py, here you will implement absolute values, see [wiki](https://en.wikipedia.org/wiki/Absolute_value) for more information.

### all (Easy)

Open all.py, here you will implement the `all()` function. This checks if all values in an iterable are True. 

### any (Easy)

Open any.py, here you will implement the `any()` function. This checks if a values in an iterable is True. 

### isinstance (Easy)

Open isinstance.py, here you will implement the `isinstance()` function. `isinstance`
can be used to check if a object is of a certain type.

## Useful Python Functions

# Syntax

## loops

In the following exercises you can practise with for loops:

- any
- all

## logic (boolean)

In the following exercises you can practise with booleans and if statements:

- any
- all

## Ternary Operator

The idea of a ternary operator is that you can have two outcomes depending on a rule. While python does not officially have a ternary operator (like C#, C++, java, etc.), there is a common way of writing them. You should use a ternary operator when the value of a variable should be A in the case of ... ortherwise B. It replace the following code:
```python
if SomeCondition:
    value = 10 #this can be any value
else:
    value = 20
```

The problem with the code above is that an `if` `else` statement can do anything, while the a ternary statement signals to the reader that a value is assigned according to some condition. The code above as a ternary statement in python looks as follows:
```python
value = 10 if SomeCondintion else 20
```

In the following exercises you can practise with ternary operators:

- abs (Easy -> Hard)

## isinstance

`isinstance` returns True if the object argument is an instance of the classinfo argument, or of a (direct, indirect, or virtual) subclass thereof. If object is not an object of the given type, the function always returns False. 

It is recommended that you fist do the isinstance.py exercise.

In the following exercises you can practise with the isinstance function:

- abs (Easy -> Hard)
- isinstance (Easy)

## complex arithmetic

For info on complex numbers, see [wiki](https://en.wikipedia.org/wiki/Complex_number). Just skip this part of the exercise, if you did not get complex numbers with calculus.

In the following exercises you can practise with complex numbers:

- abs (Easy -> Hard)
