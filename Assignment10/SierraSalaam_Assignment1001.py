# Name: Sierra Salaam
# Date: March 06, 2023
# Assignment: Final Project 1 - Planet
# Video Links: https://youtu.be/OsP7wRyzLRc
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."

import math # import the math package


class Planet(): # create a class to calculate the Planet
    'This class will calculate the position of the Planet' # docstring

    def __init__(self, radius, year): #initialize all the variables within the class
        'This method will initialize all the variable that are parameters within class' #docstring
        self.radius = radius # initialize radius of the circle
        self.year = year # initialize the total days within the year
     
    def position(self, day): # this method will calculate the position of the Planet
        'This method will calculate the position of the Planet' #docstring
    
        alpha = ((2 * (math.pi)) * day) / self.year # calculate alpha number within the circle
        xcoor = self.radius * (math.cos(alpha)) # calculate the x value 
        xcoor = round(xcoor, 2) # round up value to the 2nd decimal
        ycoor = self.radius * (math.sin(alpha)) # calculate the y value 
        ycoor = round(ycoor, 2) #  round up value to the 2nd decimal 

        return xcoor, ycoor  # save and return the value the Planet coordinates
    
    def __repr__(self):
         'This method will return the representation of the Planet class' #docstring
         return f"" # return information about the class



def distance(Planet1, Planet2, year): # the function will return the distance of two Planets 
        'The function will return the total distance between two Planets' #docstring
 
        x1,y1 = Planet1.position(year) # produce the point of Planet 1
        x2,y2 = Planet2.position(year) # produce the point of Planet 2

        d = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)) # this will caculate within the distance between two points

        return d # save and return the distance value 

def main(): # function to execute the program  
     'This function will execute classes and functions within the program' #docstring
     mars = Planet(14.2, 687) # set the Planet radius and year with Mercery
     earth = Planet(9.3, 365) # set the Planet radius and year with Earth
     #mercury = Planet(3.5, 88)
     #print(mercury.position(33)) # print the postion of mercery at 33 year

     #print(distance(earth, mars, 732)) # print the distance between earth and mercery at 732 year



main() # execute the program