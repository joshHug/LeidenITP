---
layout: minimal
title: Lab 5
description: &desc Lab 5.
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

Welcome to week 5!

This week contains a number of further exercises on loops and a couple on dictionaries.

The lab session is also a good moment to ask questions about the first assignment, which is due on 10 October. If you prefer to focus on the assignment, it may be wise to do some of these exercises at home.

- [firstmul5](https://codingbat.com/prob/p248129)
- [countuptoneg](https://codingbat.com/prob/p247485)
- [scrabble](https://codingbat.com/prob/p266552)
- [collatz](https://codingbat.com/prob/p226751)
- [scrabble2](https://codingbat.com/prob/p233769)

For a quick refresher on loops, you can refer to [lab 4](/LeidenITP/2023/09/28/lab-4.html). For loops and dictionaries, you can also refer to the sheets of [lecture 3](https://brightspace.universiteitleiden.nl/d2l/le/lessons/240322/topics/2639539) and [lecture 4](https://brightspace.universiteitleiden.nl/d2l/le/lessons/240322/topics/2647943) on Brightspace.

Recall, in particular:
- you can use `continue` to skip an iteration of a loop:
```python
for num in list:
	# skip the loop body for all numbers smaller than 10
	if num < 10:
		continue
	# rest of the loop body
	...
```
- you can use `break` to terminate a loop:
```python
while num > 0:
	# terminate the loop if (the current value of) num is odd
	if num % 2 == 1:
		break
	# rest of the loop body
	...
```
- `return` also terminates a loop:
```python
for num in list:
	# return the first number smaller than 10
	if num < 10:
		return num
	# rest of the loop body
	...
```
- you can use dictionaries as a data structure to store key-value pairs. Recall the following about dictionaries:
```python
fruitbasket = { "apple":3, "banana":5, "cherry":50 } # initialise a dictionary
fruitbasket["apple"] += 2 # update a value
fruitbasket["mango"] = 1 # add a new value
del fruitbasket["banana"] # delete a value
fruitbasket.get("apple") # will return fruitbasket["apple"], as it exists
fruitbasket.get("pear") # will return None, since it doesn't exist
fruitbasket.keys() # will return a list of keys, such as ["apple", "banana", "cherry"]
fruitbasket.values() # will return a list of values, such as [3, 5, 50]
fruitbasket.items() # will return a list of key-value tuples, such as [("apple", 3), ("banana", 5), ("cherry", 50)]
```

As always, if you have any problems or additional questions, make sure to post them on [Brightspace](https://brightspace.universiteitleiden.nl/d2l/le/240322/discussions/List).
