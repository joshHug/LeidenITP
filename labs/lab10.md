---
layout: minimal
title: Lab 10
description: &desc 17 November, 2023 - Recursion & Hashable Objects
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

Welcome to week 11, lab 10!

## PyCharm recap

This week we continue using PyCharm and running code in the terminal. In [lab 7](https://joshhug.github.io/LeidenITP/labs/lab7/) you can find information about: installing anaconda, opening projects, configuring unittests, reading unittests results, and debugging.

## Overview of This Lab

This week we have ... different exercises that range in difficulty:
 * Exercise 1: []() (standard)

   
All students, regardless of experience, should be able to complete the ... standard exercises. Whether you complete all ... is up to you.

The ... exercises marked as "challenge" provide additional practice for interested students. We believe that any student in this class who completes the standard exercises should be able to complete the "medium" difficulty challenge.

For more advanced students, you might find the more difficult ... exercise(s) to be more interesting. Feel free to skip the standard exercises if you think they are insufficiently challenging. You can also look at previous labs for challenging exercises.

If you feel that this week's challenges are too hard for you, feel free to do a challenging exercise from last week which should be easier now that you know more.

## Exercise 1: (standard)



## Exercise : Tower of Hanoi (challenge, very hard)

In this exercise, you will implement the fastest solution to solve the tower of hanoi problem for any number of blocks. The tower of hanoi is a well known toy/problem where you need to move a tower from rod **A** to rod **C**. The tower exist of several disks with different size. While, this problems seems trivial, it is not when you need to follow the following rules: 
* Only one disk can be moved at any point.
* A move is defined as taking the upper disk of a stack and place it on top of another stack/rod. This can be an empty rod.
* A disk can not be placed on top of a smaller disk.

Below you can see the start position of the tower of hanoi problem with three disks. Note, that the tower of hanoi can have any number of disks.

![image](/LeidenITP/assets/images/lab10/hanoi.png)

This problem is very well suited for a recursive function and if you really want a challenge you can open the file `tower_of_hanoi.py` and try to solve the problem yourself. As a guideline, the number of steps it takes to solve this problem is $2^n-1$, where *n* is the number of disks.