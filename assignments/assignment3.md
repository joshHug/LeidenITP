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

# Assignment 3: word n-grams & generating text

**Deadline: 1 December 2023 23:59**

Hand in your assignment via [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322). See the "Delivery" section for instructions.

## Program

In this assignment, you need to program a family of langauge models called word n-grams, from now we will just call it a n-gram. This family of language models is able to *learn* from a corpus and afterwords is able to generate/*predicts* new sentences. A corpus is just a fancy word for a (set of) file(s) that contain text which is used to train language models. However, they often also contain other stuff like the grammar for each sentence. N-grams are one of the earliest language models of natural language processing (NLP), mainly due to their simplicity, but also due to their somewhat effectiveness and low need for data.

The idea of an n-gram is that you create a huge lookup table that contains all the probabilities that any word comes after any history. Here, a history can be any number of previous words. Simply said, it uses the fact, that words are commonly in a certain order. So, even though "and" is very common, most likely the chance of it being after the word "the" is very small. This way words that are often together are generated together creating some form of sentences. The "*n*" in n-gram stands for how many words are connected. A unigram model consist of only one word, so no history, while a bigram model consists of a history of one word and one word that follows the history. Because n-grams are completely based on statistics, and therefore the given corpus, you can ask the question if they really *learn* or *predict* anything.

This assignment consists of three parts: reading a text file, *training* the models, and generating sentences. You will also implement three models: a unigram model, a bigram model, and a trigram model. For the training we will use the *abc* corpus which can for instance be found in the **NLTK** library of python. 

To make it a bit easier, we did some parsing of the corpus to make each sentence span exactly one line, removed all characters that are not letters and made everything lower case. Parsing a raw text is an assignment on its own, therefore you can just use the text file "abc_corpus.txt".

In this assignment you will ask the user which model they want to train, how many sentences need to be generated with the learned model and how long each sentences can be at most.

## Template

Each part can be found in the `assignment3.py` file on [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322), which also provides a template. While it is not mandatory to use this file, it is highly recommended. You are allowed to add more functions and/or split the current functions into several functions.

You are also free to add functionality or give the program your "personal touch", but make sure that the program remains understandable to us and the basic functionality is included.

If you use the template, we added some unittest to help you check if your functions `parse_text_file` and `make_ngram_model` work properly. However, we only added some very basic tests and this does NOT guarantee that your functions are indeed correct.

For each part there is a function in this framework, see below for more details. However, it is up to you to write a script that makes use of these functions and completes the basic functionality as described in the grading criteria.

### Parse Text File

In the `parse_text_file` function you will parse a file and return a list of sentences. Parsing means reading a text file and converting it from one format to another. For this assignment, we will read the text file `abc_corpus` and extract the sentences from it into a list of sentences. A sentence consists of a list of words and should start with a special word token `"\<s>"` and end with `"</s>"`. The goal of parsing is to make from a general written text or speach, a format that a computer can understand. While this sounds easy, there are a few things to consider:
- No matter if a word is written with upper or lower case letters it should be the same word.
- We are only interested in letters and not special characters.
- We need to find where a sentence ends.
- Numbers should be ignored.

 There are many more things to consider, but to make it a bit easier we preprocessed the text for the most part. For now, each line in the document contains one sentence that needs to be split into words. Each sentence should start with a special word `"<s>"` and end with `"</s>"`. Also, all punctuation should be removed. If a line is empty it should be skipped.

For example, the following `text.txt` file:
```text

This is a test sentence.


```
This file should be parsed into the following list:
```python
[["<s>", "this", "is", "a", "test", "sentence", "</s>"]]
```

### Make Ngram Model

To create an n-gram model, we're essentially building a predictive model for words in a sentence. This model is represented as a model-dictionary, where the keys are "histories" and the values are word-dictionaries that map possible next words to their probabilities. Thus, a word-dictionary has as key a word and as value a probability. A "history" of a word consists of a number of words preceding that word, depending on the *n* in n-gram. This can be zero words to many words. In this assignment, we will implement three n-gram models: unigram, bigram, and trigram. Let's break down how this works for each n-gram model.

1. **Unigram Model**:
   - In the unigram model, we don't consider any previous words. This means that the history consists of no words. Therefore, each word's probability is independent of its position in the sentence.
   - To make the model consistent with the other models, the model-dictionary has only one key which is a special `"<any>"` token that represents any word.
   - The values in this word-dictionary are the probabilities for each word. 
   - A unigram model does not have the start token `<s>` as key in the model-dictionary.

   For example:
   ``` python
   {"<any>": {"house": 0.01, "dog": 0.04, "nice": 0.02, "red": 0.01, "</s>": 0.002, ...}}
   ```

2. **Bigram Model**:
   - In the bigram model, the history consists of just the previous word in the sentence, and this previous word influences the next word.
   - The model consists of a model-dictionary with as keys each unique previous word.
   - Each previous word key has a word-dictionary of possible next words with their probabilities.
   - A bigram model has the start token `<s>` as a key in the model-dictionary.

   For example:
   ``` python
   {"the": {"house": 0.01, "dog": 0.04 ...}, 
    "is": {"nice": 0.02, "red": 0.01, "</s>": 0.001, ...},
    "<s>": {"the": 0.01, "a": 0.004, ...}, 
    ...}
   ```

3. **Trigram Model**:
   - In the trigram model, the history consists of the previous two words, and these two previous words influence the next word.
   - The model consists of a dictionary with each unique combination of the two previous words as a key.
   - Each key has a dictionary of possible next words with their probabilities.
   - A trigram model has the start token `<s>,<s>` as a key in the model-dictionary, and several keys consisting of the start token and a word which has the format `<s>,...`.

   For example:
   ``` python
   {"the,house": {"is": 0.01, "has": 0.04 ...}, 
    "is,a": {"book": 0.02, "house": 0.01, "</s>": 0.003, ...} 
    "<s>,the": {"house": 0.01, "chair": 0.004, ...}, 
    "<s>,<s>": {"the": 0.01, "a": 0.012, ...},
    ...}
   ```

4. **General Notes**:
   - All models exclude the start token `"<s>"` from the word-dictionaries, as the start of a sentence can not be in the middle of a sentence.
   - The end token `</s>` is added as an option for a next word in all models, i.e., it can be a key in the word-dictionaries. However, it should not be added as a key to the model-dictionary, as it denotes the end of a sentence which can not be in the middle of the sentence.
   - To calculate the probability of each word in the n-gram model, you count how many times a specific word follows a particular history, denoted as `count(word | history)`, and then divide it by the total number of occurrences of that history, represented as `sum(history)`.
   - Essentially, the probability calculation is: `count(word | history) / sum(history)`. This quantifies how frequently a specific word follows certain other words in the given corpus. This approach allows us to model the chance of a specific word following a certain history, which enables us to generate more meaningful text based on historical word patterns.
      For example, for a bigram model, if the corpus counts a 100 times the word "has" and the word "a" occurred 5 times after "has", than "a" has a probability of 0.05 given the history "has".

### Predict Sentence

In the `predict_sentence` function you will implement a sentence predictor. To generate a sentence using a n-gram model, follow these guidelines:

1. Initialize the history by appending an appropriate number of start tokens `"<s>"`, see the model descriptions above. For the unigram model, you do not add the start token `"<s>"`. The history always begins with `"<any>"`.
2. Now, you can use the history in the model-dictionary to get the word-dictionary. The keys of this word-dictionary are the possible next words and their values are the probability of that word. Use a weighted random function to get a new word. Hint: Just using `rng.choice(word-dictionary.keys())` will not work as now each word has the same chance to get chosen. Take a look at the [documentation](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html#numpy.random.Generator.choice) of rng.choice. Here, you can find how to make a weighted random choice. `rng` stands for random generator and needs to be created before using it. This can be done with the code `rng = np.random.default_rng(seed=42).`
3. When you have your next word, update the history and go back to step 2, unless step 4 applies.
4. The sentence prediction process will halt when it encounters the `"</s>"` token or reaches the maximum sentence length (given by `max_sentence_len`).
5. Each generated sentence should conclude with a period ".".
6. Once you have generated the desired number of sentences (given by `n_sentences`), save them to a text file named `f"generated_{name}_sentences.txt"` (here name is the name of the model). Each sentence should occupy its own line in the text file.

## Dry code (Don't repeat yourself)

During this assignment, you will be graded on how well you wrote your code, in particular if your code is *dry*. This means that everything should only be defined once and no code should be repeated. This is more elaborated than it sounds. For example, if you have an `if` `else` control-flow and both contain a few lines of similar code then it is not dry. This could be solved by removing the similar code outside the `if` `else` control-flow. In other option would be to write a function that executes the similar code, and call the function in the `if` and `else` statement. Not dry code could look like this:
```python
if check_first_name(name):
   name = name.lower()
   print(f"The first name of this person is {name}")
else:
   name = name.lower()
   print(f"The last name of this person is {name}")
```

The dry code could be:

```python
name = name.lower()
if check_first_name(name):
   print(f"The first name of this person is {name}")
else:
   print(f"The last name of this person is {name}")
```

If `name = name.lower()` can not be placed outside the `if else`, a function can be used. Such that the code is still dry. Below an example for such case. 

```python
def clean_name(name):
    return name.lower()

if check_first_name(name):
   print(f"The first name of this person before cleaning is {name}")
   name = clean_name(name)
   print(f"The first name of this person is {name}")
else:
   name = clean_name(name)
   print(f"The last name of this person is {name}")
```

There are a few reasons why writing *dry* code is important. Not only does it make your code shorter. Often it is more readable and it can save you time writing the same code over and over. Maybe, the most important reason is your code is easier to update and to bugfix. Let's go through a scenario together. You find a bug in the code example above. This bug consists of a first name that has whitespace around it and you do not want extra spaces in your print statement. Now, you update your code by adding `.strip()` at line 2. This solves your problem. Two months later a co-worker comes to you saying your code prints extra white spaces. You are confused because you solved the problem. However, you only changed it for first names and not for last names. This is a very common mistake made in large code basis. However, if you had made the code *dry* this would not have happened because there is only one place where you reformat `name`.

So, what you should have learned about the example above is that writing *dry* code not only means not typing the same line of code somewhere, but that it means not coding the same functionality twice. 

## Grading

*Implementing the basic functionality will give you 5 points out of 10.*

**Basic functionality**: Your program does the three main parts, reading in a file (at least the `abc_corpus.txt`), making the unigram and bigram model and generate sentences with each one. In the template description you can find a more detailed list of what the basic functionality should be. (5 points)

*The remaining 5 points can only be obtained after completing the basic functionality. The following additional functionality will get you the additional 5 points, the grade is capped at a 10:*

**User interface** The program should run according to the user input. This should consist at least of which file the n-gram should be trained on, which n-gram model to train and how many and how long the generated sentences should be. (1 point) 

**Comments**: Include comments to explain the difficult parts of your code. It is generally good practice to write a comment for each code block. (0.5 points)

**Trigram model**: Also implementing the trigram model will earn you an additional point. (1 point) 

**Dry code**: *Dry* code means that you do not repeat code. So, if you wrote code to make an unigram model, then that same code should also be able to make the other models. The assignment is set up in such a way that you only need the four definitions and only in the `set_history` function you have to make a distinction between the models. If you adhere to this concept you will get an additional point. Another half a point is awarded if the rest of your code is also *dry*. Note, that if you expend the codebase with additional functionality you can use extra functions and still get the point. (1.5 points) 

**New Coding Concepts**: This assignment lent itself for five programming concepts that we do not have seen yet in the lectures. These are `match cases` as a replacement for `if elif elif elif ...`, `defaultdict` as a replacement for `dict`, and `lambda` functions that replace a named function e.g. `def namefunction(): return`. For the fourth new coding concept you got the partial code namely `create_defaultdict`. Find out what the name is of this concept and how it works and what it does. You can write your answer in the docstring after *EXPLANATION:*. Lastly, you can use a callable `class` object to replace `create_defaultdict`. All five concepts earn you +0.25 points. To get all points make sure your `create_defaultdict` code is correct including the explanation, but you do not need to use it anywhere in the code (because the lambda and callable class are used for the same purpose). (1.25 points) 

**Extra Bonus**: Add some "personal touch" to the program or extend some functionality. You can also try to improve the parser in `parser.py` and remake the corpus. Make sure you included all your changes in the zip when you hand it in. (0.5 points)

## Tips

Tips to for the function `make_ngram_model`:
- Before making the dictionary with all probabilities, make a similar dictionary with the counts.
- To make the code cleaner, you can use a `defaultdict` instead of a `dict`. This adds the benefit that if a key does not exist the value will be a default value and not raise the error KeyError. To make a defaultdict of defaultdicts with int values. You can use `defaultdict(create_defaultdict(int))`, where `create_defaultdict` is a function that returns a defaultdict. This defaultdict has as default the input of the function `create_defaultdict`.
- If you want to loop over the keys of a dict you can type `for key in dict:`, If you want to loop over the values add .values() thus `for value in dict.values():` and for both you can use `for key, value in dict.items():`

Tip for the function `predict_sentence`:
- use np.random.choice, read the [documentation](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html) for more ideas. 

## Delivery

Once you are sure about your program, save a copy of your `.py` file with your **student number** and the **assignment number** as the file name. For example, if your student number is 123456, then save your copy as `123456_3.py`.

If your program consists of multiple files, then compress these into a `.zip` file with the same naming scheme: `123456_3.zip`. Please make sure to **not** include your `venv` folder if you do this. Your submission should not be larger than 50kB.

Next, upload your `.py` or `.zip` file on [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322) under "Assignments" > Assignment 3 - word n-gram & generating text.
