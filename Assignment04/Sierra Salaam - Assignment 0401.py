# Name: Sierra Salaam
# Date: January 30, 2023
# Assignment: 0401 - Goldbach Deuce
# Video Links: https://youtu.be/kkjApm4sKuc
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."

import random
import sys

def printIntro(): # a function that will print out an introduction of what the program is attempting to do 
    '''This function will print the at the beginning of the program''' #docstring
    
    print('''Hello!\nWe are now going to test Goldbach's Deuce.
    First, we would need you to provide us the amount of number you would like for us to randomized between 0 - 100.
    Then we would need you to provide us the a number, which we will determine what two number (from the randomized list) equal the sum of the number.''') # print statement of instructions

  
def userInput(): # a function that will ask the user for an input
    '''This function will print the at the beginning of the program''' #docstring
    
    randomNumListLength = None # creating value for the length of the list

    try: # create a try block to test for input error 

        randomNumListLength = round(float(input("How many random numbers would you like to generate?\n(Remember: The random numbers will generate 0 - 100) >   "))) #ask user for input of length
        sumnum = round(float(input("What number would you like to find two pairs that sums up? > "))) #ask user for input of sum
    except ValueError: # when a vaildation error is produce
        print("Invaild Entry! Please enter a whole number and try again!") # print statement letting user know if is an error
        userInput() #call input function again

    return randomNumListLength, sumnum # produce and save results of inputs

def ListofRandomNums(num, lst, count): # a function that will produce the list and randomize reach number from 1-100

    '''This function will produce a list of random numbers and each element in the list will have a number ranging 1 - 100''' #docstring

    if count == num: #if the count is equal to the total number of the list
        return lst # produce the full list
    elif count < num: # if the previous condition is not met and if count is less then tota number of the list
        value =  random.randint(0,100) # create a value that is a random number between 1-100
        lst.append(value) # add the number to the list
        return ListofRandomNums(num, lst, count + 1) # reproduce the function but increase the count by 1

def ListShortener(num, first, last, lst, count): # a function that will shorten the list depending on the sum number
    '''This function will shorten the list depending on the sum number ''' #docstring

    lst = sorted(lst) # sort the list 

    if lst == []: # if the list is empty
        return print("Sorry, there are no values in the list to compare!") # let the user know the list is empty 
    elif lst[last] == num: # if the last item value in the list is equal to the sum number 
        return lst # save and produce the list
    elif lst[last] > num: # if the last number is greater then sum number
        del lst[last:] #remove the last item value and the other values following after the index
        return ListShortener(num, 0, len(lst) - 1, lst, count + 1) #repeat the function again by counting up 
    else: # if all the conditions above is not met
        return lst # save and produce list



def goldDeuces(first, last, lst, sum): # This function calculates the Gold Deuces to determine two number that produce sum number

    '''This function calculates the Gold Deuces and determine which two number in the list produce the sum number'''#docstring

    if first == last: # if the last index and the first index equal each other
        return print("\nThis is the end of the program! We hope you have a great day!") # let the user know the calculation has ended
    elif lst[last] < lst[first]: # if the last index is less then the first index
        return print("\nThis is the end of the program! We hope you have a great day!") # let the user know the calculation has ended
    elif lst[first] == lst[first + 1]: # if the first index equals the index next to the first index
        return goldDeuces(first + 1, last, lst, sum) # call the function but go to the next index to the right
    elif lst[last] == lst[last - 1]: # if the last index is equal to the index next to the last index
        return goldDeuces(first, last - 1, lst, sum)  # call teh function but go to the next index to the left
    

    if lst[first] + lst[last] == sum: # if the first index and the last index equal sum
        print(lst[first], "+", lst[last], "=", sum) # show the user the values
        return goldDeuces(first + 1,last - 1, lst, sum) # recall the function and go to the next index by calculating first and last
    elif lst[first] + lst[last] < sum: # if the first index and last index is less then the sum
        return goldDeuces(first + 1, last, lst, sum) # recall the function but go to the next first index to the right 
    elif lst[first] + lst[last] > sum: # if the first index and last index is grater then the sum
        return goldDeuces(first, last - 1, lst, sum) # recall the function but go to the next last index to the left


  
def main(): # a function that calls the other functions within the program
    '''This function calls all the other functions within the program''' #doc string
    
    randomNumList = [] # declare list of numbers 
    
    printIntro() # call function that will print intro
    
    randomNumListLength , sumnum = userInput() # call input function and return two variables 
    
    randomNumList = ListofRandomNums(randomNumListLength, randomNumList, 0) # call function to create the list and add value 
    print("Now Printing full list\n", randomNumList, "\n") # print the list to show the user
    
    randomNumList = ListShortener(sumnum, 0, len(randomNumList) - 1, randomNumList, 0) # call function to shorten list and assign short list back to list variable
    print("print list sorted and shortener\n", randomNumList, "\n") # print instruction what happen to the list
    
    print("Now it is time to determine which two numbers can sum up to", sumnum, "\n") # print additional instructions for the user
    if randomNumList == None: # if list does not have anything inside of it
        return "This is the end of the program! We hope you have a great day!" # let the user know the program has ended 
    else: #if conditions above is not true
        goldDeuces(0, len(randomNumList) - 1, randomNumList, sumnum) # call function to calculate all the values in the list to produce the sum number

        

      

main() # call main function to execute program



