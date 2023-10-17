---
layout: minimal
title: Lab 7
description: &desc 20 October, 2023 - Arrays & Side effects
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

Welcome to week 7!

## PyCharm

Starting from last week, we're saying goodbye to CodingBat. From now on, we'll be using PyCharm to write and test all of our code. We provided the same manual from last week, just to have easy access to all the information. However, ofcourse do not install anaconda again. Also, if you have already done the other steps you can skip to the exercises.

In this lab, we'll be using and combining all of the techniques and syntax we've seen from labs 1 through 6.

### Installing Anaconda (redundent)

To be better prepared for future exercises, we need more than the standard python library that was included with the PyCharm installation. While it is possible to install extra libraries one at the time, it is easier to install the most common libraries all at once into what is called a "python environment". We will do this by installing  a tool called [Anaconda](https://www.anaconda.com/download). Go to the page, scroll down, choose your operating system and download Anaconda. After downloading, run the installer and follow the instructions.

### Open Project

Start by downloading the .zip file for this week's code [at this link](https://brightspace.universiteitleiden.nl/d2l/le/lessons/240322/topics/2661436). Unzip the file.

Now open PyCharm and select open and select the folder you just created (when unzipping). To work with the new conda environment, that we just installed, go to the lower corner of your screen where it says */home/user/current_python_installation*. Click on it and select **Add New Interpreter** -> **Add Local Interpreter**. This should look like the image below.

![images](/LeidenITP/assets/images/Add_interpreter.png)

Next, you will see a screen similar to the screenshot down below. At the left side of the popup screen click on **conda environment**. Then it should already be on **use existing environment** but if not click that radiobutton. Now, click on **ok** and from now you should program in this environment.

![images](/LeidenITP/assets/images/Interpreter.png)

### Configure Unittests

Instead of running the python files in the interpreter, you can also run the unittests in a test environment. The additional benefit of doing this is that you get a file tree on the left hand side with green checkmarks or red/yellow cross for each test. When you click on a tests suite you see all the results for these tests and when clicking on a single test you see only the result of that test. To do this a more elaborate editor is needed such as PyCharm or vscode. In this next section you find how to configure it for PyCharm.

To configure the test environment in PyCharm you go to the dropdown menu next to the run and debug icons in the top right corner. Here, you click **edit configurations...**, this should like the image below.

![images](/LeidenITP/assets/images/unittest_configure_menu.png)

Next, you click on the **plus icon** in the right upper corner. Go to the **python tests** and click on **unittests**. See below, for an example how it would look like. 

![images](/LeidenITP/assets/images/configure_unittests.png)

Next, you can configure what file needs to be tested when the **run icon** is clicked. However, it is easier to just let everything stand on the default and click **ok**. Now, go back to the dropdown menu, where you click **edit configurations...**, but now click **current file**. This way if you go to another file it runs that file, and you do not reconfigure anything.

### Read Unittests Results

Unittests are something new, that you did not see before. However, they are merely a tool for you to check if you work is correct. In large production environment they also function as a safety net to not release wrong code. For now, you do not need to worry about that. 

It is important to realize that unittest can not actually test if your code is correct. They just check if for a few example your code gives the correct output. Therefore, you can never rely solely on unittest to check your work. Therefore, normal debug methods are still important.

When an unittest succeeds, it does not print that much (or nothing) in the interpreter screen. However, when something does go wrong it prints out a lot. Important to note, that it will never tell you which line of code is wrong because it can only tell you if your output is wrong, unless there is an error. The screenshot below can help you understand what goes wrong. In the red box, you can find which unittest goes wrong (which is in our case always the name of the function that is wrong). In the green box, you can find which test case goes wrong. For this course we choose to give you several unittest per function. So, if there is an edge case that is wrong the other test are still right. In the yellow box, you can see of which test suite this unittest belongs. When running the test in PyCharm this will be a folder on the lower left hand side. Lastly, the green box tells you how your input is different from the expected input.

![images](/LeidenITP/assets/images/unittest_debug.png)

### Debug Tips

Even though the unittest can help you with understanding what goes wrong in your code. They are not the only tool you have to check your work. One of the easiest way to check if one line of code works the way you think it works is to run python in an interpreter and run the line of code. Running python in the interpreter can be done by just typing `python` in the interpreter/terminal. See below for an example to see what `range` returns.

![images](/LeidenITP/assets/images/use_terminal.png)

Another option is to suppress the unittests and use print statements. This can be done by changing the `VERBOSE` at the beginning of the file to 0. Now, only the number of correct and incorrect test cases are shown and your print statements are easier to find/read. Important to note, that this will only work when running the file as a normal `.py` file and not as a unittest file as we previously configured. There are two ways to run it as a normal `.py` file. One run it in the terminal by typing `python fileName.py`. The other option is to redo the steps to run it as an unittest file and instead of unittest click **python** and by script choose the script you want to run.

Lastly, you can copy the code you want to test to an empty file, at some print statements and run that file.

## Overview of This Lab

In addition to the warmup exercise earlier, this week we have 6 different exercises that range in difficulty:
 * Exercise 1: 
 * Exercise 2: 
 * Exercise 3:
 * Exercise 4: 
 * Exercise 5: 
 * Exercise 6: 
 * Exercise 7: 

All students, regardless of experience, should be able to complete the three standard exercises. Whether you complete all three is up to you.

The three exercises marked as "challenge" provide additional practice for interested students. We believe that any student in this class who completes the standard exercises should be able to complete the "medium" difficulty challenge, which builds on scrabble from an earlier lab.

For more advanced students, you might find the more difficult `fibonacci` and `add` exercises to be more interesting. Feel free to skip the standard exercises if you think they are insufficiently challenging. 

## Exercise 1: Shopping List (standard)

Before you start this exercise, make sure you understand [exercise 4 of lab 6 (helper_functions_side_effects)](https://joshhug.github.io/LeidenITP/labs/lab6/#exercise-4-helper_functions_side_effects-standard). 

In this and the next exercise, you are improving given code in two ways. We will fix the code ex.1, such that it runt correctly, and we will make the code safer and better readable ex2.. 

Important note, if a program is in an infinite loop (a loop that will never stop) you can stop the program with `CRTL-C` in the terminal or click the red square in the upper left corner of the run screen.

Take a look at the following code on [this website](https://cscircles.cemc.uwaterloo.ca/visualize#code=def+remove_all(lst,+x)%3A%0A++++%22%22%22%0A++++This+function+removes+all+the+items+from+the+lst+with+the+value+x.%0A%0A++++For+example%3A+%5B1,+2,+3,+2%5D,+2+-%3E+%5B1,+3%5D%0A++++%22%22%22%0A++++new_lst+%3D+%5B%5D%0A++++for+item+in+lst%3A%0A++++++++if+item+%3D%3D+x%3A%0A++++++++++++continue%0A++++++++new_lst.append(item)%0A++++%23+TODO+add+code+below+to+make+the+program+work%0A%0A%23+A+shopping+list+if+an+item+is+in+the+list+multiple+times+get+that+many.%0A%23+For+example%3A+%5B%22x%22,+%22x%22+,+%22y%22%5D+is+buy+2x+and+1y.%0Ashopping_lst+%3D+%5B%22banana%22,+%22apple%22,+%22cheese%22,+%22banana%22,+%22banana%22,+%22bread%22,+%22banana%22,+%22apple%22,+%22bread%22%5D%0A%0A%23+Make+a+dict+with+the+grocery+and+number+in+the+shopping_lst%0Ashopping_dict+%3D+%7B%7D%0Awhile+shopping_lst%3A%0A++++grocery+%3D+shopping_lst%5B0%5D%0A++++print(f%22grocery+%7Bgrocery%7D+is+added+to+the+shopping+list.%22)%0A++++shopping_dict%5Bgrocery%5D+%3D+shopping_lst.count(grocery)%0A%0A++++%23+remove+items+that+we+have+already+seen+for+efficiency.%0A++++remove_all(shopping_lst,+grocery)&mode=display&raw_input=&curInstr=71) and try to understand what goes wrong. 

In the question below you will fix the code. During, the question think about the difference in memory usage and code safety. The output for both questions should look like this:
```
Buy 3 banana(s).
Buy 2 apple(s).
Buy 1 cheese(s).
Buy 2 bread(s).
```

Open shopping_list.py and work your way through the exercises.

Question 1: Try to fix the code by creating a side effect in the function `remove_all`. In the code, there is ONE TODO comment specifying where you need to add code for question 1.

Question 2: Try to fix the code by not using side effects in the function `remove_all`. In the code, there are TWO TODO comment specifying where you need to add code for question 2.

## Exercise 2: Improving Shopping List (standard)

Look at this [code](https://cscircles.cemc.uwaterloo.ca/visualize#code=def+remove_all(lst,+x)%3A%0A++++%22%22%22%0A++++This+function+removes+all+the+items+from+the+lst+with+the+value+x.%0A%0A++++For+example%3A+%5B1,+2,+3,+2%5D,+2+-%3E+%5B1,+3%5D%0A++++%22%22%22%0A++++for+i,+item+in+enumerate(lst)%3A%0A+++++++if+item+%3D%3D+x%3A%0A++++++++++del+lst%5Bi%5D+++++%0A%0Ashopping_lst+%3D+%5B%22banana%22,+%22apple%22,+%22cheese%22,+%22banana%22,+%22banana%22,+%22bread%22,+%22banana%22,+%22apple%22,+%22bread%22%5D%0A%23+remove+one+product+from+the+shopping+list%0Aremove_all(shopping_lst,+%22banana%22)%0Aprint(shopping_lst)&mode=display&raw_input=&curInstr=0) and try to analyse what is wrong. Why does it not remove all banana's? 

This code is not safe at all, which has to do with the fact that we are looping through the same object while altering that object. This is common problem when removing items form, for example, a list. Generally, there are two approaches to solve this issue. First, find the items (indices) that you want to remove. Then after the for loop remove them (think about the order). Second, put the whole for loop in a while loop that terminates when nothing get delete and start the loop again each time you remove an item. This is quite slow, as you go through the same item each time you start over. Note, that there are other solutions and these approaches should be adjusted for your purpose. 

First approach:
```python
del_lst = []
for i, item in enumerate(lst):
    if ...:
        del_lst.append(i)

for i in reversed(del_lst): # think about why it would not work without reversed
    ...
```

Second approach:
```python
flag = True
while flag:
    flag = False
    
    for item in lst:
        if ...:
            lst.remove(item)
            flag = True # if nothing is remove during the for loop the while loop ends. This is safe because the default is the while loop ends.
            break
```

In the previous exercise, the code for the function `remove_all` was not according two either one of these approaches. For this exercise rewrite the code for `remove_all_count`. However, the biggest and most dangerous part of the previous code was the line `while shopping_lst:`. This code is likely to create an infinite loop because unless we code everything correct the default is an infinite loop. Therefore, in this exercise we will also change that code to a more safe version which is also better readable. To do this, we will break the while loop (`while shopping_lst:`) into two parts. One loop will find all the unique items and another loop loops over these unique items and count and removes them from the original list.

Open improve_shopping_list.py and work your way through the exercises.

As an extra practise exercise, you can also try to remove the side effect from `remove_all_count` and let it return the updated list. 

### Ternary Operator (challenge, hard)

Lastly, we can a bit of cleanup in the print statement. Now, it adds always a *s* to the name of a grocery even if it is singular. To make it only put an *s* behind plural words we can use a ternary statement. Apply, a ternary statement to the print statement to fix the singular plural problem. Below is some explanation about ternary operators.

The idea of a ternary operator is that you can have two outcomes depending on a rule. While python does not officially have a ternary operator (like C#, C++, java, etc.), there is a common way of writing them. You should use a ternary operator when the value of a variable should be A in the case of ... otherwise B. It replace the following code:
```python
if SomeCondition:
    value = 10 #this can be any value
else:
    value = 20
```

The problem with the code above is that an `if` `else` statement can do anything, while the a ternary statement signals to the reader that a value is assigned according to some condition. The code above as a ternary statement in python looks as follows:
```python
value = 10 if SomeCondintion else 20
```

## Exercise 3: Basic Numpy (standard)

In this exercise, you will learn how to do basic functionality of numpy (numerical python). There are a lot of functions in the numpy library, here we will focus on the absolute basics.

Open basic_numpy.py and work your way through the exercises.

This exercise focuses on creating numpy arrays, indexing them, and slicing.

## Exercise 4: Arithmetic With Numpy (standard)

Arithmetic with numpy arrays works differently from native python list. The main reason for this difference is that the library is made to be very similar to linear algebra with. These days almost all linear algebra expressions can be directly be used in python (with numpy). The main difference is that operators work on the values in the array and not on the array. For example, when adding list the list becomes bigger: `[1, 2] + [3, 4] = [1, 2, 3, 4]`, while when adding two arrays the size of the array stays the same and the values in the array are added: `np.array([1, 2]) + np.array([3, 4]) = np.array([4, 6])`.

Open arithmetic_numpy.py and work your way through the exercises.

This exercise focuses on arithmetic with numpy arrays.

## Exercise 5: Blurring an Images (challenge, hard)


## Exercise 6: Make an Image Criminal Friendly (challenge, very hard)