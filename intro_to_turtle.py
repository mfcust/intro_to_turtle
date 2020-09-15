#Step 1: import the turtle package like so:
import turtle

#Step 2:Create variable t, and set it equal to the turtle pen:
t = turtle.Pen()

#Great, now we can get started! Run your program and look at what you see in the output window
#turtle.Pen() gives you a blank canvas and a little arrow in the center of your screen. That is the turtle!!




#Move your turtle forward by 100 pixels using t.forward(100)




#You can set the speed at which your turtle travels by typing t.speed(integer between 1 and 10). Do that below:




#Have your turtle move backwards by 100 pixels by using t.backward(100)





#Have your turtle turn left or right a full 360 degrees (Hint: It will look similar to the two commands you just made with forward and backward)





#Draw a square with your turtle




#You can also set the color of the pen by using the following code: t.pencolor("color")
#Draw a triangle with your turtle, where each side of the triangle is a different color





#Typing out t.up() lifts the pen off the canvas so you are no longer drawing. t.down() puts the pen back down on the canvas so you can continue drawing.
#Try lifting the pen up, moving your turtle to a different location, and then putting the pen back down and drawing a straight line.





#t.clear() resets the canvas but leaves the turtle where you left it. t.reset() resets the entire canvas and moves the turtle back to the starting position.
#Try doing one of these now on the line below:





#Using what you know, draw two parallel lines using the turtle. Make sure you lift the pen up and put it back down when you do this so the lines aren't touching




#You can draw a circle using t.circle(radius, arc, steps). Use all three arguments and try to determine what each does:





#Bonus Challenges:
#Draw a square where the corners are missing




#Draw a spiral with your turtle. Hint: This is made easier by using a for loop!





#Hard: If you were able to complete the previous challenge, then try to change it so you each time you draw a line, you change your pen color.
#Hint: You will need a list, a for loop, and you must is the modulo operator!
