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
{: .fs-6 .fw-400 }

1. TOC
{:toc}

# Assignment 4: Recursive Merge Sort & Creating Classes

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

### Merge Sort

In `merge_sort.py`, you will implement recursive merge sort and you will write a small script where you sort a list with `Person` objects in the following ways:
- Without default arguments, for the `Person` class this means that the list is ordered from the shortest person to the tallest person. In other words, they are sorted in their default order.
- Reversed by using the default argument reverse.
- With the default argument key, which should make sure you can sort a `person` object any way you like and at least using all possibilities described in the grading criteria.
- A combination of reverse and key default arguments.

The script should print the list at least sorted in all possible ways listed in the grading specification. Make sure when you print the list sorted in a certain way that it is clear which way it is sorted. This script can either be added in `merge_sort.py` below all classes and functions or you can use a `main` function and add `if __name__ == "__main__": main()` at the bottom of the file.

### person class

In `person.py`, you will implement the person class and a create person list function. The person class should contain at least the functionalities described in the grading criteria. The `__init__` method is already given and it is not allowed to create any other new object attributes e.g. `self.some_name = ...`. The `create_persons_list` function should return a list of `person` objects randomly initialized as described in the program section.

### Load Names

In `load_names.py` you will write code to load the file **names.txt**. The function `load_names` should return a 1D list or array with the names.

## Dry code (Don't repeat yourself)

During this assignment it is important to write dry code. This means that everything should only be defined once and no code should be repeated. This is more elaborated than it sounds. For example, if you have an `if` `else` control-flow and both contain a few lines of similar code then it is not dry. This could be solved by removing the similar code outside the `if` `else` control-flow or write a function that execute the same code and call in both statements the new function. Old code could look like this:
```python
if check_first_name(name):
   name = name.lower()
   print(f"The first name of this person is {name}")
else:
   name = name.lower()
   print(f"The last name of this person is {name}")
```

The dry code can be:
```python
name = name.lower()
if check_first_name(name):
   print(f"The first name of this person is {name}")
else:
   print(f"The last name of this person is {name}")
```

There are a few reasons why *dry* coding is important. Not only does it make your code shorter, often more readable, and it can save you time writing the same code over and over. Maybe the most important reason is your code is easier to update and to bugfix. Let's go through a scenario together. You find a bug in the code example above. This bug consists of a first name that has whitespace around it and you do not want extra spaces in your print statement. Now, you update your code by adding `.strip()` at line 2. This solves your problem. Two months later a co-worker comes to you saying your code prints extra white spaces. you are confused because you solved the problem. However, you only changed it for first names and not for last names. This is very common mistake in large code basis. However, if you had made the code *dry* this would not have happened because there is only one place where you reformat `name`.

So, what you should learn about the example above is that *dry* coding not only means not typing the same line of code somewhere, but that it means not coding the same functionality twice. To demonstrate this let's go over the code snipped down below. This is only shows a small part of the class.

```python
class Binary():
   def __init__(self, n):
      tmp = format(n, 'b')  # This creates a binary string representation e.g. "110"
      self.bin = list(map(int, tmp))  # map applies a function to each item in a list e.g. [1, 1, 0]

   def to_int(self):
      tmp = map(str, self.bin)  # Convert each int to string e.g. ["1", "1", "0"]
      tmp = "".join(tmp)  # This joins all strings together e.g. "110"
      return int(tmp, 2)  # This converts a string to int with base two i.e. binary

   def __int__(self):
      tmp = map(str, self.bin)  # Convert each int to string e.g. ["1", "1", "0"]
      tmp = "".join(tmp)  # This joins all strings together e.g. "110"
      return int(tmp, 2)  # This converts a string to int with base two i.e. binary
```

The code above implement to methods `to_int` and the magic method `__int__`. This makes it possible to transform/cast an object of class `Binary` in two ways: `int(binary_object)` and `binary_object.to_int()`. However, similar to the previous example there are two place with the same functionality (and same code). To solve this we can make use of the magic method by altering the code as follows:

```python
class Binary():
   def __init__(self, n):
      tmp = format(n, 'b')  # This creates a binary string representation e.g. "110"
      self.bin = list(map(int, tmp))  # map applies a function to each item in a list e.g. [1, 1, 0]

   def to_int(self):
      return int(self)  # This will return the output of the magic method __init__.

   def __int__(self):
      tmp = map(str, self.bin)  # Convert each int to string e.g. ["1", "1", "0"]
      tmp = "".join(tmp)  # This joins all strings together e.g. "110"
      return int(tmp, 2)  # This converts a string to int with base two i.e. binary
```


## Grading

The first 5 points are given for:
- merge sort should be implemented recursive. (2 points)
- Default merge sort should be done by comparing objects (not attributes of objects or the return of methods) (1 point)
- You should be able to reverse sort using the default key. (1 point)
- When a `person` class object is printed it should show you the information of the object in a readable way. Thus, it should mention the name, weight, height, and age. (0.5 points)
- The file **names.txt** should be loaded in correctly. (0.5 points)

If the first 5 points are not implemented, no further points can be given.
- You should sort the list using the key argument in merge sort based on the: (1.5 points)
   - age
   - weight
   - height
   - name
   - indices 0, 1, 2, and 3
   - tuple or list representation of a `person` object
   - An index of the tuple or list representation
- You should be able to reverse sort in combination with any key argument. (0.5 points)
- A person object should also contain the following: (1.5 points)
  - The string representation of `person` objects should be the name.
  - The int and float representation of `person` objects should be the age.
  - It should be possible to get a tuple or list representation of `person` objects. When this is done the order should be: name, age, weight, height.
  - Similarly, a `person` object should be subscriptable in the same order. For example, `person1[0]` should give the name of the object `person1`.
- Dry coding. (1.5 points)

## Tips

This assignment is structured such that everything is connected and you only have to implement each functionality once. Making sure your code is dry can help you significantly to make the assignment easier and more structured.

Another tip is that coding is not only using control flows like `if elif else` or `while` loops but also using logic. Sometimes, you can achieve the same result using logic instead of an `if else`. For example, an argument that reverses the functionality of a function can be implemented in two ways. In the code below `exclude` change the functionality of `get_items` instead of returning a new list that only consists of `items` it returns a list without `items`. In the first code block `if else` is used. In the second codeblock logic is used.

```python
def get_items(lst, items, exclude=False):
   if not exclude:
      new_lst = []
      for item in lst:
         if item in items:
            new_lst.append(item)
   else:
      new_lst = []
      for item in lst:
         if item not in items:
            new_lst.append(item)
   return new_lst
```

This is not very readable code nor *dry* code. With a bit of logic we can remove the `if else` and make the code *dry*.

```python
def get_items(lst, items, exclude=False):
   new_lst = []
   for item in lst:
      if item in items ^ exclude: #  ^ stands for the logic operator XOR. Make a truthtable and test it yourself, that it is correct.
         new_lst.append(item)
```

## Delivery

Once you are sure about your program, save a copy of your `.py` file with your **student number** and the **assignment number** as the file name. For example, if your student number is 123456, then save your copy as `123456_4.py`.

If your program consists of multiple files, then compress these into a `.zip` file with the same naming scheme: `123456_4.zip`. Please make sure to **not** include your `venv` folder if you do this. Your submission should not be larger than 50kB.

Next, upload your `.py` or `.zip` file on [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322) under "Assignments" > Assignment 4 - ... .
