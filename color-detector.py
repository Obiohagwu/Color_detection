
# We start with creating an argument parser using arg parser library to insert user image input from terminal

import argparse
import numpy as np
import pandas as pd
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
#Reading image with opencv
img = cv2.imread(img_path)


# then we proceed to read the csv files with pandas
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

global b,g,r,xpos,ypos, clicked
clicked = False
r = g = b = xpos = ypos = 0



# formula for measuring dictance(d) is:
# d = abs(Red – ithRedColor) + (Green – ithGreenColor) + (Blue – ithBlueColor)

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

# Now we can create the draw_function
# We check if the left button is double clicked, then we assign the values of b, g, r. Along with x,y positions of mouse

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

# With these lines, we named our window as ‘image’ and set a callback function which will call the draw_function() whenever a mouse event occurs.


         
while(1):
    
    cv2.imshow("image",img)
    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness) -1 thickness fills rectangle entirely
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display ( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) + ' G='+ str(g) + ' B='+ str(b)

        #cv2.putText(img,text,start,font(0-7), fontScale, color, thickness, lineType, (optional bottomLeft bool) )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
  #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)

        clicked=False

    #Break the loop when user hits 'esc' key 
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()
