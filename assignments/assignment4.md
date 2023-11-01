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

# Assignment 4: Recursive Merge Sort & Creating Classes

**Deadline: ... 2023 23:59**

Hand in your assignment via [Brightspace](...) TODO. See the "Delivery" section for instructions.


## Program

In this assignment, you will implemented merge sort and create your own `Person` class. 

### Merge sort

Merge sort is a common sorting algorithm known for its recursive algorithm. The idea of mergesort is to split a "long" unsorted list into two equal parts and sort those list separately. The question: "how do you sort those smaller lists" can be answered with: "apply mergesort again". This is possible as the input for merge sort is an unsorted list and the output a sorted list. This first step of merge sort stops when the list is sorted. This happens when it only contains 1 item. The first step of the algorithm will look something like:
```
[0, 8, 3, 2] # this list becomes
[0, 8] and [3, 2] which is again split into
[0], [8], [3], [2] which are four sorted lists.
```
The second step is combining the list in such a way that they stay sorted. Just adding them back together would not work as this will just create the input list again. Even though, it looks like we did not make much progress as we now have to combine two list in sorted order. We actually made the sorting much easier as we know that those list themselves are sorted. Firstly, let's look at how combing would look like in an example. Secondly, we will discuss potential algorithm to achieve this.
```
Combine [0] and [8]
0 is smaller thus the new list becomes: [0, 8]
Next, combine [3] and [2]
2 is smaller thus the new list becomes: [2, 3]
Now, combine the newly created lists:
The first items of both lists are 0 and 2, 0 is smaller then 2 thus add zero: [0]
The next item of the first list is 8 which is larger then 2 thus add two: [0, 2]
The next item of the second list is 3 which is smaller then 8 thus add three: [0, 2, 3]
There are no items left in the second list, 
therefore add all remaining items from the first list: [0, 2, 3, 8]
Note, this is possible because both lists were ordered.
There are no more lists to combine thus merge sort is complete. 
```

The example shows a hint of how the algorithm works. In one sentence it can best be described as zipping the list together based on which item is smaller. In this assignment, you will implement this second step in the function `merge`. Here, you have two options. 

Algorithm 1, you loop through the lists using two indices e.g. `i` and `j`. Then each step you look if the first list with index `i` is smaller than the second list index `j`. If so add the value of the first list index `i` and increment `i` by one. Else, you do the opposite, add the value of the second list index `j` and increment `j` by one. When either `i` or `j` is out of bounds of their respective list, you can stop and add the rest of the remaining list to the new list.

Algorithm 2, you take always the first item of each list. Then compare the values and add the smallest value to the new list. From the lists that you took the value (with the smalles value) you will remove the first index. Keep going until one list is empty. Now, you can stop and add the rest of the remaining list to the new list.

In the next course, algorithms and data structures you will learn all about when which algorithm is better and why. For this assignment, you only have to implement a working solution.

For more information visited [this](https://nl.wikipedia.org/wiki/Mergesort) wikipedia page. Hint: try to implement the algorithm yourself and not look at the provided code. Copying code from anywhere is not allowed and it is hard to create your own code if you have seen the solution.

### Person class

When storing data, you often want to store more than one datatype per object. For example, you want to store a persons name and age. Now, it would be possible to make two lists: one for the names and one for the ages. However, this is a very bad idea. One major problem is that this can easily lead to misaligned data e.g. the first name in list one does no longer corresponds to the first age in list two. Therefore, we need a different solution which is often a [tuple](https://www.geeksforgeeks.org/tuples-in-python/) or a [named tuple](https://www.geeksforgeeks.org/namedtuple-in-python/). Even though this is a good way to store data if we want to add special methods to such data we need our own class. In this assignment, you will create a class `Person` which has similar functionality to named tuples and more. For example, both are subscriptable meaning you can use square brackets `person_object[0]`. In the template and grading criteria you can find a list with all the functionality that this class needs.

Each `Person` object should be randomly initialized with:
- A name from the global list `NAMES`.
- An age between 18 and 100.
- A height between 150 and 200 cm.
- A weight between 45 and 100 kg.

### Sorting Own Objects

At this point, we know how to sort a list of integers and why we need a class. However, when making an application it is often required that this new data class is also sortable. In this assignment you will do this in two ways. The first approach will be to make the object sortable. This means that the sorting algorithm code does not change compared to sorting integers. The second approach would be to use the default `key` argument in merge sort. The `key` argument makes it possible to sort objects differently by applying a function to a object an sorting the return of this function. This way it is for example possible to sort on the second character in a list or to sort on a certain attribute (which is sortable) of an object. In this assignment, you will for example sort the person objects based on their name using the `key` argument.

Another argument that most sorting algorithm have is the default `reverse` argument. This argument makes sure that the list is sorted in reverse order. 

Lastly, your implementation of merge sort and the two default arguments should work in any combination.  

## Template

The template for this assignment consists of 3 files: `merge_sort.py`, `person.py`, and `load_names.py`. While it is not mandatory to use these files, it is highly recommended. In the files, you can also find more information what to do where. You are allowed to add more functions.

In this assignment, it is not allowed to use any hidden/private object attributes. A hidden/private object attribute in python can be recognized by a dubbel underscore e.g. `object.__height`. In many programming languages it is not possible to access these attributes outside the class. The reason for this is that the unspoken agreement is that class method should not change (get/set), but how a class internally works can be changed completely. This means that if you use hidden/private variables and the class gets updated, your code is likely to break. While it is possible in python to use any attribute of any object, it is not recommended for the same reason.

### Merge Sort

In `merge_sort.py`, you will implement recursive merge sort and you will write a small script where you sort a list with `Person` objects in the following ways:
- Without default arguments, for the `Person` class this means that the list is ordered from the shortest person to the tallest person. In other words, they are sorted in their default order.
- Reversed by using the default argument reverse.
- With the default argument key, which should make sure you can sort a `Person` object any way you like and at least using all possibilities described in the grading criteria.
- A combination of reverse and key default arguments.

The script should print the list at least sorted in all possible ways listed in the grading specification. Make sure when you print the list sorted in a certain way that it is clear which way it is sorted. This script can either be added in `merge_sort.py` below all classes and functions or you can use a `main` function and add `if __name__ == "__main__": main()` at the bottom of the file.

### Person class

In `person.py`, you will implement the `Person` class and a create person list function. The `Person` class should contain at least the functionalities described in the grading criteria. The `__init__` method is already given and it is not allowed to create any other new object attributes e.g. `self.some_name = ...`. The `create_persons_list` function should return a list of `Person` objects randomly initialized as described in the program section.

### Load Names

In `load_names.py` you will write code to load the file **names.txt**. The function `load_names` should return a 1D list or array with the names.

## Dry code (Don't repeat yourself)

During this assignment it is important to write *dry* code. This means that everything should only be defined once and no code should be repeated. This is more elaborated than it sounds. For example, if you have an `if` `else` control-flow and both contain a few lines of similar code then it is not dry. This could be solved by removing the similar code outside the `if` `else` control-flow or write a function that execute the same code and call in both statements the new function. Old code could look like this:
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
- Default merge sort should be done by comparing objects e.g. `Person` objects (not attributes of objects or the return of methods). When objects are equal the original order should be preserved. (1 point)
- You should be able to reverse sort using the default key. (1 point)
- When a `Person` class object is printed it should show you the information of the object in a readable way. Thus, it should mention the name, weight, height, and age. (0.5 points)
- The file **names.txt** should be loaded in correctly. (0.5 points)

If the first 5 points are not implemented, no further points can be given.
- You should sort the list using the key argument in merge sort based on the: (1.5 points)
   - age
   - weight
   - height
   - name
   - indices 0, 1, 2, and 3
   - tuple or list representation of a `Person` object
   - An index of the tuple or list representation
- You should be able to reverse sort in combination with any key argument. (0.5 points)
- A `Person` object should also contain the following: (1.5 points)
  - The string representation of `Person` objects should be the name.
  - The int and float representation of `Person` objects should be the age.
  - It should be possible to get a tuple or list representation of `Person` objects. When this is done the order should be: name, age, weight, height.
  - Similarly, a `Person` object should be subscriptable in the same order. For example, `person1[0]` should give the name of the object `person1`.
- Dry coding. (1.5 points)

## Tips

This assignment is structured such that everything is connected and you only have to implement each functionality once. Making sure your code is dry can help you significantly to make the assignment easier and more structured.

When working on `load_names.py` think about how to correctly open and close a file or load in files using other libraries.

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
