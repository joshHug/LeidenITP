---
layout: minimal
title: Lab 13
description: &desc 1 December, 2023 - Game Lab
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

Welcome to week 14, lab 13!

## PyCharm Recap

This week we continue using PyCharm and running code in the terminal. In [lab 7](https://joshhug.github.io/LeidenITP/labs/lab7/) you can find information about: installing anaconda, opening projects, configuring unittests, reading unittests results, and debugging.

## Overview of This Lab

This week, the structure of the lab is a bit different. In the first 11 labs, we have covered the basic programming principles and the ways to use them in Python. It is important that you take the time to finish the previous labs and practice with each programming concept. You should only attempt this lab once you have finished all eleven of the previous labs. 

This lab is an extra special difficult challenge which contains several, hopefully fun, challenge exercises. These exercises will focus on programming a simple game or simulation. The idea is that you can either try something yourself or follow a set of instructions to implement snake.

Also below, you can find an overview where you can practice certain programming concepts.

Overview programming concept and exercise:
 * Numpy: [Lab 7](https://joshhug.github.io/LeidenITP/labs/lab7/#lab-7)
 * Dictionaries: [Lab 9](https://joshhug.github.io/LeidenITP/labs/lab9/)
 * Classes: [Lab 8](https://joshhug.github.io/LeidenITP/labs/lab8/), [Lab 9](https://joshhug.github.io/LeidenITP/labs/lab9/), and [lab 10](https://joshhug.github.io/LeidenITP/labs/lab10/)
 * Iterators & Generators: [Lab 9](https://joshhug.github.io/LeidenITP/labs/lab9/)
 * Recursion: [lab 10](https://joshhug.github.io/LeidenITP/labs/lab10/)
 * Visualization: [lab 11](https://joshhug.github.io/LeidenITP/labs/lab11/)
 * Comprehensions: [lab 11](https://joshhug.github.io/LeidenITP/labs/lab11/)

[In extra exercises](https://joshhug.github.io/LeidenITP/labs/extra_exercises/), you can find useful python functions and practice implementing them yourself.

## Implementing Your Own Game (challenge, very hard)

During the lecture, you got a basic understanding on how to make a pong game. In this exercise, you can make whatever you want and have fun. While you can stop reading here and open a new file and start working on your game/simulation, you can also use the framework we implemented as a starting point.

### The Framework

The framework can be found in the file `simple_loop.py`. Here, you can find a `BaseGame` class which implements for you the game loop and regulates the frame rate. The idea is that you make your own class and inherit from this `BaseGame` class. An example can be found in the folder `change_color_game`. Here, a simple simulations is shows that changes color each frame rate.

Below, you can find the code to use the framework. As you can see `YourGame` inherits from the `BaseGame` meaning that, as long as you don't redefine/overwrite the base class methods, you don't have to write these methods yourself. In this case, you can make a game by implementing the `setup` method and `draw` method.

```python
import pygame
from simple_loop import *

class YourGame(BaseGame):
    def setup(self):
        pass

    def draw(self):
        pass

if __name__ == "__main__":
    game = YourGame()
    game.run()
```

The `setup` method can be used to create/initialize variable you need, change the resolution by changing `self.resolution`, or change the frame rate by adjusting `self.frame_rate`. This must be done is setup because it is called before the while/game loop and before making the window you make your game in. In the `draw` method you implement your game. Each frame the `draw` method is called once. 

To start your game you need the last two lines of the code above. You need to make a game object from your class and call the method `run`.

## Snake Game

To make coding the snake game more approachable, we have set up several folders with different parts implemented or not. This way you can focus on making on part work and directly see if it works. Normally, when you make a game you have to implement several functionalities at once to see if something works making debugging more challenging than we have seen so far. Also, to show you a version of a complete snake game, how it could work, and most of all how to structure it, we created the folder "completed_snake_game" 






