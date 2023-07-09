# Name: Sierra Salaam
# Date: Feburary 13, 2023
# Assignment: 0601 - Palindrome Dates
# Video Links: https://youtu.be/trC31HnwZA8
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."

class listGenerator: # class that will generate a list depending on start range and end range 
    'Generates the list of values within range' #docstring
    def __init__(self, startnum, endnum, lst = []): # inizalized the varables 
        'Inizalized varables within function for range and list' #docstring
        self.startnum = startnum # start number 
        self.endnum = endnum # end number 
        self.lst = lst # create a value for list 

    def generateList(self): # method that will generate all the values in days, month and years list 
        'Generate the list of all the values for day, month and years.' #docstring
        for n in range(self.startnum,self.endnum): # review all elemnents between the range of start and end number
            if n < 10: # if the number is less then 10
                n = "0" + str(n) # add a 0 to the string and convert to string
            n = str(n) # convert into a string
            self.lst.append(n) # add the value to the list 
      
        return self.lst #save the list 

    def __repr__(self): # this method is repr of Palindrome Dates
        'Produce represenation of ListGenerator' #docstring
        return "This is to generate a lst depending on start number and end number for month, day and year"  # produce represenation of class
    

class DateGenerator:
    'Generate all the dates depending on arguments of days, months and years lists.' #docstring

    def __init__(self, dlst = [], mlst = [], ylst = [], dates = []): # inizalized the varables 
        'Inizalized varables within function for range and list'#docstring
        self.dlst = dlst # varable for the list for days
        self.mlst = mlst # varable for the list for month
        self.ylst = ylst # varable for the list for year
        self.dates = dates # varable for the list of dates 
        
            
    def generatelst(self): 
        'Generate all the dates in the correct order within format.' #docstring
        for y in self.ylst: # review all elements in the year list
            for d in self.dlst: # review all the elements in the day list
                for m in self.mlst: # review all the elements in the month list
                    
                    if int(d) > 29 and int(m) == 2: # if the date is greater then 29 in month of february 
                        pass # move on
                    else: # if condition is not met above 
                        date = str(d) + str(m) + str(y) # concat the string of date
                        self.dates.append(date) # add date to list 

                    if int(d) < 10: # if the day is less the 10
                        date2 = str(int(d)) + str(m) + str(y) # remove the 0 from the beginning of the date and convert back to string
                        self.dates.append(date2) # add date to list 

        return self.dates # save the dates 

    def __repr__(self): # this method is repr of Palindrome Dates
        'Produce represenation of DateGenerator' #docstring
        return "The outcome of the list is", self.dates  # produce represenation of class
                
class PalindromeDate: # a class that will produce palidrome dates 
    'Identify Palindrome Dates' #docstring
    
    def __init__(self, datelst = [], pdlst = []): # method that inizalize variables 
        'Inizalized varables within function for range and list.' #docstring
        self.datelst = datelst #  varable for all dates 
        self.pdlst = pdlst # varable for palindrome date
    
    def produceListofDates(self): # this method is for producing the palidrome dates 
        'Produce the palidrome dates. ' #docstring
        
        for d in self.datelst: # review each element in the list 
            flip = d[::-1] #file the string to print out opposite 
            
            if int(d) == int(flip): # if the value file equal each other 
                self.pdlst.append(d) # add the values ot the list
        
        return self.pdlst # save the list 
        
    def __repr__(self): # this method is repr of Palindrome Dates
        'Produce represenation of PalindromeDate Class.' #docstring
        return "The list of a palidrome dates is", self.pdlst  # produce represenation of class
    

class DateFormat: # this class with produce the correct format
    'Produce the correct format of each string.' #docstring

    def __init__(self, pdlst, outcomelst): # inizalized the varables 
        'Inizalized varables within function for the list format.' #docstring
        self.pdlst = pdlst # the list of palindrome date 
        self.outcomelst = outcomelst # the list of the format outcome

    def printFormat(self): # a method that will produce the list 
        'Produce each date in the right format' #docstring
        for pdl in self.pdlst: # review all the elements in the list
            if len(pdl) == 8: # if the string is 8
                pdl = pdl[0] + pdl[1] + "/" + pdl[2] + pdl[3] + "/" + pdl[4:] # create string in this format
                self.outcomelst.append(pdl) # add the format to the list 
            
            if len(pdl) == 7: # if the stirng is 7
                pdl = pdl[0] + "/" + pdl[1] + pdl[2] + "/" + pdl[3:] # create string in this format
                self.outcomelst.append(pdl) # add the format to the list 

        return self.outcomelst # save the list 

    def __repr__(self): # produce repr for the DateFormat 
        'Produce represenation of DateFormat class' #docstring
        return "The outcome of the list is", self.outcomelst # produce represenation of class


class File: # class createa file and produce results 
    'Produce a file and print results' # dopcstring

    def __init__(self, lst): # inizalized list 
        'Inizalized varables within function to create list' #docstring
        self.lst = lst # create a varaible called list 

    def writeOutcome(self): # a method that will produce outcome of list
        'Create a text file that will produce outcome of list' #docstring
        lengthlst = len(self.lst) # assign value to find length of list

        outfile = open('PalindromeDateOutcome.txt', 'w') # create a new file to print dates 
        outfile.write("List of All The Palindrome Dates :) \n ----------------------------\n") #print instruction to user

        for l in self.lst: # view each element of the list
            outfile.write(l +'\n') # print each element in the list 
        
        outfile.write("\nTotal length of the list is .... " + str(lengthlst)) # print the total number of on list
        outfile.close() # closing the file

        print(" ") # print statement of next line
        print("The Palindrome Date File has been created. Please Check your local Filepath.") # print state instructing user
        print(" ") # print statement of next line

    def __repr__(self): #produce repr of the File 
        'Produce represenation of File class' #docstring
        return "The results in the lst has been created in a text file"  # produce represenation of classe 


def main(): # the main function that executes the program
    'This fuction executes the program' #docstring

    days, months, years, dates, pdates, formatpdates = [], [], [], [], [], [] #declare all list used for program
    
    lstgen = listGenerator(1, 32, days) # Generate a list for the days
    lstgen.generateList() # produce list for days 

    lstgen = listGenerator(1, 13, months) # Generate a list for the months
    lstgen.generateList() # produce list for months
    
    lstgen = listGenerator(2001, 2101, years) # Generate a list for the years 
    lstgen.generateList() # produce list for years 

    dategen = DateGenerator(days, months, years, dates) # Generate a list of all the dates
    dategen.generatelst() # produce list for the dates

    paddate = PalindromeDate(dates, pdates) # Take all the dates and find which date is palindrome date
    paddate.produceListofDates() # produce the palindrome date 

    formlst = DateFormat(pdates, formatpdates) # Take all the palindrome date and format the dates
    formlst.printFormat() # produce the format for dates

    cpfile = File(formatpdates) # create a file and print all dates 
    cpfile.writeOutcome() # produce the file


main() #executing main function







    
              
            
      


      

 


