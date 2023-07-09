# Name: Sierra Salaam
# Date: January 30, 2023
# Assignment: 0502 - Cups and Dice
# Video Links: https://youtu.be/zk79ovpn4Ks
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."

import SierraSalaam_Assignment0501 #import class from previous assignment 
import random # import random library for random 
import sys # import sys for exit 

class Greeting: # A class that will gree the user and ask for user name
    'This class will greet user and ask the user for a name' #docstring
    
    def __init__(self, name = "Unknown"):  # a method initialize all arguments in class
        'A method that will initialize all variable within Greeting class' #docstring
        self.name = name # assign name to class variable self.name


    def setName(self): # A methond that will gree the user and ask for user name 
        'A method that will ask the player for name and save results' #docstring
        print("Welcome to Cups and Dice Game!") #print statement 
        self.name = str(input("We would love to know your name. Please enter you name. > ")) # ask user for input 
        return self.name # save results 

    def __repr__(self): # a method that will prodice results of the class
        'A method that will produce results of the class' #docstring
        return "Hello ", self.name, "! We are glad to have your here. Let's Play!" # save results of the class 

class Balance:
    'This class is a parent class that will produce a number and set the number as the balance' #docstring

    def __init__(self, number = 100):  # a method initialize all arguments
        'A method that will initialize all variable within Balance class' #docstring
        self.number = number # assign argument that is passing through to class name

    def setNumber(self): # a method that will set the balance number 
        'A methond that will produce the balance number' #docstring
        return self.number # save the balance number 

    def __repr__(self):  # a method that will produce results for the class
        'A method that will produce results of the class' #docstring
        return "Here is your current account balance: ", self.number # save the number for the goal

class Goal(Balance):  # this child class will set the goal number for the game
    'This is a child class and will set the goal number for the game' #docstring
    
    def setNumber(self): # a method that will set the goal number 
        'A methond that will produce the goal number' #docstring
        self.number = random.randint(1,100) # create the goal number and save in variable 
        return self.number # save the number for the goal 

    def __repr__(self):  # a method that will produce results for the class
        'A method that will produce results of the class' #docstring
        return "Here is the goal number", self.number # save results within class

class Sacrifice(Balance): # this child class will set the bet number for the game
    'This is a child class and will set the bet number for the game' #docstring
    
    def setNumber(self):
        'A methond that will produce the sacrifice number' #docstring
        try:
            self.number = int(input("What would you like to sacrifice? > ")) # ask user for input to recieve bet number 
            self.number = abs(self.number) # turn number into absolute value 
            return self.number #return number in method 
        except ValueError: # if user enter the wrong value 
            print("Invaild Entry, Please try again!") #print message 
            Sacrifice.setNumber(self) # call method again to ask question again

    def __repr__(self): # a method that will produce results for the class
        'A method that will produce results of the class' #docstring
        return "Here is the amount you are willing to sacrifice", self.number # save results within class

class Game: # This class will ask the user for an input and produce results of the cup game
    'This is a game class that will produce ask user for input and proceed to play the cup game' #docstring
    def __init__(self, number = 0, sixdie = 0, tendie = 0, twentydie = 0):  # a method initialize all arguments
        'A method that will initialize all variable within Game class' #docstring
        self.number = number # assign number to class number 
        self.sixdie = sixdie # assign six die value to class six die value 
        self.tendie = tendie # assign ten die value to class six die value
        self.twentydie = twentydie # assign twenty die value to class six die value
        

    def userGame(self): # a method that will ask user for input, run the cups game and produce results 
        "A method that will aks user for input and produce results of cups game" #docstring
        try: # attempt to get right input from user 
            self.sixdie = int(input("How many time will you like to roll the six die? > ")) #ask user for # of times six die will be rolled 
            self.tendie = int(input("How many time will you like to roll the ten die? > ")) #ask user for # of times ten die will be rolled 
            self.twentydie = int(input("How many time will you like to roll the twenty die? > ")) #ask user for # of times twenty die will be rolled 
        except ValueError: # catch Value Error when raised from input above 
            print("Invaid Entry. Please try again!") # print message to user 
            Game.userInput() # call user input function again so user can enter right information

        cupGame = SierraSalaam_Assignment0501.Cup(self.sixdie, self.tendie, self.twentydie) #assign variable to import class 
        self.number = cupGame.roll(cupGame) # call method from import class and assign to value for results of game
        
        return self.number # returning total value of cup game 

    def __repr__(self): # a method that will produce the results of class
        'A method that will produce results of the class' #docstring
        return "Here is the total number in the cup - ", self.number # produce results of the Game class 
    

class Calculation: # a class that will calculate and produce results

    'This is a class that will calculate all the values and produce the player a result' #docstring

    def __init__(self, number = 0, name = Greeting(), balance = Balance(), goal = Goal(), sacrifice = Sacrifice(), game = Game()): # a method initialize all arguments 
        "A method that initialize all the arguments to produce final balance" #docstring
        self.number = number # create value that will produce the difference number 
        self.name = name.setName() # create value that will get the name from the greeting class
        self.balance = balance.setNumber() # create value that will will get the balance from the balance class
        self.goal = goal.setNumber() # create value that will get the goal number from the goal class
        self.sacrifice = sacrifice.setNumber() # create value that will get the sacrifice number from the sacrifice class
        self.game = game.userGame() # create value that will get the game results from the game class 


    def CalculateResults(self): # a method that will calculate balnce and print results 
        'A methond that will calculate the total balance based on the game results' #docstring
        print("Beginning Account Balance -  ", self.balance) # print results of balance
        print("Goal Number -  ", self.goal) # print results of goal
        print("Sacrifice Number - ",self.sacrifice) # print results of bet number 
        print("Roll Die Sum Result -  ",self.game) # print results of die game

        self.number = self.goal - self.game # calculate the differnce between goal and actually results 
        self.number = abs(self.number) # make the difference number absoulte 

        print("Total Difference Between Goal and Roll Die Sum Result - ", self.number) # print the results 

        if self.number == 0: # if difference is 0
           self.balance = (self.sacrifice * 10) +  self.balance # add 10X to the account balance 
        elif self.number <= 3 and self.number >= 1:  # if the difference is between 1-3
            self.balance = (self.sacrifice * 5) +  self.balance # add 5X to the account balance 
        elif self.number <= 10 and self.number >=4: # if the difference is between 4-10
            self.balance = (self.sacrifice * 2) +  self.balance # add 2X to the account balance 
        else: # if all the conditons are not met
            self.balance = self.balance - self.sacrifice # deduct all the points bet in balance 

        print(self.name, "!\nYour final balance of this game is", self.balance) #print the results 

        return self.balance # save the balance 


    def __repr__(self): # a method that will produce results of class
        'A method that will produce results of the class' #docstring
        return "Your current balance is", self.balance # saving the results of class


def main(): # this function will run function nessecary to execute program  

    'This is the main function which will execute all the Class and methods' #docstring

    calculate = Calculation() # assign class to variable 
    calculate.CalculateResults() # run the calculate result method

    try: # try statement to answer if user wants to play again 
        print("Please type True for Yes and False for No.") # instruction statement 
        switchGame = eval(input("Would you like to play again? > ")) # assign value to variable 
    except ValueError: # except sttatment to answer if the user as invaild entry 
        sys.exit("Invaild, entry! We are not ending the game! Have A Good Day!") # automatically exit out the game

    if switchGame == True: #if user answer true 
        main() # call the main function again to execute program
    else: # if condition is not met above 
        sys.exit("Thank you for playing, we hope you have a wonderful day") # exit the game and produce message 

    


## Testing Classes and Methods

    #greet = Greeting()
    #greet.setName()

    #balance = Balance()
    #print("Balance Class - ", balance.number)
    
    #goal = Goal()
    #goal.setNumber()
    #print("Goal Class - ",goal.number)

    #sacrifice = Sacrifice()
    #sacrifice.setNumber()
    #print("Sacrifice Class - ",sacrifice.number)

    #game = Game()
    #game.userGame()
    #print("Game Class - ",game.number)


 

main() #running main function