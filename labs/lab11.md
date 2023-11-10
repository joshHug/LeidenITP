---
layout: minimal
title: Lab 11
description: &desc 24 November, 2023 - Comprehensions & Visualization
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

Welcome to week 12, lab 11!

## PyCharm recap

This week we continue using PyCharm and running code in the terminal. In [lab 7](https://joshhug.github.io/LeidenITP/labs/lab7/) you can find information about: installing anaconda, opening projects, configuring unittests, reading unittests results, and debugging.

## Overview of This Lab

This week we have ... different exercises that range in difficulty:
 * Exercise 1: [Filter, Map & List Comprehensions]() (standard)
   * Exercise 1a: [Filter]() (standard)
   * Exercise 1b: [Map]() (standard)
   * Exercise 1c: [Combining filters & maps]() (challenge: medium)
 * Exercise 2: [Other Comprehensions]() (challenge: medium)
 * Exercise 3:

All students, regardless of experience, should be able to complete the ... standard exercises. Whether you complete all ... is up to you.

The ... exercises marked as "challenge" provide additional practice for interested students. We believe that any student in this class who completes the standard exercises should be able to complete the "medium" difficulty challenge.

For more advanced students, you might find the more difficult ... exercises to be more interesting. Feel free to skip the standard exercises if you think they are insufficiently challenging. You can also look at previous labs for challenging exercises.

If you feel that this week's challenges are too hard for you, feel free to do a challenging exercise from last week which should be easier now that you know more.

## Exercise 1: Filter, Map & List Comprehensions (standard)

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

### Exercise 1a: Filter (standard)

The concept of a filter is a bit self-explanatory, it filters which items from an iterable are kept and which are discarded. Filters keep items based on a function applied to the item, if it returns True the item is kept otherwise it is discarded. This means that `filter` need two inputs: a function and an iterable. They return an iterator that return the filtered object one by one.

Filters are connected to list comprehensions because you can also filter lists with list comprehensions. When you want to use a list comprehension as a filter, you can use an if statement after the for loop part. This can be visualized like this:

![image](/LeidenITP/assets/images/lab11/comprehension_f.png)

Thus, the following code is a list comprehension that works as a filter.

```python
filtered_lst = [v for v in original_lst if ...]
```

This is comparable with the following code:

```python
filtered_lst = []
for v in original_lst:
    if ...:
        filtered_lst.append(v)
```

Now, open `filter.py` and follow the instructions. In this exercise, we will start implementing a filter behavior using for loops and a new lists. Each successive function has the same behavior but asks you to code it a bit different to work slowly towards using the `filter` function.

### Exercise 1b: Map (standard)

The concept of a map is less self-explanatory but in the context of the course foundations of computer science a map is similar to a function, where it maps one set of value/objects to another. In other words, map takes each item in a list and applies a function to that object which creates a new list of equal length. Therefore, `map` needs the same inputs as filter: a function and a iterable. The only difference is how the function is used.

Maps are also connected to list comprehensions because you can also use list comprehensions to get the functionality of map. When you want to use a list comprehension as a map, you can apply any function to part before the for loop, e.g., `[v**2 for ...`. Below, you can find a visualization:

![image](/LeidenITP/assets/images/lab11/comprehension_m.png)

Thus, a mapping can be achieved with the following code:

```python
mapped_lst = [func(v) for v in original_lst]
```

This is comparable with the following code:

```python
mapped_lst = []
for v in original_lst:
    mapped_lst.append(func(v))
```

Before, we continue with practicing, let's examine a common confusion/mistake when turning normal `for` loops into list comprehensions. The problem arises when `if` statements are not used as filters but as maps. This happens when you have an `if else` statement that both append to the list. See below for an example:

```python
new_lst = []
for v in original_lst:
    if ...:
        new_lst.append(func1(v))
    else:
        new_lst.append((func2(v))
```

When turning such a `for` loop into a list comprehension it is better to use substitution and think about map functions and filter functions. In the example above the `if else` statement can be substituted with an new function. Thus:

```python
def new_func(v):
    if ...:
        return func1(v)
    return func2(v)

new_lst = []
for v in original_lst:
    new_lst.append(new_func(v))
```

Alternatively, it can be written as a Ternary statement, see lab 7 [Ternary Operator](). 

```python
new_lst = []
for v in original_lst:
    new_value = func1(v) if ... else func2(v)  # These two lines of code can be combined into one.
    new_lst.append(new_value) 
```

This would result in the following list comprehension:
```python
new_lst = [func1(v) if ... else func2(v) for v in original_lst]
```

Now, open `map.py` and follow the instructions. In this exercise, we will start implementing a map behavior using a for loops and a new lists. Each successive function has the same behavior but asks you to code it a bit different to work slowly towards using the `map` function.

### Exercise 1c: Combining filters & maps (challenge: medium)

Now, that we have seen both filters and maps, we can also combine them in a list comprehension. There, is no equivalent python function to do this but you could chain filter and map as follows `map(func1, filter(func2, lst))`. Here, we first filter and then map which is more efficient but the other way around would also work. An example of a list comprehension that is a filter and map at the same time would be:

```python
altered_lst = [func(v) for v in original if ...]
```

This is equivalent to the following code:

```python
altered = []
for v in original:
    if ...:
        altered.append(func(v))
```

Again, a visualization can be made where each part in the for loop goes in the list comprehension:

![image](/LeidenITP/assets/images/lab11/comprehension_m_f.png)

`if` statements can be even more confusing when combining maps and filters into a list comprehension. Let's examine the example below:

```python
new_lst = []
for v in original_lst:
    if condition1:
        continue

    if condition2:
        new_lst.append(func(v))
    else:
        new_lst.append(v)
```

Again, here the `if else` statement can better be written as a ternary statement or a separate function, in other words a mapping, while the `if continue` statement must be seen as a reverse filter. This leads to the following list comprehension:

![image](/LeidenITP/assets/images/lab11/comprehension_m_f2.png)

Now, open `combine_map_and_filter.py` and follow the instructions. In this exercise, we will start implementing a map and filter behavior using a for loops and a new lists. Each successive function has the same behavior but asks you to code it a bit different to work slowly towards using the combination of `filter` and `map` function.

## Exercise 2: Other Comprehensions (challenge: medium)

List comprehensions are probably the most used comprehension, however, in this exercise, we will look at other comprehensions. There are three other types of comprehensions: sets, dictionaries, generators. There are no tuple nor string comprehensions because of their immutable nature. Later, we will discuss how to use effectively make them. 

#### *Set Comprehensions*

Set comprehensions are maybe the most similar to list comprehension, where the only difference is that a set comprehension generates a set and has therefore unique items. Similar as creating a new set (with items) a set comprehension can be recognized and created with curly brackets `{...}`. **Important note**, an empty set can not be created with curly brackets `{}` as that syntax is already reserved for empty dictionaries. However, similar to other datastructures such as lists and dictionaries it can be created using `set()` with no argument. Below, you can find an example of a set comprehension. 

```python
new_set = {v for v in iterable}
```

Set comprehensions work similar to list comprehensions in th way that they also have a filter and map option: 

![image](/LeidenITP/assets/images/lab11/comprehension_set.png)

#### *Dictionary Comprehensions*

Similar to set comprehensions, dictionary comprehensions are created using curly brackets `{}`. The difference is that a dictionary comprehension needs a key value pair, similar to creating a dictionary like `{"A": 1, "B" : 2}`. Below, you can find an example of a dictionary comprehension. Note, that for simplicity we used key value pairs that are the same, but in "real" code you either walk over two iterables with for example `zip` or you apply a function to value or key.

```python
new_dict = {v: v for v in iterable}
```

Unsurprisingly, dictionary comprehensions also have a filter and map function, however, because we need a key and value, there are actually two map functions: one for the key and one for the value. Below, an example where we loop over two iterables, one for the keys and one for the values.

![image](/LeidenITP/assets/images/lab11/comprehension_dict.png)

#### *Generator Comprehensions*

The most versatile comprehensions of all is the generator comprehension. It can also be seen as the "mother" of all comprehensions that do and do not exist. First, lets have a look at how to construct one and how they work. A generator comprehensions is created similar to a list comprehension but with round brackets `()`. For example:

```python
new_generator = (v for v in iterable)
```

Ofcourse a generator comprehension has also a map and filter functionality. Fun side note, `filter` and `map` are generators. Thus, the following code are identical:

```python
new_generator1 = map(map_func, filter(filter_func, iterable)) 
new_generator2 = (map_func(v) for v in iterable if filter_func(v))
list(new_generator1) == list(new_generator2)  # This is true, list is needed as generators can not be compared.
```

While, a generator comprehension looks similar to the other comprehensions there is one major difference, generators are not a data structure, but more a function as we have seen before when making them. Their use is therefore similar to other generators, which makes them good for use in for loops or to create datastructures. For example, the generator `range` is often used for this purpose. This means that we can create a list, dictionary, set, string, tuple, etc. by just using a generator comprehension and convert it to specified type. Note, less general code is better, so if you want a list and you can use a list comprehension use that and not a generator comprehension. Below, you can find some example on how a generator comprehension can be used. Note, that the round brackets can be removed if used directly in a function.

```python
new_lst    = list(v for v in iterable) 
new_tuple  = tuple(v for v in iterable)   
new_string = ''.join(v for v in iterable)  # iterable must contain strings
new_set    = set(v for v in iterable)
new_dict   = dict((v,v) for v in iterable) # This creates a dict equal to {v: v for v in iterable}

# Ofcourse this does not make any sense, unless you also apply a filter or map.
for item in (v for v in iterable):
    ...

# Do not use this unless necessary, but the point is you can EFFICIENTLY make anything using a generator comprehension.
new_array  = np.fromiter((v for v in iterable), float)  # You must know the type
```

Now, open `other_comprehensions.py` and follow the instructions. 

## Exercise 3: 

Explain:
 * The plots:
   * plot
   * bar
   * hist
   * scatter
   * imshow
 * matplotlib features:
   * xlim, ylim
   * legend
   * xticks
 * loading and saving data with numpy

Make the following images:

![image](/LeidenITP/assets/images/lab11/programming_time.png)




matplotlib (plt.plot, plt.bar, plt.hist, plt.scatter, plt.imshow)

* line plot: fill-in between lines, language trough time https://pypl.github.io/PYPL.html
* bar plot: most popular programming langauge https://pypl.github.io/PYPL.html, lab 9 Exercise 3c: Displaying dictionaries with counts
* scatter plot: random noise x,y;  sklearn.datasets.load_iris
* histogram: alcohol, in wine sklearn
* imshow: MNIST


