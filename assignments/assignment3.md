---
layout: minimal
title: Assignment 2
description: &desc Assignment 2
summary: *desc
# has_children: true
nav_order: 1
has_toc: true
parent: Assignments
grand_parent: Leiden ITP
---

# {{ page.title }}
{: .no_toc .mb-2 }

{{ page.description }}
{: .fs-6 .fw-300 }

1. TOC
{:toc}

# Assignment 2: Collecting moon stones

**Deadline: Tuesday 7 November 2023 23:59**

Hand in your assignment via [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322). See the "Delivery" section for instructions.


## Program

## Template

You can use the template program below as a starting point. This template will provide you with the code necessary to ...



## Grading

Implementing the basic functionality as described above will give you 6 points out of 10.

**Basic functionality**: Your program does everything described above without crashing (for example on bad user inputs). (5.5 points)

**Comments**: Include comments to explain the difficult parts of your code. (0.5 points)

The remaining 4 points can be obtained by implementing additional functionality:

**Pretty printing**: Instead of printing the robot's steps as a list of coordinates, show the steps on the moon surface itself by marking the coordinates and printing the moon surface again. You're free to mark it any way you want, as long as the robot's path is clear. (0.5 points)

**More stones**: Generate the moon with more than two stones and have your robot collect them all. You should still try to minimise the robot's path: finding a shortest path for an arbitrary number of stones is very difficult, so try to at least find a reasonably short path. (2 points)

**User menu**: Once you have implemented the options above, add them to a comprehensive menu in which the user can select the way of printing, the number of stones and any additional options you've added. Be careful of bad user inputs: your program should not crash. (1 point)

**Extra**: This bonus is for those who go the extra mile. Implement a smart algorithm, a polished user interface, or anything that shows outstanding use of programming. (0.5 points)


## Tips


## Delivery

Once you are sure about your program, save a copy of your `.py` file with your **student number** and the **assignment number** as the file name. For example, if your student number is 123456, then save your copy as `123456_3.py`.

If your program consists of multiple files, then compress these into a `.zip` file with the same naming scheme: `123456_3.zip`. Please make sure to **not** include your `venv` folder if you do this. Your submission should not be larger than 50kB.

Next, upload your `.py` or `.zip` file on [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322) under "Assignments" > Assignment 2 - Collecting moon stones.
