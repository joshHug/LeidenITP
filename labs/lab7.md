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
 * Exercise 1: [Shopping List](https://joshhug.github.io/LeidenITP/labs/lab7/#exercise-1-shopping-list-standard) (standard)
   *  [Ternary Operator](https://joshhug.github.io/LeidenITP/labs/lab7/#ternary-operator-challenge-medium) (challenge, normal)
 * Exercise 2: [Improving Shopping List](https://joshhug.github.io/LeidenITP/labs/lab7/#exercise-2-improving-shopping-list-standard) (standard)
 * Exercise 3: [Basic Numpy](https://joshhug.github.io/LeidenITP/labs/lab7/#exercise-3-basic-numpy-standard) (standard)
 * Exercise 4: [Arithmetic With Numpy](https://joshhug.github.io/LeidenITP/labs/lab7/#exercise-4-arithmetic-with-numpy-standard) (standard)
 * Exercise 5: (standard)
 * Exercise 6: [Rotate Colors (challenge, hard)](https://joshhug.github.io/LeidenITP/labs/lab7/#exercise-6-rotate-colors-challenge-hard)
 * Exercise 7: [Blurring an Images](https://joshhug.github.io/LeidenITP/labs/lab7/#exercise-7-blurring-an-images-challenge-very-hard) (challenge, hard)
 * Exercise 8: [Make an Image Criminal Friendly](https://joshhug.github.io/LeidenITP/labs/lab7/#exercise-8-make-an-image-criminal-friendly-challenge-very-hard) (challenge, very hard)

All students, regardless of experience, should be able to complete the four standard exercises. Whether you complete all four is up to you.

The three exercises marked as "challenge" provide additional practice for interested students. We believe that any student in this class who completes the standard exercises should be able to complete the "medium" difficulty challenge, which extends exercise 2 by making a pretty print.

For more advanced students, you might find the more difficult `Blurring an Images` and `Make an Image Criminal Friendly` exercises to be more interesting. Feel free to skip the standard exercises if you think they are insufficiently challenging.

If you feel that this week's challenges are too hard for you feel free to do a challenging exercise from last week which should be a little easier now you know more.

## Exercise 1: Shopping List (standard)

**For this exercise, we're going to do all of our work in the python visualizer. There's no local copy of the code.**

Before you start this exercise, make sure you understand [exercise 4 of lab 6 (helper_functions_side_effects)](https://joshhug.github.io/LeidenITP/labs/lab6/#exercise-4-helper_functions_side_effects-standard). 

In this exercise, we'll give you buggy code that you'll need to fix. Specifically, it gets stuck in an infinite loop. 

Let's try running it. Go to [the visualizer](https://cscircles.cemc.uwaterloo.ca/visualize#code=def+remove_all(lst,+x)%3A%0A++++%22%22%22%0A++++This+function+should+remove+all+the+items+from+the+lst+with+the+value+x.%0A++++%22%22%22%0A++++new_lst+%3D+%5B%5D%0A++++for+item+in+lst%3A%0A++++++++if+item+%3D%3D+x%3A%0A++++++++++++continue%0A++++++++new_lst.append(item)%0A%0A++++%23+TODO%3A+add+code+below+to+make+the+program+work%0A%0A%0A%23+The+code+below+should+create+a+shopping_dict+counting+the+number+of+times%0A%23+each+grocery+appears.+For+the+example+below,+we+should+get%3A%0A%23+++%7B%22banana%22%3A+4,+%22apple%22%3A+2,+%22cheese%22%3A+1,+%22bread%22%3A+2%7D%0A%23%0A%23+However,+the+code+we've+provided+fails.+Follow+the+direction+in+the+lab%0A%23+text+to+fix.%0Ashopping_lst+%3D+%5B%22banana%22,+%22apple%22,+%22cheese%22,+%22banana%22,+%22banana%22,+%22bread%22,+%22banana%22,+%22apple%22,+%22bread%22%5D%0A%0A%23+Make+a+dict+with+the+grocery+and+number+in+the+shopping_lst%0Ashopping_dict+%3D+%7B%7D%0Awhile+shopping_lst%3A%0A++++%23+get+the+front+item+in+the+shopping_lst%0A++++grocery+%3D+shopping_lst%5B0%5D%0A++++print(f%22grocery+%7Bgrocery%7D+is+added+to+the+shopping+list.%22)%0A++++%23+add+the+count+of+the+current+grocery+item%0A++++shopping_dict%5Bgrocery%5D+%3D+shopping_lst.count(grocery)%0A%0A++++%23+remove+all+copies+of+the+given+grocery,+e.g.+if+%22banana%22+is+the%0A++++%23+current+grocery,+the+shopping_lst+should+have+no+more+bananas+after+this+line%0A++++remove_all(shopping_lst,+grocery)%0A%0A%23+nice+print+to+make+the+shopping+list.%0Afor+grocery,+number+in+shopping_dict.items()%3A%0A++++print(f%22Buy+%7Bnumber%7D+%7Bgrocery%7D(s).%22)&mode=display&raw_input=&curInstr=0) and get a feeling for what's going in.

It's clear there's an infinite loop. Just like in your own programs that you'll write later, it's not always clear where the problem lies. 

Consider: Is the problem in the removeAll function? Or is it in the script that calls the removeAll function? Or is it in the interaction between the two pieces of code? 

### Exercise 1A

In exercise 1A, we'll fix the problem by ONLY changing the removeAll function so that it has a side effect. Go back to [the visualizer](https://cscircles.cemc.uwaterloo.ca/visualize#code=def+remove_all(lst,+x)%3A%0A++++%22%22%22%0A++++This+function+should+remove+all+the+items+from+the+lst+with+the+value+x.%0A++++%22%22%22%0A++++new_lst+%3D+%5B%5D%0A++++for+item+in+lst%3A%0A++++++++if+item+%3D%3D+x%3A%0A++++++++++++continue%0A++++++++new_lst.append(item)%0A%0A++++%23+TODO%3A+add+code+below+to+make+the+program+work%0A%0A%0A%23+The+code+below+should+create+a+shopping_dict+counting+the+number+of+times%0A%23+each+grocery+appears.+For+the+example+below,+we+should+get%3A%0A%23+++%7B%22banana%22%3A+4,+%22apple%22%3A+2,+%22cheese%22%3A+1,+%22bread%22%3A+2%7D%0A%23%0A%23+However,+the+code+we've+provided+fails.+Follow+the+direction+in+the+lab%0A%23+text+to+fix.%0Ashopping_lst+%3D+%5B%22banana%22,+%22apple%22,+%22cheese%22,+%22banana%22,+%22banana%22,+%22bread%22,+%22banana%22,+%22apple%22,+%22bread%22%5D%0A%0A%23+Make+a+dict+with+the+grocery+and+number+in+the+shopping_lst%0Ashopping_dict+%3D+%7B%7D%0Awhile+shopping_lst%3A%0A++++%23+get+the+front+item+in+the+shopping_lst%0A++++grocery+%3D+shopping_lst%5B0%5D%0A++++print(f%22grocery+%7Bgrocery%7D+is+added+to+the+shopping+list.%22)%0A++++%23+add+the+count+of+the+current+grocery+item%0A++++shopping_dict%5Bgrocery%5D+%3D+shopping_lst.count(grocery)%0A%0A++++%23+remove+all+copies+of+the+given+grocery,+e.g.+if+%22banana%22+is+the%0A++++%23+current+grocery,+the+shopping_lst+should+have+no+more+bananas+after+this+line%0A++++remove_all(shopping_lst,+grocery)%0A%0A%23+nice+print+to+make+the+shopping+list.%0Afor+grocery,+number+in+shopping_dict.items()%3A%0A++++print(f%22Buy+%7Bnumber%7D+%7Bgrocery%7D(s).%22)&mode=edit&raw_input=) and fill in the TODO.

Your new code should modify `removeAll` so that it has the intended side effect.

Once your code is working correctly, the output should look like:
```
Buy 3 banana(s).
Buy 2 apple(s).
Buy 1 cheese(s).
Buy 2 bread(s).
```

### Exercise 1B

Let's start over again and consider an alternate solution.

Open [the visualizer](https://cscircles.cemc.uwaterloo.ca/visualize#code=def+remove_all(lst,+x)%3A%0A++++%22%22%22%0A++++This+function+should+return+a+new+copy+of+the+lst+with+all+instances+of+x+removed.%0A++++%22%22%22%0A++++new_lst+%3D+%5B%5D%0A++++for+item+in+lst%3A%0A++++++++if+item+%3D%3D+x%3A%0A++++++++++++continue%0A++++++++new_lst.append(item)%0A%0A++++%23+TODO%3A+add+code+below+to+make+the+program+work%0A%0A%0A%23+The+code+below+should+create+a+shopping_dict+counting+the+number+of+times%0A%23+each+grocery+appears.+For+the+example+below,+we+should+get%3A%0A%23+++%7B%22banana%22%3A+4,+%22apple%22%3A+2,+%22cheese%22%3A+1,+%22bread%22%3A+2%7D%0A%23%0A%23+However,+the+code+we've+provided+fails.+Follow+the+direction+in+the+lab%0A%23+text+to+fix.%0Ashopping_lst+%3D+%5B%22banana%22,+%22apple%22,+%22cheese%22,+%22banana%22,+%22banana%22,+%22bread%22,+%22banana%22,+%22apple%22,+%22bread%22%5D%0A%0A%23+Make+a+dict+with+the+grocery+and+number+in+the+shopping_lst%0Ashopping_dict+%3D+%7B%7D%0Awhile+shopping_lst%3A%0A++++%23+get+the+front+item+in+the+shopping_lst%0A++++grocery+%3D+shopping_lst%5B0%5D%0A++++print(f%22grocery+%7Bgrocery%7D+is+added+to+the+shopping+list.%22)%0A++++%23+add+the+count+of+the+current+grocery+item%0A++++shopping_dict%5Bgrocery%5D+%3D+shopping_lst.count(grocery)%0A%0A++++%23+remove+all+copies+of+the+given+grocery,+e.g.+if+%22banana%22+is+the%0A++++%23+current+grocery,+the+shopping_lst+should+have+no+more+bananas+after+this+line%0A++++%23+TODO%3A+modify+the+line+below+so+that+the+code+works%0A++++remove_all(shopping_lst,+grocery)%0A%0A%23+nice+print+to+make+the+shopping+list.%0Afor+grocery,+number+in+shopping_dict.items()%3A%0A++++print(f%22Buy+%7Bnumber%7D+%7Bgrocery%7D(s).%22)&mode=edit&raw_input=). 

This time, you'll have two different TODOs to fill in. 

For the first TODO, modify the function so that it has no side effects, and instead returns a copy of the lst with all instances of x removed. Then modify the second TODO so that the code works overall. We won't tell exactly how to do this.

Once your code is working correctly, the output should again look like:
```
Buy 3 banana(s).
Buy 2 apple(s).
Buy 1 cheese(s).
Buy 2 bread(s).
```

Now that you've solved the problem in two ways, let's think very carefully about how the two approaches compare. Below, we visualize the return step of the function for both approaches. Note the differences.

First approach (with side effects):
![images](/LeidenITP/assets/images/lab7/lab7_side_effect_return.png)

Second approach (no side effects):
![images](/LeidenITP/assets/images/lab7/lab7_no_side_effect_return.png)

Also consider: Which solution has safer code?

## Exercise 2: Improving Shopping List (standard)

In exercise 1A, we fixed the `removeAll` method so that it had the intended side effects. One quirky thing about our code is that we had to make an entirely new list and then copy everything back. 

You might ask, how could I modify the code so that we can iterate over a list and delete items at the same time?

The naive way to do this is given in this [code](https://cscircles.cemc.uwaterloo.ca/visualize#code=def+remove_all(lst,+x)%3A%0A++++%22%22%22%0A++++This+function+removes+all+the+items+from+the+lst+with+the+value+x.%0A%0A++++For+example%3A+%5B1,+2,+3,+2%5D,+2+-%3E+%5B1,+3%5D%0A++++%22%22%22%0A++++for+i,+item+in+enumerate(lst)%3A%0A+++++++if+item+%3D%3D+x%3A%0A++++++++++del+lst%5Bi%5D+++++%0A%0Ashopping_lst+%3D+%5B%22banana%22,+%22apple%22,+%22cheese%22,+%22banana%22,+%22banana%22,+%22bread%22,+%22banana%22,+%22apple%22,+%22bread%22%5D%0A%23+remove+one+product+from+the+shopping+list%0Aremove_all(shopping_lst,+%22banana%22)%0Aprint(shopping_lst)&mode=display&raw_input=&curInstr=0), which unfortunately doesn't work. Try to analyse what is wrong. Why does it not remove all bananas? 

This code is not safe at all, which has to do with the fact that we are looping through the same object while altering that object. This is common problem when removing items form, for example, a list. 

Generally, there are two approaches to solve this issue. First, find the items (indices) that you want to remove. Then after the for loop remove them (think about the order). Second, put the whole for loop in a while loop that terminates when nothing get delete and start the loop again each time you remove an item. This is quite slow, as you go through the same item each time you start over. Note, that there are other solutions and these approaches should be adjusted for your purpose. 

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

In exercise 1A, the code for the function `remove_all` was not according to either one of these approaches. 

For this exercise rewrite the code for `remove_all`. You'll be doing this in pycharm.

Quick pedagogical note: The code we provided for exercises 1 and 2 is artificial and not a great solution for the problem. Using `while shopping_lst:` is tricky to get right, as you've seen throughout this exercise. A better approach avoids remove operations entirely. Optionally, try to recreate this entire script without having to remove anything from a list at all.

### Ternary Operator (challenge, medium)

Lastly, we can a bit of cleanup in the print statement. Now, it adds always a '*s*' to the name of a grocery even if it is singular. To make it only put an '*s*' behind plural words we can use a ternary statement. Apply, a ternary statement to the print statement to fix the singular plural problem. Below is some explanation about ternary operators.

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

In this exercise, you will learn how to do basic functionality of numpy (numerical python). There are a lot of functions in the numpy library, here we will focus on the absolute basics. Each function in this exercise will have a numpy function that does the work for you or there is a specific bracket notation `[]` that you can use. 

Often the joke is made that coding is just good googling. This is rather true in the sentence that often programmers do not know all code by hard but they know when they see a solution for their problem. To get more familiar with searching online for solution. We want you to find the solution online for this exercise. Keep in mind that the answer should be short.

Also, if you are more experienced with coding, python and more specific numpy. This exercise can be a bit bland, so feel free to skip it. This also is the case for exercise 4.

Open basic_numpy.py and work your way through the exercises.

This exercise focuses on creating numpy arrays, indexing them, and slicing.

## Exercise 4: Arithmetic With Numpy (standard)

Arithmetic with numpy arrays works differently from native python list. The main reason for this difference is that the library is made to be very similar to linear algebra. These days almost all linear algebra expressions can be directly be used in python (with numpy). The main difference is that operators work on the values in the array and not on the array. For example, when adding list the list becomes bigger: `[1, 2] + [3, 4] = [1, 2, 3, 4]`, while when adding two arrays the size of the array stays the same and the values in the array are added: `np.array([1, 2]) + np.array([3, 4]) = np.array([4, 6])`.

There is a specific operator, for each function that you need to implement in this exercise. As seen in the example above `array1 + array2` will add the elements of each array together. Therefore, there is no need for a for loop. This is the same for the function in this exercise. Do not use a for loop but use operators and if needed `np.sqrt` or `np.sum`. Feel free to google what the intended operator should be.

Open arithmetic_numpy.py and work your way through the exercises.

This exercise focuses on arithmetic with numpy arrays.

## Exercise 5: (standard)

...

## Exercise 6: Rotate Colors (challenge, hard)

This exercise learns you how to rotate the colors of an images. This is ofter one of the basic tools in photoshop but not hard to implement yourself. 

A color is an array of three values. In this exercise, we will rotate or shift each value to the left. This means that the first value becomes the third, the second the first, and the third becomes the second value. For a simplified version of the problem you can have a look at [practise exercise](https://codingbat.com/prob/p148661) of CodingBat.

Open rotate_colors.py and work your way through the exercises.

In this exercise, we continue with using numpy and slicing arrays. 
Also, we come back to reference to an object or making a copy of an object.

The end results should look like this:

![images](/LeidenITP/assets/images/lab7/rotate_colors.png)

## Exercise 7: Blurring an Images (challenge, very hard)

In this exercise, we continue with using numpy. However, this exercise is no longer a simple toy problem, but also has some real world applications. When, you complete both function you will also see the end result of the original and blurred image. Blurring an image has the effect of taking an unsharp photograph. This is done by averaging each pixel by its neighbouring pixels.

The function `len` is a bit ambiguous when it comes down to numpy arrays as they can be multidimensional. To get more readable code, we use `size` to get the overall size of the numpy array (as if it was a one dimensional list) and `shape` if we want the length of each axis in the array. Note, that shape return a tuple for each axis the length. For more information see the numpy documentation.

Open blur_image.py and work your way through the exercises.

This exercise focuses mainly on loops and slicing of numpy arrays.

The end results should look like this:

![images](/LeidenITP/assets/images/lab7/blur_image.png)

## Exercise 8: Make an Image Criminal Friendly (challenge, very hard)

In this exercise, we continue with using numpy and slicing arrays. However, this exercise is no longer a simple toy problem, but also has some real world applications. When, you complete both function you will also see the end result of the original image of a pumpkin and a blurred out pumpkin.

Blurring out the pumpkin or pixelating it is similar to what you see when a face is made unrecognizable on tv. This is done by creating the effect of locally reducing the pixel density. In this exercise, we will do this by making patches of 30x30 pixels and giving all the pixels the same color value.

Open pixelate_image.py and work your way through the exercises.

This exercise focuses mainly on loops, slicing of numpy arrays and finding a point in an image.

The end results should look somthing like this:

![images](/LeidenITP/assets/images/lab7/pixelate_image.png)
