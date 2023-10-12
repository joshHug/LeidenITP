---
layout: minimal
title: Lab 6
description: &desc 12 October, 2023 - Loops and Dictionaries
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

### Installing Anaconda

To be better prepared for future exercise we need more than the standard python library that was included with the PyCharm installation. While it is possible to install extra library one at the time, it is easier to install the most common libraries all at once with a new python environment. We will do this by installing [anaconda](https://www.anaconda.com/download). Go to the page, scrolldown, choose your operating system and download anaconda. After downloading, run the installer and follow the instructions.

### Open Project

Start by downloading the .zip file for this week's code. Unzip the file.

Now open PyCharm and select open and select the folder you just created (when unzipping). To work with the new conda environment, that we just installed, go to the lower corner of your screen where it says */home/user/current_python_installation*. Click on it and select **Add New Interpreter** -> **Add Local Interpreter**. This should look like the image below.

![images](/LeidenITP/assets/images/Add_interpreter.png)

Next, you will see a screen similar to the screenshot down below. At the left side of the popup screen click on **conda environment**. Then it should already be on **use existing environment** but if not click that radiobutton. Now, click on **ok** and from now you should program in this environment.

![images](/LeidenITP/assets/images/Interpreter.png)

### Running a Test

Try opening `lab6_intro.py`. Click the "run" button in PyCharm and you should see two red x's appear. This is because the code we currently have provided in `lab6_intro.py` is not correct.

Modify the `squared_plus_one` function so that it is correct and try running the tests again. This time you should get a green arrow.

Lastly, modify the `remove_last_item` function so that it is correct, and try running the tests again. This time all tests have passed. You're ready to move on to this week's exercises.

This week we have 5 different exercises that range in difficulty. All students, regardless of experience, should be able to complete the standard exercises.

The challenge exercises provide additional challenge for interested students. Any student in the class should be able to complete the "normal" difficulty challenge in this lab, which builds on the Scrabble exercise from week 3.

For more advanced students, you might find the `fibonacci` and `hard` exercises to be more interesting. Feel free to skip the standard exercises if you think they are insufficiently challenging. 

## Conversion2D_1D (standard)

To get more practice with basic Python, we're going to write some code that works on lists that contains lists. For example, consider the list `x = ["cat", 5, ["dog", "cow", "kaas", "koe"]]]`. This list has 3 items. `x[0]` is the string "cat". `x[1]` is the number 5. `x[2]` is also a list, in this case of length 4.

Open "Conversion2D_1D.py" and work your way through the exercises.

## Enumerate (standard)

The `enumerate` keyword in Python allows us to (brief explanation). 

Open `enumerate.py`. 

## Scrabble (challenge, normal)

The last set of exercises that we'd like everyone to complete is `scrabble.py`. 

## fibonacci (challenge, hard)

Fibonacci.py contains some additional exercises that [describe them]. 

## add (challenge, very hard)

This week we've included one especially challening exercise.




