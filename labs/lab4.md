---
layout: minimal
title: Lab 4
description: &desc Lab 4
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

## Sequences

Last week's lecture contained material on sequences, in particular on the following:

- **Indexing**: Recall that you can access individual elements in a list by providing their index: if `L = ["cat", "dog", "potato"]`, then `L[0] == "cat"`, `L[1] == "dog"` and `L[2] == "potato"]`. You can also use negative indices to start from the back: `L[-1] == "potato"`, `L[-2] == "dog"` and `L[-3] == "cat"`.
- **Slicing**: Additionally, you can use slicing to access a range of elements from a list by providing multiple indices: `L[0:2]` will give a list of the elements of `L`, from indices 0 to (**but not including!**) 2. For example, `L[0:2] == ["cat", "dog"]` and `L[2:3] == ["potato"]`.
You can also use negatives indices here: `L[0:-1] == ["cat", "dog"]`.
If you don't specify a starting index, it will default to the first one; similarly, if you don't specify a final index, it will default to the last one: `L[:2] == ["cat", "dog"]`, `L[1:] == ["dog", "potato"]` and `L[:] == ["cat", "dog", "potato"]`.
Slicing also works on strings: `"potato"[:3] == "pot"`.
- You can use `len` to get the length of a list or string, e.g., `len(L) == 3`.
- You can concatenate sequences with `+` and repeat them a number of times with `*`: `["cat", "dog"] + ["potato"] = ["cat", "dog", "potato"]` and `["cat", "dog"] * 3 = ["cat", "dog", "cat", "dog", "cat", "dog"]`.

Do the following exercises on CodingBat:
- [first_two](https://codingbat.com/prob/p184816)
- [combo_string](https://codingbat.com/prob/p194053)
- [left2](https://codingbat.com/prob/p160545)
- [reverse3](https://codingbat.com/prob/p192962)


## Loops

Last lecture covered loops, in particular the basics of while- and for-loops. Both types allow you to repeat something multiple times:
- **While-loops** repeat something as long a given condition is true. For example, the following loop will keep doubling a given number until it is at least 1000. Note that, if the number is 0, this will never stop.
```python
while number < 1000:
	number *= 2
```
- **For-loops** repeat something a set number of times, once for every element in a given sequence. For example, the following loop will print the squares of the integers 0 to 9:
```python
for i in range(10):
	print(i * i)
```
The following loop will print the first two characters of every string in a given list:
```python
for word in ["cat", "dog", "potato"]:
	print(word[0:2])
```

Do the following exercises on CodingBat:
- [pow5000](https://codingbat.com/prob/p273307)
- [sumn](https://codingbat.com/prob/p296329)
- [count_evens](https://codingbat.com/prob/p189616)
- [double_char](https://codingbat.com/prob/p170842)
- [count_hi](https://codingbat.com/prob/p167246)
- [centered_average](https://codingbat.com/prob/p126968)
<!-- - [sum67](https://codingbat.com/prob/p108886) -->
- [has22](https://codingbat.com/prob/p119308)



As always, if you have any problems or additional questions, make sure to post them on [Brightspace](https://brightspace.universiteitleiden.nl/d2l/le/240322/discussions/List).
