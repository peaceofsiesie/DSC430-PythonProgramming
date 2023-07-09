# Name: Sierra Salaam
# Date: Feburary 20, 2023
# Assignment: 0701
# Video Links: 
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."

import math
import SierraSalaam_Assignment0701 


class Point(): 

    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord
        
    
    def setx(self, xcoord):
        self.x = xcoord
    
    def sety(self, ycoord):
        self.y = ycoord

    def getx(self):
        return self.x

    def gety(self):
        return self.y
    
    def distance(self, other):
        return math.sqrt((self.xcoord - other.xcoord)**2 + (self.ycoord - other.ycoord)**2) #square root (x1-x2) + (y1-y2)

    def __repr__(self):
        return "This is ", self.x, "and", self.y

class Ellipse():
    
    def __init__(self, f1, f2, width):
        self.f1 = f1
        self.f2 = f2
        self.width = width


    def totalWidth(self, other):
        
        sumlength = Point.distance(self.f1, other) + Point.distance(self.f2, other)

        if sumlength <= self.width:
            return True
        return False

    #boundary of the ellipse 
    
    def __repr__(self):
        return "This ", self.width



def computeOverlapOfEllipses(e1, e2):


    #create random darts 
    # come up with a good frame
    #threshold to make sure
    pass 

def frame():
    # come up with a box and output of lrtb 
    pass

   
#create random darts inside the frame
#import random class
#for loop i in range 10000 darts create random points 
# random in bounder x 1 - 2

#import the previous assignment

def checkpoint():
    #if the point is inside the ellipse 1 and e 2
    #then incrument the count 

    
    pass

def main():
    pass 


'''
Notes about the assignment

a + b = w
w is the length of the long axis of the ellipse

is a point within the ellipse
a+b < ? = W (x1, y1), (x2, y2), w

method in the ellipse class that accept
 a point and returns true or false
 if the point is in the ellipse

 if the point is outside the ellipse
 then it is greater then w

What is the area of two overlapping ellipse?
put a box around the two ellipse

Create a box and get the L, R, T, B of ellipse
Find out what L should be
Take all the x values on the points for the 2 ellipse
get the min of the x values and go little bit over.  Take 
both ellipse and take the max w of both ellipseand go left go over a little bit more  

what is the area of two overlapping ellipses
Place random points inside the box using random generator
create random x and random y to get the point

take count of the hits, how often am I inside both ellipse by call the 
ellipse function on both of the ellipse

The area of the box
n - number of random points
hits - the number of random points that fell within both ellipses

calculate the area it overlaps

first and second ellipse
point A - 0,0
point B 0,0
w = 2

anwser should be pie

Strategy - 
breaking it down in small parts 
write a main function which each line is english 
the helper function

e1 bigger e2 smaller test to the see if area is the same number
pi(a,b)

One Task at a time - keep things simple 

'''