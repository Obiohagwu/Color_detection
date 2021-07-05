Rough Explanation of some things

The first few lines of code are relatively unimportant as they are used to implement the argument parser, which is used to  input user image from command line

The mouse callback event window is used to display the input image based on mouse clicks or some other mouse event.
More precisely: The draw_function is the callback function called when the mouse event happens.
The window is used to display the image after callback function (draw_function) is called by double clicking.

In order to actually get the color we, use an ingenious method of calculating a distance(d) which tells us how close we are to a color and choose the one having minimum diatance.
Our distance is calculated by this formula:

d = abs(Red – ithRedColor) + (Green – ithGreenColor) + (Blue – ithBlueColor)
