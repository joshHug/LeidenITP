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

Snake is a fun and not to hard game to implement. Here, we will implement the one player version of the game, which was popular on for example the dinosaurs called nokia phones. If you do not know how snake works you can find an example on [this website](https://playsnake.org/), and we encourage you to google how it works.

To make coding the snake game more approachable, we have set up several folders with different parts implemented or not. This way you can focus on making on part work and directly see if it works. Normally, when you make a game you have to implement several functionalities at once, to see if something works making debugging more challenging than we have seen so far. Also, to show you a version of a complete snake game, how it could work, and most of all how to structure it, we created the folder "completed_snake_game". You can complete the snake game for the following functionalities and difficulties:
 - [Snake From Scratch]() (challenge, very hard+)
 - [Snake From Scratch With Tips]() (challenge, very hard)
 - [Snake Controls]() (challenge, medium)
 - [Snake General Game Flow]() (challenge, hard)
 - [Snake Objects]() (challenge, medium)


For all versions of finishing the snake game, the vector2D class is already implemented. This class stores coordinates for the game. While it is not important for this lab and similar functionality could be achieved for numpy, it is a good example how to work with magic methods and keep the code dry.

### Snake From Scratch (challenge, very hard+)

In this version of the lab exercise you get the framework, but you need to implement the snake and apple class, the general game control flow, and the player controls. The only thing that is given is the vector2D class which can be used to store or do math with coordinates. This exercise should be completed in the folder `snake_game_from_scratch`.

For the general game control flow, you need to think what should happen each step of the game and how to draw that. To keep the method small and to adhere to the idea ["one function one purpose"](https://joshhug.github.io/LeidenITP/labs/lab12/#one-function-one-purpose), you should not code how the snake, for example, gets update but just code snake.update(). How the snake is update should be a method of snake. So, similar to lab 12, the code for changing the snake itself should be in the snake class and in the general control flow should only determine in which other snake methods (and other methods) are called. Hint: do not forget to paint the whole screen black each frame, otherwise frames will visually overlap each other. The general game control flow code should be coded in the `update` method of the `SnakeGame` class in the file `snake_game.py`. 

The snake object should contain all the functionality to handle things related to the snake. For example, there should be a method to draw the snake on screen or check if the snake collides with something else. You need to implement enough methods such that the general game loop just needs to call snake methods to check things or update things. In other words, a good snake class makes it possible to not use any attribute of a snake object outside the snake class itself. The snake class code should be written in the `snake.py` file.

The philosophy should be the same for the apple class. All thing related to the apple class should be implemented as methods of the apple class. The apple class code should be written in the `apple.py` file.

For both the apple and snake class an update and draw function are already given in the class. Each game object should have these methods. Your still need to write the code, but you can draw inspiration of what these methods should do from the doc-string.

Finally, if you have done the tasks above you have a moving snake and an apple which are visualized on the screen. However, to complete the game of snake, you need user input to control the snake. This must be programmed in the `draw` method of the `SnakeGame` below the comment: `# TODO, finish the user controls.`.

### Snake From Scratch With Tips (challenge, hard)

This version of finishing the snake game is the same as described in "Snake From Scratch", except that the methods and their purpose for the snake class and apple class are given. This should give some hints how to separate the general game control flow code from the snake and apple class code. This means that you only need to complete all method but to not have to add new methods. This exercise should be completed in the folder `snake_game_from_scratch_hints`.

### Snake Controls (challenge, medium)

In this version of the lab exercise, you will need to implement the game controls. The snake and apple classes are already implemented as well as the general game control flow. This exercise should be completed in the folder `snake_game_controls`.

When you run the game, you can see that there is already a moving snake and an apple which are visualized on the screen. However, to complete the game of snake, you need user input to control the snake. This can be programmed in the `draw` method of the `SnakeGame` below the comment: `# TODO, finish the user controls.`. Also, you need to add a method in snake that makes the snake change direction when an arrow key is pressed.

### Snake General Game Flow (challenge, very hard)

In this version of the lab exercise, you will need to implement the general control flow of the game. The snake and apple classes are already implemented as well as the controls. This exercise should be completed in the folder `snake_game_loop`.

For the general game control flow, you need to think what should happen each step of the game and how to draw that. To keep the method small and to adhere to the idea ["one function one purpose"](https://joshhug.github.io/LeidenITP/labs/lab12/#one-function-one-purpose), you should not code how the snake, for example, gets update but just code snake.update(). How the snake is update should be a method of snake. So, similar to lab 12, the code for changing the snake itself should be in the snake class and in the general control flow should only determine in which other snake methods (and other methods) are called. Hint: do not forget to paint the whole screen black each frame, otherwise frames will visually overlap each other. 

Note, that the snake and apple class are already implemented. Check, which function might be helpful in the game loop. You should not have to implemented additional methods to snake or apple, nor should you change the attributes of the objects in the game loop. 

Now, complete the general game control flow code in the `update` method of the `SnakeGame` class in the file `snake_game.py`. 

### Snake Objects (challenge, medium)

In this version of the lab exercise, you will need to implement the snake and apple class. The general control flow is already implemented as well as the controls. This exercise should be completed in the folder `snake_game_objects`.

The snake object should contain all the functionality to handle things related to the snake. For example, there should be a method to draw the snake on screen or check if the snake collides with something else. You need to implement enough methods such that the general game loop just needs to call snake methods to check things or update things. In other words, a good snake class makes it possible to not use any attribute of a snake object outside the snake class itself. 

Now, complete the code in the `snake.py` file and `apple.py` file. All the methods that need to be implemented are already given including a description what they should do. If it is unclear try to add print statements to figure out how these methods are used and/or how the game works.



