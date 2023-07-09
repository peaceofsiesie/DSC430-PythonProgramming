# Name: Sierra Salaam
# Date: January 23, 2023
# Assignment: 0301 - Goldbach's Conjecture
# Video Links:  https://youtu.be/i3xJKI1G3no
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."


primeList = [] # creating a list 
number = 100 # creating a varaible that equals maximum number 

def main(): # a function that calls the other functions within the program
    '''This function calls all the other functions within the program''' #doc string
    printIntro(number) # call function that will print intro
    findPrimeNumbers(number) #call function that will find prime number 
    printGoldConjecture(number, primeList) # call function that will test and print Gold Conjecture 


def findPrimeNumbers(num): # a function that will find all the prime numbers within range 1 - number
    ''' This function that will find all the prime numbers within range 1 - the number that is declared''' #docstring
    list_factors = [] # a list to capture all the factors 

    for i in range(1,num+1): # create a loop that will go through the range of numbers 
        for factor in range(1,num+1): # run a for loop takes input number and check to see if number is consider as factor for number
            num_a = i % factor # calculate module 
            if num_a == 0: # if results are 0, it is considered as a factor 
                list_factors.append(factor) # add factor number to list
        i + i + 1 # increase count into loop

        if len(list_factors) == 2: # if the length of the list equals 2
            primenum = list_factors[1] # make first index value equal as a prime number
            primeList.append(primenum) # add the prime number to the prime list
  
        list_factors.clear() # clear the factor list
    return primeList # the results is the total prime list 


def printGoldConjecture(num, lst): # a function that will test and print the Gold Conjecture 
    ''' This function will test and print out the Gold Conjecture number theory''' #docstring
    
    print("These are all prime numbers ranging 1 - " + str(num) + ".\n") # print a statement to let user know we are printing prime list
    print(primeList) # print the prime list
    print("\nThese are all the prime numbers that sums up to an even number") # print a statment to let user know we are printing the sum of two prime numbers 
    

    for i in lst: # create a loop that will view every value in the list
        print(" ")
        for j in lst: # create a loop that will view every value in the list
            sumnum = i + j # add both of the values together 
            if sumnum % 2 == 0: #if the sum of both values are divisible by 2
                print(str(i) + " + " + str(j) + " = " + str(sumnum)) # then print i + j = sumnum

def printIntro(num): # a function that will print out an introduction of what the program is attempting to do 
    '''This function will print the at the beginning of the program''' #docstring
    print("Hello!\nWe are now going to test Goldbach's Conjecture.\nWe will now find the prime number between the range of 1- " + str(num) + ".\n") # print statement of instructions
    
    

main() # call main function to execute program
