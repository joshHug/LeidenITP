---
layout: minimal
title: Lab 8
description: &desc 3 November, 2023 - classes and objects
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

Welcome to week 8!

## PyCharm recap

This week we continue using PyCharm and running code in the terminal. In [lab 7](https://joshhug.github.io/LeidenITP/labs/lab7/) you can find information about: installing anaconda, opening projects, configuring unittests, reading unittests results, and debugging.

## Overview of This Lab

In addition to the warmup exercise earlier, this week we have ... different exercises that range in difficulty:
 * Exercise 1: [Memory problems and 2D lists](https://joshhug.github.io/LeidenITP/labs/lab8/#exercise-1-memory-problems-and-2d-lists-standard) (standard)
   * Exercise 1a: [Understand the problem](https://joshhug.github.io/LeidenITP/labs/lab8/#exercise-1a-understand-the-problem-standard) (standard)
   * Exercise 1b: [Use numpy](https://joshhug.github.io/LeidenITP/labs/lab8/#exercise-1b-use-numpy-standard) (standard)
   * Exercise 1c: [The ambiguity of multiplying a list](https://joshhug.github.io/LeidenITP/labs/lab8/#exercise-1c-the-ambiguity-of-multiplying-a-list-standard) (standard)
   * Exercise 1d: [How to make a 2D list](https://joshhug.github.io/LeidenITP/labs/lab8/#exercise-1d-how-to-make-a-2d-list-challenge-medium) (challenge, medium)
 * Exercise 2: [Side effects]() (challenge, medium)
 * Exercise 3: [First ten digits]() (challenge, medium)
 * Exercise 4: (standard)
 * Exercise 5: (standard)
 * Exercise 6: 
 * Exercise 7:  (challenge, hard)
 * Exercise 8:  (challenge, very hard)

All students, regardless of experience, should be able to complete the four standard exercises. Whether you complete all four is up to you.

The three exercises marked as "challenge" provide additional practice for interested students. We believe that any student in this class who completes the standard exercises should be able to complete the "medium" difficulty challenge, which extends exercise 2 by making a pretty print.

For more advanced students, you might find the more difficult `Blurring an Images` and `Make an Image Criminal Friendly` exercises to be more interesting. Feel free to skip the standard exercises if you think they are insufficiently challenging.

If you feel that this week's challenges are too hard for you, feel free to do a challenging exercise from last week which should be easier now that you know more.

## Exercise 1: Memory problems and 2D lists (standard)

In this exercise, we will show you why multiplying a list is a bad idea and dangerous. But more important we want to emphasise that coding is thinking about what happens in your memory. While some code looks correct when reading it as a natural language (e.g. English), it does not give the right instructions to your computer. To concluded be always aware of what the code does and specifically think about if you copy the value(s) to new memory or just creates a reference to the same memory.

Tip: If you are unsure about the behavior of your code, and you want to make sure that it is a copy, you can use `import copy` and then `some_variable = copy.deepcopy(...)`

### Exercise 1a: Understand the problem (standard)

Go to the following [page](https://cscircles.cemc.uwaterloo.ca/visualize#code=%22%22%22%0AHint%3A+Multiplying+a+list+does+not+create+a+copy+in+memory,+but+can+ints,+floats,+bool,+strings+etc.+be+changed.%0A++++++What+do+these+data+types+have+in+common%3F+And+what+happens+when+you+try+to+multiply+a+list+with+such+datatypes%3F%0A%22%22%22%0A%0Asingle_value+%3D+%5B0%5D%0Asingle_list+%3D+single_value+*+4%0A%23+The+double+lists+below+are+exactly+the+same,+but+to+show+you+what+happens+we+made+double_list%0A%23+However+often+the+code+you+see+or+try+is+double_list2.%0Adouble_list+%3D+%5Bsingle_list%5D+*+3%0Adouble_list2+%3D+%5B%5B0%5D+*+4%5D+*+3%0A%0Aprint(single_value)%0Aprint(single_list)%0Aprint(double_list)%0Aprint(double_list2)%0A%0A%23+changing+some+values+with+some+unexpected+behavior.%0Asingle_value%5B0%5D+%3D+3%0A%0Asingle_list%5B3%5D+%3D+1%0Adouble_list2%5B0%5D%5B3%5D+%3D+1%0A%0Adouble_list%5B1%5D%5B2%5D+%3D+5%0Adouble_list2%5B1%5D%5B2%5D+%3D+5%0A%0Aprint(single_value)%0Aprint(single_list)%0Aprint(double_list)%0Aprint(double_list2)&mode=display&raw_input=&curInstr=0) and try to understand what goes wrong. 

Hint: Multiplying a list does not create a copy in memory, but can ints, floats, bool, strings etc. be changed. What do these data types have in common? And what happens when you try to multiply a list with such datatypes?

### Exercise 1b: Use numpy (standard)

In exercise 1a, we saw that building a 2D list can create unexpected results. In exercise 1c, you will see why it is even een worse idea to construct a 2D list by multiplying a list. Finally, in exercise 1d, you will try to implement a correct way of constructing a 2D list. While these exercise can help you understand what happens in memory, the second lesson in the whole exercise is do not use list when you use one data type, and you know the length/shape/size it needs to be. In this case, **always** use numpy arrays and never use lists. This solves also the problem of even trying to create 2D lists because, as we saw last week, numpy has the functions: `np.zeros`, `np.ones` and `np.empty`. 

Tip: You can even use your own classes in arrays by using the argument `dtype`. 

Open exercise 2D_data_structures.py and complete the function `exercise_1a_with_2D_arrays`.

### Exercise 1c: The ambiguity of multiplying a list (standard)

In exercise 1a, we learned that multiplying a list is a bad way to create a 2D list. However, even multiplying a single list can be a big problem. Look at the code below and try to answer the following question: Do we know what this code does? or is it ambiguous and only when to code is run (at runtime) we find out what the actual effect is?

```python
new_list = [some_variable] * 4
```

Below you will find a bit more fletched out piece of code. Is it now possible to answer what the code will do? or is it still ambiguous?

```python 
>>> print(some_variable)
-3
>>> new_list = [some_variable] * 4
>>> new_list[0] = abs(new_list[0])
>>> print(new_list) #[3, -3, -3, -3] or [3, 3, 3, 3]?
...
```

The answer to these question is that it is ambiguous, but try to understand why. Also, note that even with more context and print statements, it is still unclear what the code does. This means that the code is unreadable and therefore very bad.

To show an example where the code above does two different things, we made two examples. [link 1](https://cscircles.cemc.uwaterloo.ca/visualize#code=%22%22%22%0AThis+code+will+only+make+the+first+item+a+string.%0A%22%22%22%0A%0Asome_variable+%3D+-3%0A%0Aprint(some_variable)%0Anew_list+%3D+%5Bsome_variable%5D+*+4%0Anew_list%5B0%5D+%3D+abs(new_list%5B0%5D)%0Aprint(new_list)&mode=display&raw_input=&curInstr=0) only makes the first item in the list positive. [link 2](https://cscircles.cemc.uwaterloo.ca/visualize#code=%22%22%22%0AThis+makes+all+items+in+the+list+positive.%0A%22%22%22%0A%0Aclass+width%3A%0A++++def+__init__(self,+w)%3A%0A++++++++%22%22%22+initialize+object%22%22%22%0A++++++++self.w+%3D+w%0A%0A++++def+__abs__(self)%3A%0A++++++++%22%22%22+This+method+is+called+when+abs+is+used+as+in+abs(object).+%22%22%22%0A++++++++self.w+%3D+abs(self.w)%0A++++++++return+self%0A%0A++++def+__repr__(self)%3A%0A++++++++%22%22%22+This+method+is+used+to+print+the+object.+%22%22%22%0A++++++++return+str(self.w)%0A%0Asome_variable+%3D+width(-3)%0A%0Aprint(some_variable)%0Anew_list+%3D+%5Bsome_variable%5D+*+4%0Anew_list%5B0%5D+%3D+abs(new_list%5B0%5D)%0Aprint(new_list)&mode=display&raw_input=&curInstr=0) makes all items in the list positive. You can argue that seeing how `some_variable` is defined can solve the problem. However, when working in large code bases `some_variable` can be defined anywhere, for example, in a different file or somewhere you don't know.

### Exercise 1d: How to make a 2D list (challenge, medium)

As explained in exercise 1b, it is generally not a good idea the use lists if you can use numpy arrays. However, it is a good exercise to think about how you could make the code work in exercise 1a. Therefore, in this exercise you will fix the code in 1a by using lists.

Open exercise `2D_data_structures.py` and complete the function `exercise_1a_with_2D_lists`.

## Exercise 2: Side effects (challenge, medium)

This exercise continues with exploring how side effects work and how to create or avoid them. This is also a good exercise for a simple example of creating your own functions. In the exercise, we will repeat [exercise 3: enumerate](https://joshhug.github.io/LeidenITP/labs/lab6/#exercise-3-enumerate-standard) `multiply_index_value` from lab 6. However, it is extended a bit by not only asking the complete `multiply_index_value` but also use it to calculate the difference between the original list and the outcome of `multiply_index_value`.

In this exercise you will no longer only complete one function, but you need to complete the `main` function that can use any number of functions. This is synonymous with writing small scripts. Open exercise `side_effects.py` and follow the instructions.

## Exercise 3: First ten digits (challenge, medium)
In this exersice, we will work out the first ten digits of the sum of ninety-nine 50-digit numbers in the file `first_ten_digits.txt`. We will use two strategies to do this. First, we will open the file as a textfile and transform the strings into numbers. Second, we use numpy to read the file and continue with a numpy array.

It is important to also close a file when you are opening it using code. This can be seen similarly as just opening a file in a program and not closing it. What happens if you open a file 50 times and you adjust one or if you want to delete the file but some program is using it (having it open). Therefore it is important to make sure that after your script has run all files are closed. Even if your program terminates unexpected due to for example a bug.

To make sure a file is closed python has a specific syntax which is as follows:
```python
with open(file_name, file_mode) as f:
   # This would print the whole file.
   print(f.read())  
   
   # This loops through all the lines in the file. 
   # Equivalent to: for line in f.readlines().
   for line in f:
      pass
```
As soon as you do not need the file anymore you can continue outside the `with` statement. This then closes the file.

When you use `np.genfromtxt` the file is automatically closed after this line of code.

Open exercise `first_ten_digits.py` and follow the instructions.

## exercise 4;



![images](/LeidenITP/assets/images/lab7/rotate_colors.png)
