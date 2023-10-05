---
layout: minimal
title: Assignment 1
description: &desc Assignment 1
summary: *desc
has_children: true
has_toc: true
parent: Leiden ITP
permalink: /:path/
---

# {{ page.title }}
{: .no_toc .mb-2 }

{{ page.description }}
{: .fs-6 .fw-300 }

1. TOC
{:toc}

# Assignment 1: Higher or Lower?

**Deadline: 10 October 2023 23:59**

Hand in your assignment via [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322). See the "Delivery" section for instructions.

## PyCharm projects

It's recommended to start a new project in PyCharm for each assignment. Each project has its own files, which helps you in staying organised.

## Program

You must write an interactive program which plays the following simple guessing game with the user:

1. The program greets the player and the game starts.
1. The rules are explained clearly to the player.
1. The computer generates a random integer number between 0 and 10 (both included).
1. The computer asks the player to guess the number. If the player guesses correct, they get 10 points.
1. If the player guesses wrong, the computer tells the player whether the actual number is higher or lower than the guess. The player can try again. If they get it correct on the second try, they get 5 points.
1. Once the player has guessed the number or has guessed a wrong answer twice, the round is over and the process is repeated.
1. The player plays three rounds. If they get at least 15 points in total, they win. Otherwise, they lose.
1. Once the game is over, the player is asked whether they want to play another game. If so, the game starts again.

## Grading

**Functionality**: The basic functionality of the game is there. (5 points)

**Clarity**: The communication with the user is clear and the user does not get confused. (1 point)

**Interactivity**: The code is interactive in multiple aspects, asking the player for input and reacting accordingly. (1 point)

**Flexibility**: The code is able to take different types of input without outputting errors (example: "5", "five", "yes", "y", capital letters, lower case, etc.). (2 points)

**Ready to use**: The file is ready to use. The graders can unzip the archive, open the file in PyCharm and run it immediately. (1 point)

## Delivery

Once you are sure about your program, save a copy of your `.py` file with your **student number** and the **assignment number** as the file name. For example, if your student number is 123456, then save your copy as `123456_1.py`.

If your program consists of multiple files, then compress these into a `.zip` file with the same naming scheme: `123456_1.zip`. Please make sure to **not** include your `venv` folder if you do this. Your submission should not be larger than 50kB.

Next, upload your `.py` or `.zip` file on [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322) under "Assignments" > Assignment 1 - Higher or Lower?
