# Name: Sierra Salaam
# Date: January 30, 2023
# Assignment: 0501 - Dice and Cups
# Video Links: https://youtu.be/Jn5XyDWmY7M
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."

import random # import random library to execute different methods 

class SixSideDie: # creating a parent class to roll a six sided die
    'A parent class that will roll and show face value of 6 sided die' #docstring

    def __init__(self, die): #creating initialize function class with self and one variable die
        'A method that will initialize all variable within the parent class SixSide Die and Child Class' #docstring
        self.die = die # assign die variable to initialize variable 


    def roll(self): # a method that will roll the die
        self.die = random.randint(1,6) # create a random number between 1-6 and assign it to die
        print(self.die) #print out the number 

    def getFaceValues(self): # a method that will display the die face value 
        'A methond that will print out die face value' #docstring
        print(self.die) #print out the die face value

    def __repr__(self): # a method that will print out the result of the die and repr
        'A method that will produce the results of the class' #docstring
        print(self.die) # print results of die


class TenSidedDie(SixSideDie): # create a child class to roll a ten sided die
    'A child class that will role and show face value of the 10 sided die' # docstring
        
    def roll(self): # a method that will roll a ten sided die 
        'A method that will roll a ten sided die and display the die value' #docstring
        self.die = random.randint(1,10) # generate random number between 1-10
        print(self.die) # print the results of the die

    def __repr__(self): # a method that will print out the result of the die and repr
        'A methond that will produce results of the class' #docstring
        print(self.die) # print the result of the die
 

class TwentySideDie(SixSideDie): # create a child class to roll a ten sided die
    'A child class that will role and show face value of the 20 sided die' # docstring
    def roll(self): # a method that will roll a twenty sided die
        self.die = random.randint(1,20)  # generate random number between 1-20
        print(self.die) # print out die results 

    def __repr__(self): # a method that will print out the result of the die and repr
        'A method that will produce the results of the class' #docstring
        print(self.die) # print results of die


class Cup: # a class that will produce the total sum in cup
    'A class that will gather all the die values and produce a total number sum in cup' # docstring


    def __init__(self, six = 0, ten = 0, twenty = 0):
        'A method that will initialize all arguments to produce total sum' #docstring
        self.six = six # value for the six die  
        self.ten = ten # value for the ten die 
        self.twenty = twenty # value for the twenty die

    
    def roll(self, cup): #
        "A method that will roll all die and calculate the total sum of each die in the cup" #docstring
        self.cup = cup # assign arg variable to self variable 
        self.cup = 0 # assign a value to self.cup variable 


        cup06 = cup10 = cup20 = 1 # assign all the variables to 1

        while cup06 <= self.six: # run until all the total numbers of six die are all counted for 
            i = random.randint(1,6) # create a random number to generate 
            self.cup =  self.cup + i # add a additonal count to the total amount in cup 
            cup06 += 1 # continue loop counter 
        
        
            
          
        while cup10 <= self.ten: # run until all the total numbers of six die are all counted for 
            j = random.randint(1,10) # create a random number to generate 
            self.cup = self.cup + j # add a additonal count to the total amount in cup 
            cup10 += 1 # continue loop counter

      
        while cup20 <= self.twenty:# run until all the total numbers of six die are all counted for
            k = random.randint(1,20) # create a random number to generate 
            self.cup = self.cup + k # add a additonal count to the total amount in cup
            cup20 += 1 # continue loop counter
            
        
        print(self.cup) # print the cup results 

        return self.cup # return the cup results 
       

    def getSum(self): # a method that will print the result of all the sum of the die
        'A method that will print the sum of all the die in the cup' #docstring
        print(self.cup) # print results
        return self.cup #return resutls 

    def __repr__(self): # a method that will  produce the results    
        ' A methond that will produce the results of the  ' #docstring           
        results = "The total amount of rolling Six Die: ", self.six, " Ten Die: ", self.ten, "and Twenty Die", self.twenty, "Which sums to - ", self.cup # assing 
        return results # return results 
    

#def main(): # the main function that will execute all called classes 
    #'A function that will call all classes and functions to run the code' # docstring
    #cup = Cup(1,2,1) # assign the class to a variable and pass different parameters 
    #cup.roll(cup) # call the roll method 
    #cup.getSum() # call the sum method 
   
    


#main() # calling the main function to run the code