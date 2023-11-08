---
layout: minimal
title: Lab 10
description: &desc 17 November, 2023 - Recursion & Hashable Objects
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

Welcome to week 11, lab 10!

## PyCharm recap

This week we continue using PyCharm and running code in the terminal. In [lab 7](https://joshhug.github.io/LeidenITP/labs/lab7/) you can find information about: installing anaconda, opening projects, configuring unittests, reading unittests results, and debugging.

## Overview of This Lab

This week we have ... different exercises that range in difficulty:
 * Exercise 1: 

 * comprehensions (filter, map, combo, others)
 * matplotlib (plt.plot, plt.bar, plt.hist, pls.imshow)

All students, regardless of experience, should be able to complete the ... standard exercises. Whether you complete all ... is up to you.

The ... exercises marked as "challenge" provide additional practice for interested students. We believe that any student in this class who completes the standard exercises should be able to complete the "medium" difficulty challenge.

For more advanced students, you might find the more difficult ... exercises to be more interesting. Feel free to skip the standard exercises if you think they are insufficiently challenging. You can also look at previous labs for challenging exercises.

If you feel that this week's challenges are too hard for you, feel free to do a challenging exercise from last week which should be easier now that you know more.

## Filter, Map & Comprehensions

Before, we explain what filters, maps, and list comprehensions are it is important to understand why we use them. The functionality of all three can be achieved by initializing a new list and while looping the original list adding elements to it. This would look something like:

```python
new_lst = []
for v in orginal_lst:
    # do something
    new_lst.append(v)
```

However, the downside of this approach is that it is not clear what the code does especially if there are multiple if statements in the for loop that alter what is added to the new_lst. Also, it might not be clear at a first cleanse what you code should do at all. Therefore, we like to use code blocks or coding concepts that clearly signal what the intent of the code is. For example, a filter can only discard items from an iterable not changes them or add new. 

### List comprehensions

List comprehensions are a general way to signal that you want to create a new list based on another list. You can also see them as shorthand for code we wrote above whereby writing the for loop in the square brackets we get the same behavior as creating a new list and appending the items to it. Below, you will see visualization of this idea.

![image](/LeidenITP/assets/images/lab11/comprehension.png)

Before, we go in to detail how to construct a list comprehension that does more than create the same list, let's go over what filter and map do and how they are connected to a list comprehension. This will also answer the question: how to use list comprehensions.

### Filter

The concept of a filter is a bit self-explanatory, it filters which items from an iterable are kept and which are discarded. Filters keep items based on a function applied to the item, if it returns True the item is kept otherwise it is discarded. This means that filters need two inputs: a function and an iterable. They return an iterator that return the filtered object one by one.

Filters are connected to list comprehensions because you can also filter lists with list comprehensions. When you want to use a list comprehension to filter you can use an if statement after the for loop part. Thus:

```python
filtered_lst = [v for v in original_lst if "some condition"]
```

This is comparable with the following code:

```python
filtered_lst = []
for v in original_lst:
    if "some condition":
        filtered_lst.append(v)
```


Now, open `filter.py` and follow the instructions. In this exercise, we will start implementing a filter behavior using for loops and new lists. Each successive function has the same behavior but asks you to code it a bit different to work slowly to using the `filter` function.

