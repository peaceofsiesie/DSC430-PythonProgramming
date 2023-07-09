# Name: Sierra Salaam
# Date: Feburary 27, 2023
# Assignment: 0801 - Plot Generator and 0802 - Plot Viewer
# Video Links: https://youtu.be/oRi8uHH_Cds and https://youtu.be/u1YYXCeqItg
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."

import random #import random function

class SimplePlotGenerator: # creating a parent class to generate plot
    'This parent class will generate plot.' #docstring

    def __init__(self, plot_name = [], plot_adjectives = [], plot_profesions = [], plot_verbs = [], plot_adjectives_evil = [], plot_villian_job = [], plot_villains = []):
        'This method initialize all the variables within the class' #docstring
        self.plot_name = plot_name # initialize list for plot name
        self.plot_name = open("plot_names.txt", 'r').read().splitlines() # read file, split by each line and assingn the variable 

        self.plot_adjectives = plot_adjectives # initialize list for plot adjectives
        self.plot_adjectives = open("plot_adjectives.txt", 'r').read().splitlines() # read file, split by each line and assingn the variable 


        self.plot_profesions  = plot_profesions # initialize list for plot profesion
        self.plot_profesions = open("plot_profesions.txt", 'r').read().splitlines() # read file, split by each line and assingn the variable 


        self.plot_verbs  = plot_verbs # initialize list for plot verbs
        self.plot_verbs = open("plot_verbs.txt", 'r').read().splitlines() # read file, split by each line and assingn the variable 


        self.plot_adjectives_evil = plot_adjectives_evil # initialize list for plot adjective_evil
        self.plot_adjectives_evil = open("plot_adjectives_evil.txt", 'r').read().splitlines() # read file, split by each line and assingn the variable 


        self.plot_villian_job = plot_villian_job # initialize list for plot villian job
        self.plot_villian_job = open("plot_villian_job.txt", 'r').read().splitlines() # read file, split by each line and assingn the variable 


        self.plot_villains = plot_villains # initialize list for plot villains
        self.plot_villains = open("plot_villains.txt", 'r').read().splitlines() # read file, split by each line and assingn the variable 

        
    def registerPlotViewer(self, pv): # a methond that will register the plot viewer
        'This method will register the Plot Viewer Class' #docstring
        self.pv = pv # assign the input parameter to a variable 

    def generate(self): # method that will generate the action
        'This method will generate an action within the class' #docstring
        return 'Something Happens \n' # return a value of the class


class RandomPlotGenerator(SimplePlotGenerator): # this class will generate a random plot 
    'This class will generate a random plot and child of the Simple Plot Generator' #docstring
    def generate(self):
        'This methond will generate a random plot and produce results' #docstring
        name = random.choice(self.plot_name) # choose a random element in list and assign the variable 
        adjectives = random.choice(self.plot_adjectives) # choose a random element in list and assign the variable 
        profesions = random.choice(self.plot_profesions) # choose a random element in list and assign the variable 
        verbs = random.choice(self.plot_verbs) # choose a random element in list and assign the variable 
        adjectives_evil = random.choice(self.plot_adjectives_evil) # choose a random element in list and assign the variable 
        villian_job = random.choice(self.plot_villian_job) # choose a random element in list and assign the variable 
        villains = random.choice(self.plot_villains) # choose a random element in list and assign the variable 

        results = "\n" + name + ", a " + adjectives + profesions + " must " + verbs + " the " + adjectives_evil + villian_job + ", " + villains + "\n" # concatenate all variables until produce value
        
        return results # return value created within method

class InteractivePlotGenerator(SimplePlotGenerator): # this class will generate random options and have the user select the options
    'The class will generate random options the user can use and produce results' #docstring
  
    def generate(self): #this method will produce random choices and generate results based on user input
        'This method will generate the random choices and produce results based on user input ' #docstring

        name = random.choices(self.plot_name, k = 5) # choose 5 random values from the list
        #print(name)
        n = self.pv.queryUser("Which name would you like to select (please enter a whole number value between 0-4): \n" + ",  ".join(name) + " > ") # ask the user to select a whole number
        name_result = name[int(n)] # use a number to generate one of the results 

        adjectives = random.choices(self.plot_adjectives,  k = 5)  # choose 5 random values from the list
        n = self.pv.queryUser("Which adjectives would you like to select (please enter a whole number value between 0-4): \n" + ",  ".join(adjectives) + " > ") # ask the user to select a whole number
        adjectives_result = adjectives[int(n)] # use a number to generate one of the results 

        profesions = random.choices(self.plot_profesions,  k = 5)  # choose 5 random values from the list
        n = self.pv.queryUser("Which profesions would you like to select (please enter a whole number value between 0-4): \n" + ",  ".join(profesions) + " > ") # ask the user to select a whole number
        profesions_result = profesions[int(n)] # use a number to generate one of the results 


        verbs = random.choices(self.plot_verbs,  k = 5)  # choose 5 random values from the list
        n = self.pv.queryUser("Which verb would you like to select (please enter a whole number value between 0-4): \n" + ",  ".join(verbs) + " > ") # ask the user to select a whole number
        verbs_result = verbs[int(n)] # use a number to generate one of the results 


        adjectives_evil = random.choices(self.plot_adjectives_evil,  k = 5)  # choose 5 random values from the list
        n = self.pv.queryUser("Which adjective evil word would you like to select (please enter a whole number value between 0-4): \n" + ",  ".join(adjectives_evil) + " > ") # ask the user to select a whole number
        adjectives_evil_result = adjectives_evil[int(n)] # use a number to generate one of the results 


        villian_job = random.choices(self.plot_villian_job,  k = 5)  # choose 5 random values from the list
        n = self.pv.queryUser("Which villian job word would you like to select (please enter a whole number value between 0-4): \n" + ",  ".join(villian_job) + " > ") # ask the user to select a whole number
        villian_job_result =  villian_job[int(n)] # use a number to generate one of the results 


        villains = random.choices(self.plot_villains,  k = 5)  # choose 5 random values from the list
        n = self.pv.queryUser("Which villain would you like to select (please enter a whole number value between 0-4): \n" + ",  ".join(villains) + " > ") # ask the user to select a whole number
        villains_result = villains[int(n)] # use a number to generate one of the results 


        results = "\n" + name_result + ", a " + adjectives_result + " " + profesions_result + " must " + verbs_result + " the " + adjectives_evil_result + " " + villian_job_result + ", " + villains_result + "\n" # concatenate all variables until produce value
    
        return results # return value created within method
   

class PlotViewer: # this class will be the plot viewer 
    'This class is the Plot Viewer class' #docstring
    def registerPlotGenerator(self, pg): # methods that will register plot generator
        'This method will register the Plot Generator' #docstring
        self.pg = pg # assign parameter variable to the class
        self.pg.registerPlotViewer(self) # call the registerPlotViewer method and assign the variaable to itself

    def queryUser(self, str): # this method is used to query user to accept an input for the user
        'This method is used to to query user to accept an input from the user.' #docstring
        return input(str) # return the input string value 
    
    def generate(self): # this method will generate the plot from the class it has been assigned to
        'This method will generate the Plot from the class that is assigned' #docstring
        return self.pg.generate() # return the result from the generate method.



def main(): # This class will execute different class and methods in program
    'This is the main function that will execute program' #docstring

    pv = PlotViewer() # assign the Plot View class to a variable 

    print("Printing from Simple Plot Generator") # statment to let usser know which class
    pv.registerPlotGenerator(SimplePlotGenerator()) # call the registerPlotGenerator Function with the Parent class
    print(pv.generate()) #this will print the results to the generator function 

    print("Printing from Random Plot Generator") # statment to let usser know which class
    pv.registerPlotGenerator(RandomPlotGenerator())  # call the registerPlotGenerator Function with the Child class
    print(pv.generate()) #this will print the results to the generator function 

    print("Printing from Interactive Plot Generator") # statment to let usser know which class
    pv.registerPlotGenerator(InteractivePlotGenerator())  # call the registerPlotGenerator Function with the Child class
    print(pv.generate()) #this will print the results to the generator function 
    


main() # call class to execute program