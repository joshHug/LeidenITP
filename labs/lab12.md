---
layout: minimal
title: Lab 12
description: &desc 1 December, 2023 - Bomb Lab
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

Welcome to week 13, lab 12!

## PyCharm Recap

This week we continue using PyCharm and running code in the terminal. In [lab 7](https://joshhug.github.io/LeidenITP/labs/lab7/) you can find information about: installing anaconda, opening projects, configuring unittests, reading unittests results, and debugging.

## Overview of This Lab

This week, the structure of the lab is a bit different. In the last 11 labs, we have covered the basic programming principles and the ways to use them in Python. It is important that you take the time to finish the previous labs and practice with each programming concept. You should only attempt this lab once you have finished all eleven of the previous labs. 

This lab is an extra special very difficult challenge which contains only one, hopefully fun, challenge exercise. This exercise will focus on the concept of control flow and how to interact with class objects. It uses a lot of very strange concepts, and solving the puzzles inside would be challenging even for a veteran programmer.

Also below, you can find an overview where you can practice certain programming concepts.

Overview programming concept and exercise:
 * Numpy: [Lab 7](https://joshhug.github.io/LeidenITP/labs/lab7/#lab-7)
 * Dictionaries: [Lab 9](https://joshhug.github.io/LeidenITP/labs/lab9/)
 * Classes: [Lab 8](https://joshhug.github.io/LeidenITP/labs/lab8/), [Lab 9](https://joshhug.github.io/LeidenITP/labs/lab9/), and [lab 10](https://joshhug.github.io/LeidenITP/labs/lab10/)
 * Iterators & Generators: [Lab 9](https://joshhug.github.io/LeidenITP/labs/lab9/)
 * Recursion: [lab 10](https://joshhug.github.io/LeidenITP/labs/lab10/)
 * Visualization: [lab 11](https://joshhug.github.io/LeidenITP/labs/lab11/)
 * Comprehensions: [lab 11](https://joshhug.github.io/LeidenITP/labs/lab11/)

[In extra exercises](https://joshhug.github.io/LeidenITP/labs/extra_exercises/), you can find useful python functions and practice implementing them yourself.

## Theoretical Background

The main goal of this exercise is to provide you a fun puzzle. However, before we start the exercise, let us go through a few coding concepts that we have seen in the past few weeks and that throughout the exercise will be used or shown. 

### Control flow

Here, we will briefly discuss what control flow is and why it is useful. Control flow refers to the order in which individual statements, instructions, or commands of a program are executed. It determines the direction of code execution based on conditions, loops, and function calls. Control flow is used to structure code, like conditionals (if, else, switch) and loops (for, while, do-while), and allow programmers to create dynamic and flexible algorithms.

Ofcourse, this is a very general statement and coding would not be possible without control flow, but the important questions is: "What is good control flow and how can thinking in control flow help to structure code?". In the section below, we will discuss this in more detail but in general the answer is: "Good control divides your code into manageable and understandable pieces". Dividing code into manageable piece can happen at different levels of abstraction. It often helps when you write code to think about these different levels and structure you code accordingly. For example, when writing code to control a robot. You can think about what it should do, for example, it should be able to move in four directions and not bump into things. This can be a high level piece of code like:

```python
def move_robot():
    if something_in_front():
        if something_to_the_right():
            go_left()
        else:
            go_right()
    else:
        go_forward()
```

Here, you do not care about how to check if you can go a certain direction or how to move. So, each level of abstraction you go in more detail about how to do something. 

### Code Blocks

Let's go back to the beginning of how to structure your code. One important concept is a code blocks. There are many variations of the definitions for the term code blocks but here we will use it as a piece of code that belongs together or in other words a piece of code that contains one control flow. A few examples of code blocks are a `if elif elif else` statement, a `for` or `while` loop, or a function. Code blocks can also help you write more readable code and structure your code. Two good guidelines are a code blocks has a docstring or a comment and has white space around it. For example, let say we want to filter something from a list and then based on if the list is empty to something or not. Even from the word "and" in the text you can see that this code consists of two code blocks. The code could look something like:

```python

# This code filters ... from the old_lst and makes a new list filtered_lst
filtered_lst = []
for item in old_lst:
    if ...:
        filtered_lst.append(item)

# Depending on if the filtered_lst contains items run it through the next step and return that or return False
if filtered_lst:
    return do_something(filtered_lst)
else:
    return False

```

As you can see in this example each code block is separated by new lines. Also, above the code block there is a comment what the code block does. Each code block contains one control flow: a `for` loop or a `if else` statement. Note, that the `if else` statement does not contain what to do when the if is true, that is put in a separate code block, namely the function `do_something`. Also note, that `filtered_lst = []` is in the code block of the for loop because it is part of the control flow (the initialization for the `for` loop).

### One Function One Purpose

This concept is part of OOP (object orientated programming) and while there are many opinions how far you should push this concept. The idea is similar to what we previously discussed,but it comes down to that basically each control flow/code blocks has its own function. While this sounds like a wonderful idea. For example, you only need docstrings for the functions and inline comments are not needed. Also, every function is relative small making it easier to debug and also your code is probably more dry (don't repeat yourself). There can be a downside where a simple piece of script (10 lines of code) now takes multiple functions to implement which makes it hard to read. For now, try to think what each function should do and add at most three control flows to it. Also, try not to nest control flows to much. For example, this was the code to count the number of letters from lab9 exercise 3 (the comments are minimal to save space): 

```python
def count_letters(names):
   """
   Count for each letter how many times it occurs in the list names.
   """
   # Control flow 1
   letter_dict = {}
   for name in names:
      for letter in name.strip().lower(): # Control flow 2
         # Control flow 3
         # Check if the letter is a letter not a number of special symbol
         if not letter.isalpha():
             continue
          
         # Control flow 3
         # Increase the count for letter in the dict
         try:
             letter_dict[letter] += 1
         except KeyError:
             letter_dict[letter] = 1
```

In this example, four control flows are nested. So, to adhere more to the idea of OOP and one function one purpose. We could rewrite as follows:

```python
def count_letters(names):
   """
   Count for each letter how many times it occurs in the list names.
   """
   letter_dict = {}
   for name in names:
      for character in name:
         update_letter_dict(letter_dict, character)

def update_letter_dict(letter_dict, character):
   """
   This function parse the character and when it is a letter updates the letter dictionary.
   """
   letter = parse_letter(character)
   
   if letter is None:
       return
   
   increment_letter_dict(letter_dict, letter)

def parse_letter(character):
   """
   This function takes a character and returns either a lower case letter or nothing.
   """
   if character.isalpha():
      return character.lower()

def increment_letter_dict(letter_dict, letter):
   """
   This function increments the letter value.
   """  
   try:
       letter_dict[letter] += 1
   except KeyError:
       letter_dict[letter] = 1
```

As said before, this is maybe too much of one function one purpose, but it is a good exercise to identify the control flows in your code and how you can structure it. Also, each piece of code is faster to understand without the need of reading comments (because function names are kind of comments).

### Classes and Interacting With Them

To continue the topic of control flow and where you need to do what. There are certain guidelines on how to work with classes and make them. One of these guidelines is that you do not change the attributes of an object outside the class. So, your class should contain all the methods needed to work with it. This is because the problem with classes and methods is that often a method relies on certain attributes of an object. Changing these attributes can easily lead to error or bugs. Therefore, classes often contain methods to change the value of an attribute (setters) or methods to get the value of an attribute (getters). To make clear to other programmers that certain attributes or methods should not be used outside the class you can add an underscore in front of your variable name. In other language, you can actually make a variable private (instead of public) to enforce this behavior, in python this is not possible. 

That methods use variables/attributes that are not given as input arguments is also where methods differ from functions. A function only uses variables that it gets as an argument or made in the function itself. A method uses the attributes of the object and the arguments only contain variables from outside the object. 

This ties needly in with our discussion about control flow, where you can change or get information about an object, but you do not write code that actually does it. An example that is common in machine learning is that you have a certain model that needs to learn something and then predict it. In these case the code looks often something like:

```python

x, y = ...   # Some data to learn from
x_new  # New data points where you want to predict the y value for.
model = Model()  # Creates the object
model.fit(x, y)  # Train the model 
y_new = model.predict(x_new)
```

As you can see you do not do any coding on how this `fit` or `predict` works. Below, you can find a real example for Linear Regression (fit a line through points).

```python
model = sklearn.linear_model.LinearRegression()
model.fit(x,y)
y_new = model.predict(x_new)
```

Thus, all the control flow to interact with an object should be in the class and not outside a class, for example, in a script. 

### Everything is an Object in Python

The last thing unrelated to control flow what we need to discuss is everything in Python is an object. This means that a variable (or attribute) can contain a reference to anything: an integer, a string, a list, a function, a class, an instance of a class, etc. For example, in the code below `var` is just a name of a function. In other words, `var` is the variable name for a callable object.

```python
def var():
    print("This is the variable var.")
```

We can also assign a different variable to var. For example, the code below would print `"This is the variable var."`.

```python
def var():
    print("This is the variable var.")

another_var = var
another_var()
```

This also means that arguments of a function can be a function, object, or any other variable. For example, the code below would also print `"This is the variable var."`.

```python
def function_with_var(func):
    func()

function_with_var(var)
```

Alternatively, a function can have a return variable that is a function. This is a topic on its own but if you want more information you can google decorators. 

A very useful way we can use callable objects or functions variable in our code is when we want to check something or run several function in sequences. For example, the code below will print twice the string: `"This is the variable var."`.

```python
func_lst = [var, another_var]
for func in func_lst:
    func()
```

## The Bomb Lab (Challenge, Hard)

In this exercise, you will help a robot to dismantling a fictional bomb under the LIACS building. The bomb is build by an overly careful programmer that tried to make sure that nobody could temper with his bomb object. This results in some very bad code, but it also makes it near impossible to use or change any attributes of the bomb object. Luckily for us, he also left a way to dismantle the bomb by executing a precise sequence of methods for the robot.

There are multiple bombs with different difficulties to make the challenge more accessible. After importing `bomb`, you can set the difficulty by calling it and use the `level` argument as show below:

```python
bomb(level=1)
```

Video solutions are provided for levels 1 and 2.

### Level 0

The `bomb` class has the following interface on all levels of the game.
 - `bomb(level=N)` starts level N.
 - `bomb.is_dismantled()` returns True if the bomb is dismantled and false otherwise.
 - `bomb.console(data)` enters the given text into the console. Example, the first step for every level is to call `bomb.console("Start dismantle bomb program.")`

### Level 1

On level 1, there are two additional new features you'll need to use:

 - `bomb.get_wires()` - returns a list of colors, e.g. `["blue", "green", "orange"]`
 - `bomb.cut_XX_wire()` - There is one function per color. We do not provide the full list of colors. You'll need to figure these out through trial and error.

 Note: After cutting all wires succesfully from a single `get_wires` call, you may need to call `get_wires` again. For example, if on the first call of `get_wires` you get `["blue", "green", "orange"]`, the bomb may or may not be dismantled yet. You'll need to check using `is_dismantled`. If it is not yet dismantled, you should call `get_wires` to get the next set of wires.

The set of colors is randomly chosen each time you play. The number of times you'll have to call `get_wires` is randomly chosen each time you play.

For a video demo giving a solution for level 1, see: []().

### Level 2

On level 2, there are three new thing you'll need to consider.
 - `bomb.get_wires()` - returns a list of colors just like level 1, e.g. ["blue", "green", "orange"], but only if the next step is to cut wires. If the next step is NOT to cut wires or the bomb is dismantled, then a `BombStartsBeeping` exception occurs, which you should catch to keep the game running.
 - `bomb.get_cipher()` - returns a list of numbers that must be entered into the console, e.g. could return `[3, 1, 5, 9]`, which would require calling `bomb.console(3)`, then `bomb.console(1)`, and so forth. This only happens if the next step is to enter codes into the console. If the next step is NOT to enter numbers into the console or the bomb is dismantled, then a `BombStartsBeeping` execption occurs, which you should catch to keep the game running.
 - There is no way to ask the bomb directly whether the next step is to cut wires or enter codes. You must use trial and error with `get_wires` and `get_cipher`. Note that once the bomb is dismantled, both `get_wires` and `get_cipher` will cause the `BombStartsBeeping` exception.

Like all other levels, the wires and codes are random each time you play.

For a video demo giving a solution for level 2, see: []().

### Level 3

Same as level 2, except that:

 - `bomb.get_cipher()` - Instead of a list, will now sometimes return a nested list, e.g. `[1, 2, [3, 4], [[20, 30], 7, 8], 9]`, in which case you should now enter the numbers 1, then 2, then 3, then 4, then 20, then 30, then 7, then 8, then 9, in that order. There is a clever way to do this.

### Level 4

Level 4 has these four new functions.

 - `bomb.get_part()` - gets a part to be removed.
 - `bomb.get_screws()` - gets a list of screws that must be removed. This must be called immediately AFTER `get_part`, but before `remove_part`.
 - `screw.remove()` - removes a given screw. Note that this is a function of the screw object, not the bomb.
 - `bomb.remove_part(part)` - removes the given part.

Note that for this part, there are now four different functions you may need to call in order to dismantle the bomb: `get_wires`, `get_cipher`, `get_screws`, and `get_part`. You'll need to come up with some way to iterate over these four functions. Hint: To avoid a messy solution with lots of `try`/`except` statements, keep in mind that you can make lists or even dictionaries of functions.

### Level 5

To be able to complete the last level the robot needs to enter a secret password.

The new attributes for this part are:
 - `bomb.get_encrypted_password()` - gets the encrypted password that needs to be input.
 - `bomb.insert_password(password)` - provide the solution to the encrypted password given by `get_encrypted_password`
 - `bomb.get_clue()` - gives a clue to help compute the password.

The password can be decrypted by applying one of four sequences, that we saw in previous labs, to the encrypted password. The four sequences are: fibonacci, padovan, triangular, and factorial. So let say the encrypted password is `[4,2,7,0]` and the fibonacci sequence is the correct one, than the decrypted password would be `[fibo(4), fibo(2), fibo(7), fibo(0)] = [3, 1, 13, 0]`. 

The `get_clue` function gives you a clue that you must use to determine which sequence is correct. `get_clue` returns a tuple where the first element is n (the starting index), and the second element is a list of integers. 

For example the clue might be `2, [1, 2, 3, 5, 8]`. This means the correct sequence is the sequence where starting from n = 2, the values are `[1, 2, 3, 5, 8]`. This means the correct sequence is the fibonacci sequence. 

Another clue might be `(3, [6, 10, 15, 21, 28, 36])`. This means the correct sequence is the sequence where starting from n = 3, the values are `[6, 10, 15, 21, 28, 36]`. This time, this is the triangular sequence, since the triangular sequence is `[1, 3, 6, 10, 15, 21, 28, 36...]`, note that starting from n = 3, the values begin with 6.