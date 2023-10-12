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

Start by downloading the .zip file for this week's code. Unzip the file.

Now open PyCharm and select ...

(add screenshots and further directions)

### Running a Test

Try opening `lab6_intro.py`. Click the "run" button in PyCharm and you should see two red x's appear. This is because the code we currently have provided in `lab6_intro.py` is not correct.

Modify the `squared_plus_one` function so that it is correct and try running the tests again. This time you should get a green arrow.

Lastly, modify the `remove_last_item` function so that it is correct, and try running the tests again. This time all tests have passed. You're ready to move on to this week's exercises.

### 2D_to_1D

To get more practice with basic Python, we're going to write some code that works on lists that contains lists. For example, consider the list `x = ["cat", 5, ["dog", "cow", "kaas"]]]`. This list has 3 items. `x[0]` is the string "cat". `x[1]` is the number 5. `x[2]` is also a list, and it also has 3 of its own items.