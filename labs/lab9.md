---
layout: minimal
title: Lab 9
description: &desc 10 November, 2023 - Classes & Errors
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

Welcome to week 10, lab 9!

## PyCharm recap

This week we continue using PyCharm and running code in the terminal. In [lab 7](https://joshhug.github.io/LeidenITP/labs/lab7/) you can find information about: installing anaconda, opening projects, configuring unittests, reading unittests results, and debugging.

## Overview of This Lab

This week we have ... different exercises that range in difficulty:
 * Exercise 1: [Fix the code]() (standard)
 * Exercise 2: [Sequence iterators & generators]() (standard)
 * Exercise 3: [Counting with dictionaries]() (standard)
   * Exercise 3a: Counting with dictionaries (standard)
   * Exercise 3b: Counting with defaultdicts (challenge, medium)
 * Exercise 4: []()


All students, regardless of experience, should be able to complete the ... standard exercises. Whether you complete all four is up to you.

The ... exercises marked as "challenge" provide additional practice for interested students. We believe that any student in this class who completes the standard exercises should be able to complete the "medium" difficulty challenge.

For more advanced students, you might find the more difficult ... . Feel free to skip the standard exercises if you think they are insufficiently challenging. You can also look at previous labs for challenging exercises.

If you feel that this week's challenges are too hard for you, feel free to do a challenging exercise from last week which should be easier now that you know more.

## Exercise 1: Fix the code (standard)

In this exercise the code is already coded. However, there is a problem it does not pass all unittests. It is up to you to make the code work. To do this you are only are allowed to use `try except` statements. 

Open exercise `fix_the_code.py` and fix the functions.

## Exercise 2: Sequence iterators & generators (standard)

## Exercise 3: Counting with dictionaries (standard)

In this exercise, we will have a look how to construct a dictionary that counts objects. There are many ways to implement this, however, some are more clear or faster than others. Also, you can sometimes find some bad suggestions on forums where they suggest code that was used in python2 and later was deprecated in python3. For example, the `dict.has_key()` method does no longer exist. Here, we will go over four different (and most used) solutions when dynamically filling a dictionary with keys and values.  

The problem when dynamically filling a dictionary is that you do not know if a key exist or not, therefore the following code will break and throws the error KeyError on the third line because the key `"d"` does not exist (yet).

```python
dct = {"a": 1, "b": 2}
dct["a"] += 1
dct["d"] += 1
```

The most used solution is to check with an `if` statement if the key exist or not. If it exist you just add one to the count, otherwise, you create the key and set in on one. The problem is that it is not immediatly clear what the intent of the code is. After all, after a `if` statement can be anything.

```python
if item not in dct:  # Test if the key "item" exists in the dictionary "dct".
    dct[item] = 1  # Create the key
else:
    dct[item] += 1  # Increment the value of the key
```

Possibly, a bit cleaner code can be created using the `dct.get(key, defaultvalue)` method. The advantage of using `get` is that it works the same as using square brackets `[]`, but if they key does not exist it returns the default value. This code is commonly used if you are only interested in getting a value but not changing it. The code below is therefore a bit clunky. 

```python
dct[item] = dct.get(item, 0) + 1
```

The last option before using extra libraries is to just let the code crash on purpose. The upside is, it is fast and clear what you want to do. The downside is that some people don't like to use `try except` when it is not needed. The idea is that you just try the code you want to execute namely incrementing the value and when it fails you create the key, see below.

```python
try:
    dct[item] += 1
except KeyError:
    dct[item] = 1
```

Lastly, you can use a `defaultdict` from the library collections. This library has some very helpful datastructures. The idea of a `defaultdict` is that you expect that you will come across keys that don't exist, but they should always be initiated the same way. In other words, they all should have the same default value. When using a `defaultdict` you do not need to change the increment code, but you give the dict a default value when creating the dict. The advantage is that this generates the cleanest and most readable code. However, there is one caveat. The outcome is not the same as the three other solutions because a `dict` is not the same type as a `defaultdict`. Also, the default is a bit more complicate then with `.get()`. A `defaultdict` has as default either a type with a boolean value false or function that return a default value. For example, a `defaultdict` with as default `str` gives new keys an empty string (`""`) as value.

```python
from collections import defaultdict  # import defaultdict from collections
dct = defaultdict(int)  # creating the default dictionary with as default value the false value of an int (0). 
dct[item] += 1  # you can just increment the item, if it does not exist it will be created.
```

### Exercise 3a: Counting with dictionaries (standard)

In this exercise, you will be given a list of names and your job is to write a piece of code to count for each letter how many times it is used, open exercise `has_key.py` and complete the function `count_letters`.

### Exercise 3b: Counting with defaultdicts (challenge, medium)

Exercise 3b has the same purpose as 3a only now you are asked to use a `defaultdict`. Open exercise `has_key.py` and complete the function `count_letters_default_dict`.

### Exercise 3c: Displaying dictionaries with counts (challenge, hard)

In this exercise, you will plot for each letter how many times it is used in the file `names.txt`. The plot should be in alphabetically order. Below you will find an image how it should look like. Colors are not mandatory nor the colorbar is mandatory. Keep in mind that both add additional challenge. Open exercise `has_key.py` and complete the script or the main function.

![image](/LeidenITP/assets/images/lab9/letters_used_in_names.png)

Hint: Use `plt.bar` from matplotlib.pyplot (this commonly import as `import matplotlib.pyplot as plt`). To get different colors, you can either add 26 colors or you can use a cmap (get_cmap) as function and use the values (counts) to calculate the colors. For the colorbar, you could use ScalarMappable in combination with `plt.colorbar`. Note, that there are probably many ways to create the plot.

## Exercise 4:












