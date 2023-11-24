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

This week, the structure of the lab is a bit different. In the last 11 labs, we have covered the basic programming principles and the ways to use them in Python. It is important that you take the time to finish the previous labs and practice with each programming concept. Therefore, this week will contain only one, hopefully fun, challenge exercise. This exercise will focus on the concept of control flow and how to interact with class objects. Also below, you can find an overview where you can practice certain programming concepts.

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
   if character.isaplha():
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

The last thing unrelated to control flow what we need to discuss is everything in Python is an object. This means that a variable or attribute can contain anything or in other words can be anything. For example, in the code below `var` is just a name of a function. In other words, `var` is the variable name for a callable object.

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

## The Bomb Lab

In this exercise, you will help a robot to dismantling a fictional bomb under the LIACS building. The bomb is build by an overly careful programmer that tried to make sure that nobody could temper with his bomb object. This results in some very bad code, but it also makes it near impossible to use or change any attributes of the bomb object. Luckily for us, he also left a way to dismantle the bomb by executing a precise sequence of methods for the robot.

There are multiple bombs with different difficulties to make the challenge more accessible. After importing `bomb`, you can set the difficulty by calling it and use the `level` argument as show below:

```python
bomb(level=1)
```

There are 6 levels each adding additional complexity to the dismantling. We already completed dismantling the zeroth level and started on the first level. In the `bomb_dismanteling.py` file you can see how that works. The levels add the following steps to the bomb dismantling: 
0. Starting the bomb dismantling program already dismantles the bomb. This can be done by typing the correct string in the bomb console, which can be done with `bomb.console(sentence)`. 
1. In this level, the robot also needs to cut different colors of wires. Each wire color can be cut using its own method using the following code: `bomb.cut_COLOR_wire()`, where COLOR can be any color. For example, the red wire can be cut using `bomb.cur_red_wire()`. You can  either use trial and error to find all colored wires or try to find the most common colors for plotting.
2. The second level brings new functionality to the console. When the bomb gives you a sequence of integers, you need to type them one by one into the console using the following code: `bomb.console(number)`.
3. Now, the bomb can also give you a nested list of integers to type into the console. The order of the integers would be the order of printing.
4. For level 4 you need to use two new functionality for the robot. The first one is removing parts of the bomb which can be done with the code: `bomb.remove_part()`. However, before you can remove a part you need to remove the screws which can be done with `screw.remove()`.
5. To be able to complete the last level the robot needs to enter a secret password. This can be done with `bomb.insert_password(password)`. The password can be found be decrypting the encrypted password that the bomb gives you. The password can be decrypted by applying one of four sequence, that we saw in previous labs, to the encrypted password. The four sequences are: fibonacci, padovan, triangular, and factorial. So let say the encrypted password is `[4,2,7,0]` and the fibonacci sequence is the correct one than the decrypted password would be `[fibo(4), fibo(2), fibo(7), fibo(0)] = [3, 1, 13, 0]`. You know what sequence it is because the robot can give you a clue containing what the first index is and the small part of the sequence. For example the clue good be `2, [1, 2, 3, 5, 8]` which points to the fibonacci sequence.

Above, you can find what the robot can do. However, it can also ask the bomb several questions which can either results in an `BombStartsBeeping` error (which can be caught) or:
- `bomb.get_wires()` can result in a sequence of colors that need to be cut in that order.
- `bomb.get_cipher()` can result in a sequence of numbers that need to be typed in the console.
- `bomb.get_part()` can result in part object.
- `get_encrypted_password()` can result in a encrypted password.

In each step of the dismantling process only one of the above function will give you a result and not an `BombStartsBeeping` error. With each bomb level the number of steps increases but it is always random. 

There is also two extra question you can ask the bomb to help the robot which are `bomb.get_screws()` and `bomb.get_clue()`.

To help you structure you approach we have already started dismantling a level one bomb. This can be found in the `bomb_dismanteling.py`. Below, you can also find a part of the code for extra information how it works.

```python
def cut_wires(colors): 
    """
    You can structure you code by handling each possible dismantling task in a separate function.
    Here, we already made a function where you can program the control flow for cutting wires.
    """
    pass

def find_next_step(bomb):
    """
    This function Loops through the possible dismantling steps.
    When a step is done, the function calls itself to perform another step.
    """
    for bomb_func, dismantle_func in BOMB_DISMANTLED_STEP.items():  
        feedback = bomb_func()  # Ask the bomb for info
        print("new code:", feedback)

        dismantle_func(feedback)  # Dismantle a step, depending on what function the bomb did not give a BombStartsBeeping error.

        find_next_step(bomb)

"""
This global dictionary can be used to connect a question that can be asked to the bomb with a function that dismantles that task. 
We already filled it in for a level one bomb, where bomb.get_wires gives us the wires to cut and cut_wires handles the control flow to cut those wires.
"""
BOMB_DISMANTLED_STEP = {bomb.get_wires: cut_wires}

bomb(level=1)
bomb.console("Start dismantle bomb program.")  # Step one in the bomb dismantling process

find_next_step(bomb)  # A recursive function to dismantle all steps
```















