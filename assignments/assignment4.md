---
layout: minimal
title: Assignment 4
description: &desc Assignment 4
summary: *desc
# has_children: true
nav_order: 1
has_toc: true
parent: Assignments
grand_parent: Leiden ITP
---

# {{ page.title }}
{: .no_toc .mb-2 }

{{ page.description }}
{: .fs-6 .fw-300 }

1. TOC
{:toc}

# Assignment 4: Recursive Merge Sort & Creating Class

**Deadline: ... 2023 23:59**

Hand in your assignment via [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322). See the "Delivery" section for instructions.


## Program

Explain:
 - recursive merge sort
 - sort two list, explain both ways;
   - remove elements from the list
   - walk through the list
 - default arguments key, explain why it needs to be a function.
 - default argument reverse (explain that this is a function)
 - recursion
 - classes with magic methods


Each Person object should be randomly initialized with:
 - A name from the global list `NAMES`.
 - An age between 18 and 100.
 - A height between 150 and 200 cm.
 - A weight between 45 and 100 kg.

## Template

The template for this assignment consists of 3 files: `merge_sort.py`, `person.py`, and `load_names.py`. While it is not mandatory to use these files, it is highly recommended. In the files, you can also find more information what to do where. You are allowed to add more functions. 

In this assignment, it is not allowed to use any hidden/private object attributes. A hidden/private object attribute in python can be recognized by a dubbel underscore e.g. `object.__height`. In many programming languages it is not possible to access these attributes outside the class. The reason for this is that the unspoken agreement is that class method should not change (get/set), but how a class internally works can be changed completely. This means that if you use hidden/private variables and the class gets updated, your code is likely to break. While it is possible in python to use any attribute of any object, it is not recommended for the same reason.  

In `merge_sort.py`, you will implement recursive merge sort and you will write a small script where you sort a list with `Person` objects in the following ways:
 - Without default arguments, for the `Person` class this means that the list is ordered from the shortest person to the tallest person. In other words, they are sorted in their default order. 
 - Reversed by using the default argument reverse.
 - With the default argument key, which should make sure you can sort a `person` object any way you like and at least on all possibilities described in the grading criteria.
 - A combination of reverse and key default arguments.
The small script should print the list sorted at least in all possible ways listed in the grading specification. Make sure when you print the list sorted in a certain way that it is clear which way it is sorted. 

...

In `person.py`, you will implement the person class and a create person list function. The person class should contain at least functionality for the following things:
 - When a `person` class object is printed it should show you the information of the object in a readable way. Thus, it should mention the name, weight, height, and age.
 - The string representation of the class should be the name.
 - The int representation of the class should be the age

The `__init__` method is already given and it is not allowed to create any other new object attributes e.g. (self.some_name = ...). 


## Grading

Points should be given for:
 - merge sort should be implemented recursive.
 - Default merge sort should be done by comparing objects (not attributes of objects or the return of methods)
 - You should be able to reverse sort using the default key.
 - You should be able to reverse sort in combination with any key argument.
 - You should sort the list using the key argument in merge sort based on the:
   - age
   - weight
   - height
   - name
   - indices 0, 1, 2, and 3
   - tuple or list representation of a `person` object
   - An index of the tuple or list representation
 - The string representation of `person` objects should be the name.
 - The int and float representation of `person` objects should be the age.
 - It should be possible to get a tuple or list representation of `person` objects. When this is done the order should be: name, age, weight, height.
 - Similarly, a `person` object should be subscriptable in the same order. For example, `person1[0]` should give the name of the object `person1`.
 - 
 - Dry coding. This means that everything should only be defined once and no code should be repeated.

## Tips


## Delivery

Once you are sure about your program, save a copy of your `.py` file with your **student number** and the **assignment number** as the file name. For example, if your student number is 123456, then save your copy as `123456_4.py`.

If your program consists of multiple files, then compress these into a `.zip` file with the same naming scheme: `123456_4.zip`. Please make sure to **not** include your `venv` folder if you do this. Your submission should not be larger than 50kB.

Next, upload your `.py` or `.zip` file on [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322) under "Assignments" > Assignment 4 - ... .
