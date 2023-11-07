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
 * Exercise 1: [Recursive Sequences]() (standard)
   * Exercise 1a: Standard implementation (standard)
   * Exercise 1b: Fast implementation (challenge, hard)
   
All students, regardless of experience, should be able to complete the ... standard exercises. Whether you complete all ... is up to you.

The ... exercises marked as "challenge" provide additional practice for interested students. We believe that any student in this class who completes the standard exercises should be able to complete the "medium" difficulty challenge.

For more advanced students, you might find the more difficult ... exercise(s) to be more interesting. Feel free to skip the standard exercises if you think they are insufficiently challenging. You can also look at previous labs for challenging exercises.

If you feel that this week's challenges are too hard for you, feel free to do a challenging exercise from last week which should be easier now that you know more.

## Hashable Objects

## Exercise : Hashable Number class (standard)

## Recursive Functions

Recursion is often an elegant way to write an algorithm. However, at one moment in time humans are often only capable of keeping track of a few recursive steps. For example, without practise people tent only to think a few steps a head in chess. Therefore, it is often hard to come up with a recursive algorithm. In A&DS, you will get a lot more practise with it but for now we want to give you some tips and tricks.

The first step into making a recursive algorithm is te recognize if a problem can be recursively solved (or is suitable for it). A problem is most suitable for recursion if, at one point in the algorithm, the next step can be calculated without knowing what the previous steps were and any outside information. For example, in chess you don't need to know what happened before a certain move to do the next. Ofcourse most people use certain strategies which consists of previous moves, but technically each bord configuration has its optimal move which can be determined by just examining the bord. 

The next step is to make the recursive algorithm which consists of a base case and a recursive step. Some people like to think about the base case first and vice versa. For now, let's start with the recursive step. 

The best tip for coming up with a recursive step is to think about a small step you can do that needs the same algorithm to solve the step but makes it a little bit smaller. This is a bit cryptic so let's examine an example. Let's say we want to solve the problem of summing up the following list of numbers:

```python
numbers = [1, 4, 3, 6]
```

Think about a small step you can do, which result in the same problem. The easiest solution would be just do nothing and repeat the problem. However, this would lead to an endless loop of doing nothing. So, we need to make the problem smaller. One option for calculating the sum of a list would be to take the first number, repeat the problem with the rest of the list and added those numbers together. Thus:

```python
def recursive_sum(numbers):
    ...
    
    first_number = numbers[0]
    smaller_problem = recursive_sum(numbers[1:])
    return first_number + smaller_problem
```

Note, that sometimes a recursive step splits into multiple smaller numbers. We could (needlessly) simulated this by splitting the list in two parts after taking the first number. This would create two smaller problems. *Just a note for more advanced programmers, the only upside of this approach would be to limit the recursive depth.*

```python
def recursive_sum(numbers):
    ...
    
    first_number = numbers[0]
    middle = len(numbers) // 2
    smaller_problem1 = recursive_sum(numbers[1:middle])
    smaller_problem2 = recursive_sum(numbers[middle:])
    return first_number + smaller_problem1 + smaller_problem2
```

There is a reason that both function have dots because we did not add a base case. A base case is a moment in the recursive algorithm when you can't make the problem smaller or the problem is at its smallest. Another way to say this is the base case determines when the algorithm needs to stop. Often a base case is just an if statement to check for a certain condition. In our example, there are two possible base cases. Think for a moment what these base cases could be? In other words, ask yourself when should you stop the recursion? 

Maybe the most natural base case would be when the input of the function is an empty list. The reason is very simpel the sum of an empty list is always zero. However, you could argue that when a list only contains one element you also know the sum. Below, you will find the final recursive algorithm. 

```python
def recursive_sum(numbers):
    if not numbers:
        return 0
    
    first_number = numbers[0]
    smaller_problem = recursive_sum(numbers[1:])
    return first_number + smaller_problem
```

## Exercise : Recursive Product (standard)

In the example above you saw how to implement `sum` recursively. Here, you will implement `product` recursively. The product of a list is all the number multiplied together. For example, the product of the list `[1, 2, 3]` is `6`. Open exercise `product.py`, follow the instructions and complete the recursive function `recursive_multiply`.

### Exercise extra: Recursive Unfold Product (challenge, hard)

In this extra exercise, you will expand the previous implemented recursive product to be able to calculate the product of nested lists. In other words, if you would unfold a nested list into a one dimensional list and take the product over that list. For example, the product over the following nested list `[2, [[3, 1], 4]]` would be `24`. Open exercise `product.py`, follow the instructions and complete the recursive function `recursive_unfold_multiply`.

## Exercise : Recursive Reverse (standard) 

In this exercise, we will recursively reverse a sequence which is either a list or a string. Open exercise `reverse.py`, follow the instructions and complete the recursive function. Even though unittest are provided, check with a small script and print statements how your function works and if it works as expected. Often, this is easier to debug then understanding why an unittest fails.

Tip: Try to think about how you could reverse one item in a list assuming the rest is already reversed.

## Exercise : Recursive Palindrome (standard) 

In this exercise, we will reversely check if a sequence is a palindrome and create a palindrome from a given sequence. A palindrome is a sequence of words, letters or numbers that reads the same backwards as forwards. For example, *radar* is a palindrome because when you reverse the word it is the same. Another example would be the sequence `[0, 1, 1, 0]`. It does not matter if a sequence has an oneven or even length as long as it is the same backwards as forwards. For more information on palindromes you can visit the [wiki](https://en.wikipedia.org/wiki/Palindrome).

Open exercise `palindrome.py`, follow the instructions and complete the recursive functions.

## Exercise : Recursive Sequences (standard)

Last week, you made iterable classes for several integer sequences. In this week's exercise, you will make a recursive function to calculate a specific index in the sequence. In this exercise, we will use the following sequences:

```text
 - Fibonacci        (0, 1, 1, 2, 3, 5, 8, 13, 21, 34) p(n) = p(n-2) + p(n-1)
 - Tribonacci       (0, 0, 1, 1, 2, 4, 7, 13, 24, 44) p(n) = p(n-3) + p(n-2) + p(n-1) 
 - Powers of three  (1, 3, 9, 27, 81, 243, 729, 2187) p(n) = p(n-1) * 3
 - factorial        (1, 1, 2, 6, 24, 120, 720, 5040)  p(n) = p(n-1) * n
```

### Exercise a: Standard implementation (standard)

Open exercise `recursive_sequences.py`, follow the instructions and complete the recursive functions.

### Exercise b: Fast implementation (challenge, hard)

Even though recursive function are very elegant solutions in a lot of situations, often they are not very fast in their basic form. Let's investigate what behind the scenes is needed to calculate the 8th fibonacci number. Open this [link](https://cscircles.cemc.uwaterloo.ca/visualize#code=def+recursive_fibo(n)%3A%0A++++if+n+%3C%3D+1%3A%0A++++++++return+n%0A++++n_1+%3D+recursive_fibo(n-1)%0A++++n_2+%3D+recursive_fibo(n-2)%0A++++return+n_1+%2B+n_2+%0A%0A%0Aa+%3D+f%22The+8th+fibonacci+number+is+%7Brecursive_fibo(7)%7D!%22%0Aprint(a)&mode=display&raw_input=&curInstr=0) and in frames you can see the stack of recursions. Note, how many steps it takes to calculate the 8th fibonacci number. Think about why it takes so many steps?

You probably noticed that a lot of fibonacci number are calculated numerous time. You can draw a calculation tree which shows you this very clearly. Below you can see such tree. Here, you can see the steps that need to be taken to calculate the 7th fibonacci number.

![image](/LeidenITP/assets/images/lab10/calculation_tree.png)

As you can see, calculating the fibonacci sequence this way is not very efficient. Imaging you need multiple fibonacci number during your program, this would be very slow and inefficient. The core problem is that each recursion you have two recursion steps. An easy solution would be to just remember all the fibonacci numbers you calculated. Open this [link](https://cscircles.cemc.uwaterloo.ca/visualize#code=FIBO_SEQ+%3D+%7B0%3A+0,+1%3A+1%7D%0A%0Adef+recursive_fibo_memory(n)%3A%0A++++try%3A%0A++++++++return+FIBO_SEQ%5Bn%5D%0A++++except+KeyError%3A%0A++++++++n1+%3D+recursive_fibo_memory(n+-+1)%0A++++++++n2+%3D+recursive_fibo_memory(n+-+2)%0A++++++++tmp+%3D+n1+%2B+n2%0A++++++++FIBO_SEQ%5Bn%5D+%3D+tmp+%0A++++++++return+tmp%0A%0Aa+%3D+f%22The+8th+fibonacci+number+is+%7Brecursive_fibo_memory(7)%7D!%22%0Aprint(a)&mode=display&raw_input=&curInstr=0) and have a look how this would work. Notice, that this code takes significantly fewer steps to calculate the 8th fibonacci number. 

Ofcourse rewriting both codes would result in a different number of steps on the waterloo website. However, we can also have a look at speed. Open `recursive_speedtest.py` and run the file. The *35th* fibonacci number is chosen to show the difference but make the wait time manageable. you can try different numbers to see what happens. However, keep in mind that going from the *n* to *(n+1)* fibonacci index takes almost twice as long for the basic implementation.  

In `recursive_speedtest.py` is also a test added to calculate the *900th* value of the sequence power of three. Here, it does not matter which implementation you use. Why does it not matter now? (think about how this calculation tree would look like).

The fast recursive function for the fibonacci sequence is already implemented in the examples. Now, make a fast recursive function for the sequences:

```text
 - Padovan     (1 ,1 ,1 ,2 ,2 ,3 , 4, 5, 7, 9)   p(n) = p(n-3) + p(n-2)
 - Tribonacci  (0, 0, 1, 1, 2, 4, 7, 13, 24, 44) p(n) = p(n-3) + p(n-2) + p(n-1) 
```

Open exercise `recursive_sequences_memory.py`, follow the instructions and complete the recursive functions. 

A final educational note, coding a recursive function where you remember previous calculation is often called dynamic programming. In your next course, A&DS, you will learn more about this.

## Exercise: Tower of Hanoi (challenge, hard or very hard)

In this exercise, you will implement the fastest solution to solve the tower of hanoi problem for any number of blocks. The tower of hanoi is a well known toy/problem where you need to move a tower from rod **A** to rod **C**. The tower exist of several disks with different size. While, this problem seems trivial, it is not when you need to follow the following rules: 
* Only one disk can be moved at any point.
* A move is defined as taking the upper disk of a stack and place it on top of another stack/rod. This can be an empty rod.
* A disk can not be placed on top of a smaller disk.

Below you can see the start position of the tower of hanoi problem with three disks. Note, that the tower of hanoi can have any number of disks.

![image](/LeidenITP/assets/images/lab10/hanoi.png)

This problem is very well suited for a recursive solution and if you really want to challenge yourself, you can open the file `tower_of_hanoi.py`, follow the instructions, and try to solve the problem. As a guideline, the number of steps it takes to solve this problem is 2<sup>*n*</sup> - 1, where *n* is the number of disks. For students that want a challenge but not that hard, you can read the explanation of the recursive algorithm below.

### Tower of Hanoi: Recursive Algorithm Explanation (challenge, hard)

The reason that the tower of hanoi problem lents itself very well for a recursive solution is that for any number of disks the same three steps need to be taken. When you want a tower from a *source* rod to a *destination* rod you can follow these steps:
 * Step one, move the tower except for the largest disk from the *source* rod to the *auxiliary*
 * Step two, move the largest disk from the *source* to the *destination* rod.
 * Step three, move the tower, that you previously moved to the *auxiliary* rod, from the *auxiliary* rod to the *destination* rod. 

You may have noticed that step 1 and 3 are not necessarily legal moves (step two is). However, step 1 and 3 are just moving a tower from one rod to another. Therefore, step 1 and 3 can be complete in the following exactly the same three steps described above. This looks like a infinite loop of repeating the same steps but note that each time the tower becomes one disk shorter. Thus, eventually step one and three are legal moves because the top of the tower only consists of one disk. 

Below, you can see an example for the a tower of hanoi with three disks. The first three steps can be seen here:

![image](/LeidenITP/assets/images/lab10/Hanoi3.png)

Then, step 1 in the previous image can be solved as follows:

![image](/LeidenITP/assets/images/lab10/Hanoi2a.png)

Finally, step 3 of the first image can be solved like this:

![image](/LeidenITP/assets/images/lab10/Hanoi2b.png)

Open exercise `tower_of_hanoi.py`, follow the instructions and complete the recursive function. 

## Exercise : Permutations (challenge, very hard)

In [lab 8 Using 2Dvectors: shortest path](https://joshhug.github.io/LeidenITP/labs/lab8/#using-2dvectors-shortest-path-challenge-hard), you could have used `itertools.permutations` to find the shortest path by just trying all orders of the list with coordinates. In this exercise, we will make our own permutation function. Generating permutations is not any easy task but making them recursive is a bit easier. Think about what each step of the recursion should do and how to yield each permutation back. Tip: First, just try to print all the permutations.

If you want you can open exercise `permutations.py`, follow the instructions and complete the recursive function. However, below we will give you some hints on how to do this.

Hints: 
 - Each recursive step, you reduce the size of the list by one.
 - Till now, you could make the problem smaller by taking, for example, the first item. Here, you need to loop over all possible items in the list and remove that item to make the list smaller. Otherwise, you will only get the first permutation.
 - If a function returns a generator, you can yield each item from that generator by looping through the generator and yield the item. For example, `range` returns a generator so, if my function should yield all values of `range` one by one, I can use:
```python
def test(n):
    for value in range(n):
        yield value
```
 - Think about memory and how you delete items from the list.