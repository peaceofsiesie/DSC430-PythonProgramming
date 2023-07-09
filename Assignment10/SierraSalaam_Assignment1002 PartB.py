# Name: Sierra Salaam
# Date: March 06, 2023
# Assignment: 1002 - Final Project 2 - Closest Planet Part A
# Video Links:  
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."

import numpy as np # import numpy package 
import pandas as pnd # import pandas package
import matplotlib.pyplot as plt # import matplotlib package
import SierraSalaam_Assignment1001 as as1 # import previous assignment 

def simulationTwo():
    numday = 1001 # declare numbers of days 
    earthdistanceTracker = np.zeros((numday, 3)) # create a 2d array to take distance between plants and earth

    planetNames = ['mercury', 'venus',  'mars'] # name of the plants within simulation
    pvalues =  [(3.5, 88),(6.7, 225), (14.2, 687)] # radius and years of each plant

    df = pnd.DataFrame(earthdistanceTracker, columns = ['mercury', 'venus', 'mars'] ) #dataframe of the 2d array

    row = len(planetNames) # declare the length of the rows
    column = len(planetNames) # declare the length fo the columns

    planet1 = as1.Planet(9.3, 365) # set plant one as the radius and year of Earth

    for py in range(numday): # for the range in number of days produced
        for r in range(row): # range of the rows
            for c in range(column): # range of the columns
                planet2 = as1.Planet(pvalues[c][0], pvalues[c][1]) # declare plant 2 as one of the plants
                earthdistanceTracker[py][c] = as1.distance(planet1, planet2, py) # add the value to the array and calculate distance

    df.to_csv('Second Simulation') # create a csv file that will hold all the values within data frame 
    print(df) # print the data frame 

    df.plot() # create a plot for the data frame set
    plt.ylim(0,25) # create the scale for the y axis
    plt.xlabel("Years", size = 10) # create the title of x axis 
    plt.ylabel("Distance", size = 10 ) # create the title of y axis 
    plt.title("Measure of The Distance To The Earth", size = 15) # Create the title for the plot
    plt.show() # Show the plot


def main():
    simulationTwo()

main()




   


            



            

        




    
  
    
    


