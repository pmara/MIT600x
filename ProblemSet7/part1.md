PROBLEM 1: THE RECTANGULARROOM CLASS : 10.0 POINTS
==================================================

You will need to design two classes to keep track of which parts of the room have been cleaned as well as the position and direction of each robot.

In ps7.py, we've provided skeletons for the following two classes, which you will fill in in Problem 1:

 - RectangularRoom

   Represents the space to be cleaned and keeps track of which tiles have been cleaned.

 - Robot

   Stores the position and direction of a robot.

We've also provided a complete implementation of the following class:

 - Position

   Stores the x- and y-coordinates of a robot in a room.

Read ps7.py carefully before starting, so that you understand the provided code and its capabilities.

PROBLEM 1
---------

In this problem you will implement two classes, RectangularRoom on this page and Robot on the next.

For the RectangularRoom class, decide what fields you will use and decide how the following operations are to be performed:

 - Initializing the object

 - Marking an appropriate tile as cleaned when a robot moves to a given position (the function math.floor may be useful to you here)

 - Determining if a given tile has been cleaned

 - Determining how many tiles there are in the room

 - Determining how many cleaned tiles there are in the room

 - Getting a random position in the room

 - Determining if a given position is in the room

 - Complete the RectangularRoom class by implementing its methods in ps7.py.

Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. For reasonable representations, a majority of the methods will require only one line of code.)

Hint: During debugging, you might want to use random.seed(0) so that your results are reproducible.

PROBLEM 1: THE ROBOT CLASS : 10.0 POINTS
========================================

For the Robot class, decide what fields you will use and decide how the following operations are to be performed:

 - Initializing the object

 - Accessing the robot's position

 - Accessing the robot's direction

 - Setting the robot's position

 - Setting the robot's direction

Complete the Robot class by implementing its methods in ps7.py.

Although this problem has many parts, it should not take long once you have chosen how you wish to represent your data. For reasonable representations, a majority of the methods will require only one line of code.)

Note: The Robot class is an abstract class, which means that we will never make an instance of it. You've actually seen an abstract class already - the Trigger class from Problem Set 6!

In the final implementation of Robot, not all methods will be implemented. Not to worry -- its subclass(es) will implement the method updatePositionAndClean() (this is similar to the evaluate method of the Trigger class of PS6).
