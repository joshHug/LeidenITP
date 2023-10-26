---
layout: minimal
title: Assignment 3
description: &desc Assignment 3
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

**Deadline: ... 2023 23:59**

Hand in your assignment via [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322). See the "Delivery" section for instructions.


## Program

In this assignment, you will program a family of langauge models called word n-grams, from now we will just call it a n-gram. This family of language models is able to *learn* from a corpus and afterwords is able to generate/*predicts* new sentences. A corpus is just a fancy word for a (set of) files(s) that contain text which is used to train langauge models. However, they often also contain other stuf like the grammer of each sentence. n-grams are one of the earliest language models of natural language processing (NLP) mainly do to there simplicity, but also do to there somewhat effectiveness and low need for data.

The idea of an n-gram is that you create a huge lookup table where you can find for each history the probability that a certain word follows. Here, a history can be any number of previous words. Simply put it use the fact that words are commonly in a certain order. So, even though "and" is very common, most likely the chance of it being after word "the" is very small. This way words that are often together are generated together creating some from of sentences. The "*n*" in n-gram stands for how many words are connected. An unigram model consist of only one word, so no history. While a bigram model consists of a history of one word and one word that follows the history. Because n-grams are completely based on statistics and therefore the given corpus you can ask the question if they really *learn* or *predict* anything.

This assignment consists of three parts: reading a text file, *training* the models, and generating sentences. You will also implement three models: a unigram model, a bigram model, and a trigram model. For the training we will use the *abc* corpus which can for instance be found in the **NLTK** library of python. 

To make it a bit easier, we did some parsing of the corpus to make each sentence span exactly one line, remove all character that are not letters and made everything lower caes. Parsing raw text is an assignment on its own, therefore you can just use the text file "abc_corpus.txt".

In this assignment you will ask the user which model they want to train, how many sentences need to be generated with the learned model and how long each sentences can be at most.

## Template

A more detailed description of each part should do can be found in the assignment3.pt file, which als provides a template. While it is not mandatory to use this file, it is highly recommended. You are allowed to add more functions and/or split the current functions into several functions.

You are also free to add functionality or give the program your "personal touch", but make sure that the program remains understandable to us and the basic functionality is there.

If you use the template we added some unittest to help you check if your functions `parse_text_file` and `make_ngram_model` work propperly. However, we only added some very basic tests and this does NOT guarantee that your functions are indeed correct.

## Grading

Implementing the basic functionality will give you 6 points out of 10.

**Basic functionality**: Your program does the three main parts, reading in the file, making the unigram and bigram model and generate sentences with each one. Use the user input do run the programming accordingly. In the template is a more detailed list what the basic functionality should be. (5.5 points)

**Comments**: Include comments to explain the difficult parts of your code. (0.5 points)

The remaining 4 points can be obtained by implementing additional functionality:

**Trigram model**: Also implementing the trigram model will earn you an additional point.

**Dry code**: Dry code means that you do not repeat code. So, if you wrote code to make an unigram model, then that same code should also be able to make the other models. The assignment is set up just so you only need the four definitions and only in the `set_history` function you have to make a distinction between the models. If you adhere to this concept you will get an additional point. Note, that if you expend the codebase with additional functionality you can use extra functions and still get the point.

**Extra**: Try to make a quadragram, let the user choose the start of the sentences, or any other extra functionality. As a tip: You can read a bit more about n-grams to get ideas. Another option would be to improve the parser such that less nonsense words are in the corpus. You can do this by changing the code in `parser.py`. This is not an easy challenge so make sure everything else works before you start on this. Also, if you change `parser.py` make sure you hand it in as well (zip the files). Depending on how elaborate the extra functionality is and how many you have you can get an additional point.

**New Coding Concepts**: This assignment lent itself for three programming concepts that we do not have seen yet in the lectures. These are `match cases` as a replacement for `if elif elif elif ...`, `defaultdict` as a replacement for `dict`, and `lambda` functions that replace a named function e.g. `def namefunction(): return`. The last new coding concept you got the partial code for namely `create_defaultdict`. Find out what the name is of this concept and how it works and what it does. You can write your answer in the docstring after *EXPLANATION:*. Lastly, you can use a callable `class` object to replace `create_defaultdict`. All five concepts earn you +0.25 points.

## Tips

Tips to for the function `make_ngram_model`:
- Before making the dictionary with all probabilities, make a similar dictionary with the counts.
- To make the code cleaner, you can use a `defaultdict` instead of a `dict`. This adds the benefit that if a key does not exist the value will be a default value and not throw the error KeyError. To make a defaultdict of defaultdicts with int values. You can use `defaultdict(create_defaultdict(int))`, where `create_defaultdict` is a function that returns a defaultdict. This defaultdict has as default the input of the function `create_defaultdict`.
- If you want to loop over the keys of a dict you can type `for key in dict:`, If you want to loop over the values add .values() thus `for value in dict.values:` and for both you can use `for key, value in dict.items():`

Tip for the function `predict_sentence`:
- use np.random.choice check 


## Delivery

Once you are sure about your program, save a copy of your `.py` file with your **student number** and the **assignment number** as the file name. For example, if your student number is 123456, then save your copy as `123456_3.py`.

If your program consists of multiple files, then compress these into a `.zip` file with the same naming scheme: `123456_3.zip`. Please make sure to **not** include your `venv` folder if you do this. Your submission should not be larger than 50kB.

Next, upload your `.py` or `.zip` file on [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322) under "Assignments" > Assignment 2 - Collecting moon stones.
