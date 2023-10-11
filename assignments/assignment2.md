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

# Assignment 2: Collecting moon stones

**Deadline: Tuesday 7 November 2023 23:59**

Hand in your assignment via [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322). See the "Delivery" section for instructions.


## Program

In this second assignment you're going to program a moon robot, which collects stones on the moon surface.

You are given an incomplete program, which asks the user for a moon size and then creates a square grid (NumPy array) containing zeros and ones. The ones represent the stones, whereas the zeros represent empty spaces. The moon can be of size 5, 6, 7 or 8. It will contain two stones by default.

Your task is to program a robot to collect both stones, while minimising the distance travelled by the robot. In other words: your robot has to find a shortest path.
The robot starts at coordinate `(0, 0)` (the upper left corner).
It can only travel horizontally and vertically, and every step has a distance of 1.
The robot picks up stones automatically when it's at the same coordinate as them.
The output of your program should consist of a list of visited coordinates, as well as the total distance travelled, as in the example below:

```
On what moon size do you want your robot to search (5, 6, 7 or 8)? 8

[[0. 0. 0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 1. 0.]]

Shortest path: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
Total distance travelled: 13
```

In particular, note that:
- The robot does not need to return to its starting position. It can stop after collecting the final stone.
- Your printed coordinates should include the robot's starting coordinate and the coordinate of the final stone collected by the robot.
- The travelled distance is not entirely equal to the number of visited coordinates.


## Template

You can use the template program below as a starting point. This template will provide you with the code necessary to generate the moon surface with a number of stones. While it is not mandatory to use the template, it is strongly recommended.
You are free to add functionality, change the layout or give the program your "personal touch", but make sure that the program remains understandable to us.

```python
import numpy as np

def main():
	moonSize, moon = get_moon()
	print(moon)

	# Steps that might help you getting started:
		# Find the location of both stones
		# Determine whether it is faster to first pick up stone 1 or stone 2
		# Travel the coordinates and keep track of your route
		# Print your route as well as the distance covered

# You get this function for free to retrieve the size of the moon from the user and generate a moon surface of the correct size. You're free to write your own.
def get_moon():
	moonSize = input("On what moon size do you want your robot to search (5, 6, 7, or 8)? ")
	# Check that moon size is an integer
	if moonSize.isnumeric():

		# Convert to integer
		moonSize = int(moonSize)

		# Check that moon size is between 5 and 8
		if 5 <= moonSize <= 8:

			# Create a 1D NumPy array with the correct number of stones and empty spots
			moon = np.array([0] * (moonSize * moonSize - 2) + [1] * 2)
			# Shuffle the array to randomise the locations of the stones
			np.random.shuffle(moon)
			# Convert to square 2D array to have a square moon surface
			moon = np.reshape(moon, (-1, moonSize))

			# Return the moon size and the generated moon surface
			return moonSize, moon

		else:
			# If moon size is too small or too large, rerun function to get new input
			print("Your input was too large or too small")
			return get_moon()

	else:
		# If moon size is not an integer, rerun function to get new input
		print("Your input was not an integer.")
		return get_moon()

# Start the program by calling the main() function
if __name__ == "__main__":
	main()
```


### NumPy arrays

The template code above uses the NumPy library as a convenient tool to generate a two-dimensional array as the moon surface. The moon surface's  (`type(moon)`) is `numpy.ndarray`, but you can generally treat it like a list of lists: you can access the value at coordinate `(3, 0)` (row 3, column 0) through `moon[3][0]` and you can iterate over its rows:
```python
for row in moon:
	print(row)
```
You don't need to use any additional NumPy functionality, though it is allowed.


## Grading

Implementing the basic functionality as described above will give you 6 points out of 10.

**Basic functionality**: Your program does everything described above without crashing (for example on bad user inputs). (5.5 points)

**Comments**: Include comments to explain the difficult parts of your code. (0.5 points)

The remaining 4 points can be obtained by implementing additional functionality:

**Pretty printing**: Instead of printing the robot's steps as a list of coordinates, show the steps on the moon surface itself by marking the coordinates and printing the moon surface again. You're free to mark it any way you want, as long as the robot's path is clear. (0.5 points)

**More stones**: Generate the moon with more than two stones and have your robot collect them all. You should still try to minimise the robot's path: finding a shortest path for an arbitrary number of stones is very difficult, so try to at least find a reasonably short path. (2 points)

**User menu**: Once you have implemented the options above, add them to a comprehensive menu in which the user can select the way of printing, the number of stones and any additional options you've added. Be careful of bad user inputs: your program should not crash. (1 point)

**Extra**: This bonus is for those who go the extra mile. Implement a smart algorithm, a polished user interface, or anything that shows outstanding use of programming. (0.5 points)


## Tip

The `main()` function in the template program lists some suggested steps to get you started:
- Find the location of both stones
- Determine whether it is faster to first pick up stone 1 or stone 2
- Travel the coordinates and keep track of your route
- Print your route as well as the distance covered


## Delivery

Once you are sure about your program, save a copy of your `.py` file with your **student number** and the **assignment number** as the file name. For example, if your student number is 123456, then save your copy as `123456_2.py`.

If your program consists of multiple files, then compress these into a `.zip` file with the same naming scheme: `123456_2.zip`. Please make sure to **not** include your `venv` folder if you do this. Your submission should not be larger than 50kB.

Next, upload your `.py` or `.zip` file on [Brightspace](https://brightspace.universiteitleiden.nl/d2l/home/240322) under "Assignments" > Assignment 2 - Collecting moon stones.
