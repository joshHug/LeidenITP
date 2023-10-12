---
layout: minimal
title: Lab 6
description: &desc 12 October, 2023 - Trickier Problems
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

Welcome to week 6!

## PyCharm

Starting this week, we're saying goodbye to CodingBat. From now on, we'll be using PyCharm to write and test all of our code.

In this lab, we'll be using and combining all of the techniques and syntax we've seen from labs 1 through 5.

### Installing Anaconda

To be better prepared for future exercises, we need more than the standard python library that was included with the PyCharm installation. While it is possible to install extra libraries one at the time, it is easier to install the most common libraries all at once into what is called a "python environment". We will do this by installing  a tool called[anaconda](https://www.anaconda.com/download). Go to the page, scroll down, choose your operating system and download anaconda. After downloading, run the installer and follow the instructions.

### Open Project

Start by downloading the .zip file for this week's code [at this link](). Unzip the file.

Now open PyCharm and select open and select the folder you just created (when unzipping). To work with the new conda environment, that we just installed, go to the lower corner of your screen where it says */home/user/current_python_installation*. Click on it and select **Add New Interpreter** -> **Add Local Interpreter**. This should look like the image below.

![images](/LeidenITP/assets/images/Add_interpreter.png)

Next, you will see a screen similar to the screenshot down below. At the left side of the popup screen click on **conda environment**. Then it should already be on **use existing environment** but if not click that radiobutton. Now, click on **ok** and from now you should program in this environment.

![images](/LeidenITP/assets/images/Interpreter.png)

## Exercise 1: Trying Out Our New Pycharm Environment

Try opening `lab6_intro.py`. Click the "run" button in PyCharm and you should see several yellow x's appear. This is because the code we currently have provided in `lab6_intro.py` is not correct.

Modify the `squared_plus_one` function so that it is correct and try running the tests again. Make sure to remove the line that says ` raise NotImplementedError("Complete the code in this function")`. The yellow x for `TestSquaredPlusOne` should be gone, leaving only the yellow x for `TestRemoveLastItem`.

Lastly, modify the `remove_last_item` function so that it is correct, and try running the tests again. You should get a green check mark, indicating you've passed all of the tests. You're ready to move on to this week's exercises.

## Overview of This Lab

In addition to the warmup exercise earlier, this week we have 6 different exercises that range in difficulty:
 * Exercise 2: conversion2D_1D (standard)
 * Exercise 3: enumerate (standard)
 * Exercise 4: helper_functions_side_effects (standard)
 * Exercise 5: scrabble (challenge, medium)
 * Exercise 6: fibonacci (challenge, hard)
 * Exercise 7: add (challenge, very hard)

All students, regardless of experience, should be able to complete the three standard exercises. Whether you complete all three is up to you.

The three exercises marked as "challenge" provide additional practice for interested students. We believe that any student in this class who completes the standard exercises should be able to complete the "medium" difficulty challenge, which builds on scrabble from an earlier lab.

For more advanced students, you might find the more difficult `fibonacci` and `add` exercises to be more interesting. Feel free to skip the standard exercises if you think they are insufficiently challenging. 

## Exercise 2: conversion2D_1D (standard)

To get more practice with basic Python, we're going to write some code that works on lists that contains lists. For example, consider the list `x = ["cat", 5, ["dog", "cow", "kaas", "koe"]]`. This list has 3 items. `x[0]` is the string "cat". `x[1]` is the number 5. `x[2]` is also a list, in this case of length 4.

Open `Conversion2D_1D.py` and work your way through the exercises.

## Exercise 3: enumerate (standard)

The `enumerate` function in Python allows us to loop over an iterable (such as a list) and return both the item and the index. In other words `enumerate` creates an iterator that returns for each item their index. Later in the course, we go in more detail about iterators but for now you can just use it like this `for i, item in enumerate(...):`. This is also the most common way enumerate is used and the preferred way to get the index of an item instead of `for i in range(len(...)):`.

Furthermore, this exercise focus on creating new lists, lists in lists, and dictionaries.

Open `enumerate.py` and work your way through the exercises.

## Exercise 4: helper_functions_side_effects (standard)

In lecture, we discussed the idea of functions having side effects. Consider this function:

```python
def set_element_zero_no_side_effects(lst):
   copy_of_lst = lst.copy()
   copy_of_lst[0] = 4
   return copy_of_lst
```

It sets element 0 to 4 with no side effects. To see this in action, go to [this link](https://cscircles.cemc.uwaterloo.ca/visualize#code=def+set_element_zero_no_side_effects(lst)%3A%0A+++copy_of_lst+%3D+lst.copy()%0A+++copy_of_lst%5B0%5D+%3D+4%0A+++return+copy_of_lst%0A%0Alst+%3D+%5B%22alpha%22,+%22beta%22,+%22gamma%22%5D%0Anew_lst+%3D+set_element_zero_no_side_effects(lst)%0Aprint(lst)%0Aprint(new_lst)&mode=display&raw_input=&curInstr=0) and step through the code as it runs. You'll see that `set_element_zero_no_side_effects` has no effect on `lst`, i.e. it creates a totally new copy and `lst[0]` remains `"alpha"`.

By contrast, the function below is dangerous. While it is correct, it also has the side effect of changing `lst`.

```python
def set_element_zero_no_side_effects(lst):
   lst[0] = 4
   return lst
```

To see this in action, go to [this link](https://cscircles.cemc.uwaterloo.ca/visualize#code=def+set_element_zero_no_side_effects(lst)%3A%0A+++lst%5B0%5D+%3D+4%0A+++return+lst%0A%0Alst+%3D+%5B%22alpha%22,+%22beta%22,+%22gamma%22%5D%0Anew_lst+%3D+set_element_zero_no_side_effects(lst)%0Aprint(lst)%0Aprint(new_lst)&mode=display&raw_input=&curInstr=0) and watch carefully to see what happens as the code runs.

In this exercise, we'll explore this idea more carefully.

## Exercise 5: scrabble (challenge, medium)

The last exercise that any student should be able to solve, at this points, is `scrabble.py`. In this exercise, we continue with the scrabble exercise from last week, but now we are no longer dealing with one word but with a sentence (i.e. a list of strings). 

In this exercise, we will focus on summation, creating dictionaries, and searching.

Open `scrabble.py` and work your way through the exercises.

## Exercise 6: fibonacci (challenge, hard)

Fibonacci.py contains some additional exercises that involve creating the [fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence). This will be the first exercise where using help functions could be useful. Furthermore, the exercise focus on creating lists and lists in lists. 

If you don't think a hard challenge is something for you try to solve the first function `def fibonacci_sequence(n):`, which is a normal difficulty function. Later on we will come back to the fibonacci sequence when we discuss recursion and it is helpful if you have seen the sequential variant first.

## Exercise 7: add (challenge, very hard)

This week we've included one especially challenging exercise. This involves adding [binary numbers](https://en.wikipedia.org/wiki/Binary_number) together. This challenge involves string to lists and vise versa and building new lists with several if-statements.




