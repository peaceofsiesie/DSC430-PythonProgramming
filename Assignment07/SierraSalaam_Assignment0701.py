# Name: Sierra Salaam
# Date: Feburary 20, 2023
# Assignment: 0701 - War and Random Numbers
# Video Links: https://youtu.be/UdBOWm9K6QY
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."

import random # import random class
from math import * # import all functions from math library
import statistics # import the statstics packages 



class WarAndPeacePseudoRandomNumberGenerator(): # a class that will read file and produce random numbers 
    'This class will produce random numbers using the Peace and War file.' #docstring
    def __init__(self, seed = 1000, step = 100, bits = 32, sumbit = 0): # the function that initialize values 
        'This function will initialize values' #docstring
        self.seed = seed # the number that will considered at the seed 
        self.step = step # the number of step the file would have to produce 
        self.bits = bits # the number of bits that would need to be produced
        self.sumbit = sumbit # the random number that is created 
        global charlst # make the  charlst global
        global bitslst # making bitlst global
        charlst = [] # create a list that will produce the two chars to compare
        bitslst = [] # create a list that will hold all the 1s and 0s
        
    
    def random(self): # the function will produce the random number
        'This function will produce the random number.' #docstring
        file = open('war-and-peace.txt', 'r') #read the file
       

        for i in range(32): # go through the range up to 32
            while len(charlst) < 2: # while length of charlst is less then 2
                
                if len(charlst) > 0: # if the length of the charlst is greater then 0
                    self.seed = self.seed + self.step # step additonal steps in the file
                    file.seek(self.seed) # find the point in the file
                    char = file.read(1) # read the value and assign it to variable char
                    charlst.append(char) # add the char value to list
                    #print("initial on second round", char) #comment out # print char produce here

                    while charlst[0] == char: # of index 0 value is equal to char
                        self.seed = self.seed + 3 # step additional three steps in the file
                        #print(char, charlst[0]) #comment out # print char produce here
                        file.seek(self.seed) # find the point in the file 
                        char = file.read(1) # read the value and assign it to variable char
                        charlst[1] = char # add the char to the list in index 1
                        if char == '': # if the char is blank
                            self.seed = 0 # change seed to 0
                            #print(char, charlst[0]) #comment out # print char produce here
                            file.seek(self.seed) # take the curse to the seed marker
                            char = file.read(1) # read the char 
                            charlst[1] = char # assign char to index 1 of charlst


                        #print("final char", char) #comment out # print char produce here
                
                else: # if the above condition is not true
                    file.seek(self.seed) # find the point in the file 
                    char = file.read(1) # read the value and assign it to variable char
                    charlst.append(char) # add the char value to list
                    #print("else", char) #comment out # print char produce here
        
            #print(charlst) # comment out #print out the charlst
         
            
            if charlst[0] > charlst[1]: # if the value in index 0 is greater then value in index 1
                bitslst.append(1) # add 1 to the bitlist
                charlst.clear() # clear the charlst
                self.seed =  self.seed + self.step # add the step to the seed
            else: # if the condition above is not met
                bitslst.append(0) # add 0 to the bitlist 
                charlst.clear() # clear the charlst
                self.seed =  self.seed + self.step # add the step to the seed
 
        #print("bitlst", bitslst) # comment out #print out the bitlist 

        if len(bitslst) == self.bits: # if the length of the list equals to 32 bits 
            tempbitlst = [] # a temporary list that will collect calculations
            for i in range(len(bitslst)): # go through the length of the list 
                num = bitslst[i] * (1/2)**(i+1) # calculate the bit number to produce a random num
                tempbitlst.append(num) # add the calculation in the bit number
            
            bitslst.clear() #clear the bit list
  
            self.sumbit = sum(tempbitlst) # add all the elements in the list together and assign to variable 
            tempbitlst.clear() # clear the temp list

        file.close()
        
        return self.sumbit # return a function that will generate a number
       
    def __repr__(self): # this function is a representation of the class
        'This function is will generate a printable representation. ' #docstring
        return "This will generate one random number which is", self.sumbit # return a print statment
    
    
def main(): # create main function 
    'This is the main functions that will execute the program.' #docstring
    seed = 4 # the input seed 
    finallst = [] # a final list to generate all the random numbers 
    y = 0 # initialize the counter for the while loop
    bitnum = 0 #create a single number 
 

    prng = WarAndPeacePseudoRandomNumberGenerator(seed) # call the class and assign to variable 
   
    while y < 10000: # run the program 10,000 times 
        bitnum = prng.random() # generate random number 
        finallst.append(bitnum) # add the calculated number to list
        y = y + 1 # counter 
    
    
    print(finallst) #printing out the total list 

    print("") #space
    print("Minimum: ", min(finallst)) #print out the minimum
    print("Maximum: ",max(finallst)) #print out the maximum
    print("Mean: ",statistics.mean(finallst)) # print out the mean of the list
          
main() # call main function

'''
when looping until around 514 times then 0.0 displays 
the mean is .5 




'''











