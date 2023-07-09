# Name: Sierra Salaam
# Date: March 06, 2023
# Assignment: 0902 - Game of Life
# Video Links: https://youtu.be/Zj5MXj6hVDQ
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."


import numpy as np # import the numpy package
import copy # import the copy package
from array import * # import all the libraries in array package


def conway(s,p = 0.1): # create a function that will generate a random board
    "This function will display the baord" # docstring
    board = np.zeros((s,s)) # create an array that will produce all zeros
    
    random_sample = np.random.choice([0, 1], size=(s, s), p=[1-p, p]) # produce a random sample of 1 and 0 based on the probability set
    board[random_sample == 1] = 1 # when the probability of the spot is 1 change the spot on the board to one
    return board # return the board
    

def advance(b,t): # this function will geneate the game 
    "This function will generate the game based on the rules set" #docstring
    
    blst = b.tolist() # will transfer the array to a board
    
    time = 0 # set the counter of the time equal to zero
    r = len(blst) # set the number of the total rows
    c = len(blst[0]) # set th enumber of the total column

    while time < t: # run through the block of code below based on the t parameter
        newblst = copy.deepcopy(blst) # create a new copy of the current board
        for i in range(r): # loop through all the rows
            for j in range(c): # loop through all the columns

                nhcount = blst[i][(j+1)%c] + blst[i][(j-1)%c] + blst[(i + 1)%r][(j)] + blst[(i - 1)%r][(j)] #count the total of neighbor by left right up and down
                
                if nhcount < 2 and blst[i][j] == 1.0: # the rule that will generate when cell is underpopulated
                    newblst[i][j] = 0.0 # change the cell to 0
                elif nhcount > 3 and blst[i][j] == 1.0: # the rule that will generate when cell is overpopulated
                    newblst[i][j] = 0.0 # change the cell to 0
                elif nhcount == 3 and blst[i][j] == 0.0: # the rule that will generate when cell is reproduction state
                    newblst[i][j] = 1.0 # change the cell to 1
        

        time = time + 1 # a counter that will continue the loop

        oboard = np.array(blst) # set the old list back to an array board
        nboard = np.array(newblst) # set the new list back to an array board
        
        blst = newblst # assign the new list to the old list
   
        print("oldboard") # print statement 
        print(oboard) # print old board
        print("") # print a space
        print("newboard") # print statement
        print(nboard) # print new board
        print("")  # print a space

        if time != t: # if the time does not equal the set time inputed 
            print("New Iteration") # print statment
            print("___________________") # print statment
        


def main(): # the main function that will execute the program
    "This function will execute the program" # docstring
    testboard = conway(5,0.7) # generate the function of the board
    advance(testboard, 5) # generate the function that will produce the game
    
main() # function that will execute the program

