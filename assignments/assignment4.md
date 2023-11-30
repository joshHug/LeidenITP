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

**Deadline: 22 December 2023 23:59**

Hand in your assignment via [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322). See the "Delivery" section for instructions.

## Program

In this assignment, you will implemented merge sort and create your own `Person` class. 

### Merge sort

Merge sort is a common sorting algorithm known to be implemented recursively. The concept of mergesort involves dividing an "unsorted" list into two equal parts and sorting them individually. When pondering how to sort these smaller lists, the answer lies in applying mergesort again. This works because merge sort takes an unsorted list as input and produces a sorted list as output. The algorithm consists of two steps: a recursive phase that splits the lists into smaller lists and sorts them, and a merging phase that merges the sorted lists together. The initial step of merge sort stops when the list is sorted, which occurs when it contains only one item. For illustrative purposes each split is colored red for the left part and blue for the right part. An illustration of this first step of the algorithm might look something like this:

![images](/LeidenITP/assets/images/assignment4/tree.png)

The subsequent step involves combining the lists in a manner that maintains their sorted order. Simply rejoining them wouldn't work, as it would recreate the input list. However, despite the appearance of minimal progress because we're combining two lists in sorted order, this actually makes sorting much simpler due to our knowledge that these lists themselves are sorted. First, let's examine how combining would appear in an example. Then, we'll discuss potential algorithms to achieve this.

```
Combine [0] and [8]
0 is smaller, so the new list becomes: [0, 8]
Next, combine [3] and [2]
2 is smaller, so the new list becomes: [2, 3]
Now, combine the newly created lists:
The first items of both lists are 0 and 2. As 0 is smaller than 2, add zero: [0]
The next item in the first list is 8, which is larger than 2. Thus, add two: [0, 2]
The next item in the second list is 3, which is smaller than 8. So, add three: [0, 2, 3]
No items are left in the second list, 
so add all remaining items from the first list: [0, 2, 3, 8]
Note, this is possible because both lists were ordered.
There are no more lists to combine, thus merge sort is complete. 
```

This example offers insight into how the algorithm operates. In brief, it could be described as zipping the lists together based on which item is smaller. In this assignment, your task is to implement this second step in the function merge. You'll have two options:

Algorithm 1 involves looping through the lists using two indices, e.g. `i` and `j`. At each step you check if the element at index `i` in the first list is smaller than the element at index `j` in the second list. If so, add the value of the first list's index `i` to the new list and increment `i` by one. Otherwise, add the value of the second list's index `j` to the new list and increment `j` by one. When either `i` or `j` exceeds the bounds of their respective lists, stop and add the remaining list elements to the new list.

Algorithm 2 always selects the first item of each list, compares their values, and adds the smallest value to the new list. Then, it removes the first index from the list that contributed the smallest value. This continues until one list is empty. At that point, stop and add the remaining elements from the non-empty list to the new list.

In your upcoming course on algorithms and data structures, you'll learn about the contexts in which each algorithm performs better and why. However, for this assignment, your main objective is to implement a functional solution.

For more information visited [this wiki page](https://nl.wikipedia.org/wiki/Mergesort). Hint: Try to implement the algorithm yourself and do not look at the provided code. Copying code from any source is not permitted and could hinder your ability to create your own solution.

### Person class

When managing data, there's often a need to store multiple data types within a single object. For instance, you might want to retain a person's name and age. While one might consider using two separate lists – one for names and another for ages – this approach isn't advisable. An inherent issue is the potential for misalignment in data. For instance, the first name in list "one" may no longer correspond to the first age in list "two". Hence, an alternative solution is required, often in the form of a [tuple](https://www.geeksforgeeks.org/tuples-in-python/). Although a tuple is efficient for storing data, having our own class allows us to incorporate (magic) methods. In this task, you will create a Person class with several (magic) methods. The template and grading criteria contain a comprehensive list of the functionalities required for this class.

Each `Person` object should be randomly initialized with:
- A name from the global list `NAMES`.
- An age between 18 and 100.
- A height between 150 and 200 cm.
- A weight between 45 and 100 kg.

### Sorting Own Objects

At this point, we know how to sort a list of integers and why we need a class. However, when making an application it is often required that this new data class is also sortable. Sortable means that if you have two objects of your class they can be compared. This can be done by implementing the magic method for equality and either lesser than or greater than. To also be able to use `<=` and `>=` in combination with your own object in your code, you also need to implement either lesser than and equal or greater than and equal. Note, that you can use two previous implemented magic methods to do that (this must be done to keep your code dry).

After, you made the `Person` class sortable you should be able to sort it similar to how you sort a list of integers. You can also test if you implemented the magic methods correctly by using the python function `sorted(Person_object_list)`. This should give you a sorted list of `Person` objects.

### Key and Reverse Arguments

At this point, we know how to sort a list any list of sortable objects. However, sometimes we do not want to sort a list of objects on their default order. Let's say we have a list with tuples containing names and ages, see below for an example.

```python
name_age_lst = [("John", 30), ("Mary", 34), ("Christof", 40)]
```

Now, if we want to sort this list we can just use `sorted` or the `merge_sort` that you have implemented previously. The default sorting of a tuple is on the first item, therefore, both algorithm should produce the following result:

```python
>>> print(sorted(name_age_lst))
[('Christof', 40), ('John', 30), ('Mary', 34)]
```

This is nice but what if we want to sort the list based on age? We can try to flip the tuples such that we get an (age, name) tuple, then sort it, and finally flip the tuples back to their original order. However, there is an easier approach. Most sorting function have the default argument `key`. This argument makes it possible to sort a list differently then the default sorting. The default of `key` is None, which result in the default sorting. However, if we have a function that maps the object we want to sort to another sortable object then we can use that function as `key` argument. This has as result that the list is no longer sorted on the original objects but on the objected return by the `key` argument. Let's break it down in an example. Now, we want to sort the `name_age_lst` variable on the second item in the tuple, i.e, the age. First, we need a function that returns this objects, for example:

```python
def get_second_item(name_age_tuple):
    return name_age_tuple[1]
```

Now, if we apply this function to an object from the list, for example, `('John', 30)` then we get `30`. This is internally used in the sort function to instead compare the tuples compare this new object, age. This makes it possible to sort a function on age as follows:

```python
>>> print(sorted(name_age_lst, key=get_second_item))
[('John', 30), ('Mary', 34), ('Christof', 40)]
```

In this assignment, it is your job to also implement this behavior into `merge_sort` using a default `key` argument. Tip: When implementing the `key` argument think about what part of the sorting algorithm should change and what can stay the same. It is really advised to use helper function for example `compare` to implement this `key` argument. In the following example you can see how this would work and what the output should be.

```python
>>> print(mergesort(name_age_lst, key=get_second_item))
[('John', 30), ('Mary', 34), ('Christof', 40)]
```

In this assignment, you will also write a small script where you will among other things use the `key` argument to sort a list of `Person` objects in various ways.

Most sorting algorithms also include another parameter, namely the default argument `reverse`. This argument ensures that the list is sorted in reverse order. For our previous example this would look as follows:

```python
>>> print(mergesort(name_age_lst, reverse=True))
[('Mary', 34), ('John', 30), ('Christof', 40)]
```

When implementing reverse, you should not copy past the whole algorithm but think how you can alter the behavior of the code such that it works as intended. Adding an helper function to achieve this is a good idea or you can check the example in tips.

To finalize, ensure that your implementation of merge sort and the two default arguments seamlessly operate together in any configuration. For example:

```python
>>> print(mergesort(name_age_lst, key=get_second_item, reverse=True))
[('Christof', 40), ('Mary', 34), ('John', 30)]
```

## Template

The template for this assignment consists of 3 files: `merge_sort.py`, `person.py`, and `load_names.py`. It is mandatory to use these files and also it is highly recommended. In the files, you can also find more information what to do where. You are allowed to add more functions.

It is generally good practise to not uses attributes of a class outside the class. In later courses you get more details on why. For example, the following code is bad practise:

```python
person1 = Person("John", 30, 180, 80)
person1._age  # You should not do this.
```

To additionally signal to programmers that you should not use an attribute outside a class you can add one or two underscores if front of the variable name. examples can be found in the `Person` class. If you want to use, for example, `person1._age` you should make a method in the `Person` class that returns `self._age`. In this assignment, it is not allowed to use any attributes of a `Person` object outside the class `Person` itself.

### Merge Sort

In `merge_sort.py`, your task involves implementing the recursive merge sort. Before, you start sorting a list with `Person` objects check if you merge sort works on a list of integers. If your code works for sorting a list of integers and you made the `Person` class sortable than it should also work on a list of `Person` object without any adjustments to your merge sort algorithm.

In addition to implementing the merge sort algorithm, you'll create a small script to sort a list containing `Person` objects in various ways:
- Sorting without default arguments, meaning the list will be ordered from the shortest person to the tallest person, representing their default order.
- Sorting in reverse by utilizing the default argument `reverse`.
- Employing the default argument `key` to enable sorting `Person` objects any way you like, but at least according to various options which are mentioned in the grading criteria.
- Creating a combination of `reverse` and `key` default arguments for sorting.

The script should print the list at least sorted in all possible ways listed in the grading specification. Make sure when you print the list, sorted in a certain way, that it is clear which way it is sorted. For example, you first print: `Below you can find the list sorted on weight:` and then you print the list sorted on weight. This script can either be added in `merge_sort.py` below all classes and functions or you can use a `main` function and add `if __name__ == "__main__": main()` at the bottom of the file.

### Person class

In `person.py`, your task is to construct the `Person` class along with a function, `create_persons_list`. The Person class should encompass functionalities outlined in the grading criteria. It's important to note that the `__init__` method is already provided, and the creation of any new object attributes like `self.some_name = ...` is prohibited.

The `create_persons_list` function is expected to yield a list consisting of `Person` objects initialized randomly in accordance with the description given in the program section.

### Load Names 

In `load_names.py` you will write code to load the file `names.txt`. The function `load_names` should return a 1D list or array with the names.

## Dry code (Don't repeat yourself)

During this assignment it is important to write *dry* code. This means that everything should only be defined once and no code should be repeated. This is more elaborated than it sounds. For example, if you have an `if` `else` control-flow and both contain a few lines of similar code then it is not *dry*. This could be solved by removing the similar code outside the `if` `else` control-flow or write a function that execute the same code and call in both statements the new function. Old code could look like this:
```python
if check_first_name(name):
   name = name.lower()
   print(f"The first name of this person is {name}")
else:
   name = name.lower()
   print(f"The last name of this person is {name}")
```

The *dry* code can be:
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

*Implementing the basic functionality will give you 5.5 points out of 10.*
**Basic functionality**, this can be split in the following items:
- Merge sort should be implemented recursive. (2 points)
- Default merge sort should be done by comparing objects e.g. `Person` objects (not attributes of objects or the return of methods). When objects are equal the original order should be preserved. `Person` class objects should be compared/sorted on default on their height. (1 point)
- You should be able to reverse sort using the default argument `reverse`. (1 point)
- When a `Person` class object is printed it should show you the information of the object in a readable way. Thus, it should mention the name, weight, height, and age. (0.5 points)
- The file `names.txt` should be loaded in correctly. (0.5 points)
- Include comments to explain the difficult parts of your code. It is generally good practice to write a comment for each code block. (0.5 points)

*The remaining 4.5 points can only be obtained after completing the basic functionality. The following additional functionality will get you the additional 4.5 points, the grade is capped at a 10. Note, that completing the basic functionality does not mean flawless implementation. If you make a mistake in the basic functionality, you can still get additional points.*

**Sorting with key arguments**: You should sort the list using the key argument in merge sort based on the following attributes of the `Person` class: (1 point)
- age
- weight
- height
- name
- indices 0, 1, 2, and 3
- tuple or list representation of a `Person` object
- an index of the tuple or list representation

**Person Class**: A `Person` object should also contain the following: (1 point)
- The string representation of `Person` objects should be the name.
- The int and float representation of `Person` objects should be the age.
- It should be possible to get a tuple or list representation of `Person` objects. When this is done the order should be: name, age, weight, height.
- Similarly, a `Person` object should be subscriptable in the same order. For example, `person1[0]` should give the name of the object `person1`.

**Combining key and reverse** You should be able to reverse sort in combination with any key argument. (1 point)

**Dry code**: For example, each functionality in you class should only be implemented once. Another example would be, there should only be one sorting algorithm. The two arguments `key` and `reverse` can be handled in a separate helper function. (1.5 points)

## Tips

This assignment is structured such that everything is connected and you only have to implement each functionality once. Making sure your code is *dry* can help you significantly to make the assignment easier and more structured.

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

Next, upload your `.py` or `.zip` file on [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322) under "Assignments" > Assignment 4 - Recursive Merge Sort & Creating Classes.
