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

# Assignment 3: word n-grams, generating text

**Deadline: Tuesday 7 November 2023 23:59**

Hand in your assignment via [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322). See the "Delivery" section for instructions.


## Program

In this assignment, you will program a family of langauge models called word n-grams, from now we will just call it a n-gram. This family of language models is able to *learn* from a corpus and afterwords is able to generate/*predicts* new sentences. A corpus is just a fancy word for a (set of) files(s) that contain text which is used to train langauge models. However, they often also contain other stuf like the grammer of each sentence. n-grams are one of the earliest language models of natural language processing (NLP) mainly do to there simplicity, but also do to there somewhat effectiveness and low need for data.

The idea of an n-gram is that you create a huge lookup table where you can find for each history the probability that a certain word follows. Here, a history can be any number of previous words. Simply put it use the fact that words are commonly in a certain order. So, even though "and" is very common, most likely the chance of it being after word "the" is very small. This way words that are often together are generated together creating some from of sentences. The "*n*" in n-gram stands for how many words are connected. An unigram model consist of only one word, so no history. While a bigram model consists of a history of one word and one word that follows the history. Because n-grams are completely based on statistics and therefore the given corpus you can ask the question if they really *learn* or *predict* anything.

This assignment consists of three parts: reading a text file, *training* the models, and generating sentences. You will also implement three models: a unigram model, a bigram model, and a trigram model. For the training we will use the *abc* corpus which can for instance be found in the **NLTK** library of python. 

To make it a bit easier, we did some parsing of the corpus to make each sentence span exactly one line, remove all character that are not letters and made everything lower caes. Parsing raw text is an assignment on its own, therefore you can just use the text file "abc_corpus.txt".

## Template

A more detailed description of each part should do can be found in the assignment3.pt file, which als provides a template. While it is not mandatory to use this file, it is highly recommended.

You are also free to add functionality or give the program your "personal touch", but make sure that the program remains understandable to us and the basic functionality is there.

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
