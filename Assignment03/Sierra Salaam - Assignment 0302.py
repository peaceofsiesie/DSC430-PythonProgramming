# Name: Sierra Salaam
# Date: January 23, 2023
# Assignment: 0302 - Happy Primes
# Video Links:  https://youtu.be/Be4dwIqWWs8
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."


def main(): # This function will call all the functions within the program 
    ''' This fucntion will execute all of the code within the program''' #docstring
    requestInput() # call function to request input
    checkPrimeNumber(number) # call function to check number is prime
    checkHappy(number) # call function to check if number is happy
    printResults(number) # call function to print results

def checkPrimeNumber(num): # function that will determine if number is prime
    ''' This function will check to see if the number is prime''' # docstring
    factorList = [] # create a list to input factors
    
    for factor in range(1,num+1): # run a for loop takes input number and check to see if number is consider as factor for num
        sumnum = num % factor # calculate module 
        if sumnum == 0: # if results are 0, it is considered as a factor 
            factorList.append(factor) # add factor number to list
        factor = factor + 1 # continue loop by adding 1
         
    if len(factorList) == 2: # if the length of the factor list is 2
        primenum = factorList[1] # assign index 1 as the prime number
        return True #results are True. The number is prime
    else: # if the condition above is not met
        return False #results are False. The number is not prime

def splitDights(num): # a function that will split the number into each dight and add each dight to the list
    ''' This function will split the numbers and add each digit to a list''' #docstring

    listDigits = [] # create a list save each digits

    num = str(num) # take the numbers and convert the number into a string

    for i in num: # create a loop that will view each element of the string
        i = int(i) # convert each digit into a integer
        listDigits.append(i) # add the integer to a list
    return listDigits # result of function is list

def calculateDigits(lst): # this function will calculate each digits within the list
    ''' This function will calculate the digits within the list ''' #docstring
    total = 0 #create a value for the total

    for i in range(0,len(lst)): # create a loop that will review the length of the list
        total = total + lst[i]**2 # calculate the digit by taking the power of the digit
    
    return total # result of the function is the total


def checkHappy(num): # a function that will determine if number is happy or sad
    '''This will determine if the number is considered Happy or Sad''' #docstring
    lstnum = [] # create a list 
    
    while True: # loop through the calculation until results are less then 10
        lstnum = splitDights(num) # Spliting the digit adding digits to the list
              
        num = calculateDigits(lstnum) # calculating the digits within the list and assign results into to varaiable 
                
        lstnum.clear()  # clear out the list       
        
        if num < 10: # if the variable is less then 10
            break # end the loop
    
    if num == 1: # if the variable equal 1 
        return True #then return true and considered as Happy
    return False # if the above condition is not met, then return false and considered as sad

def printResults(num): # a function that will print out results 
    '''This function will print results''' #docstring
    
    print("\nHere is the results to determine if " + str(num) + "\nis prime or non-prime and happy or sad.\n") #print statement to instruct user what is next

    if checkPrimeNumber(num) == True: # if function is true 
        numberPrime = "Prime" # then assign string as Prime
    else: # if the above condition is not executed 
        numberPrime = "Non Prime" # then assign string as Non Prime
        
    if checkHappy(num) == True: # if function is true
        numberHappy = "Happy" # then assign string as Happy
    else: # if the above condition is not executed 
        numberHappy = "Sad" # then assign string as Sad
        
    return print(numberHappy + " " + numberPrime + "\n\nThank you!\nThis program has now ended!\n\n") # print out the results of the program

def requestInput(): # a function will request the user to input a number to execute program
    '''This function will ask the user for an input of the number to execute rest of program''' #doctstring
    global number # creating a local variable 

    print("\nWelcome!\nWe are here to determine if a number is consider as\nHappy Prime, Happy Non-Prime, Sad Prime and Sad Non-Prime!\n") #print statement to let user know what the program is about to do

    while True: # create a loop that will ask the user for a number
        try: # 
            number = int(input("Please input any number > ")) # ask the user for an input
        except ValueError: # when the user enter a value that produces ValueError error
            print("Invaild Entry, Please enter a whole number.") # print the statement below
            continue # continue the loop until user enter the right information
        else: # if the except condition is not met then produce condition below
            break # end the loop
    return number #result will be in the number 

main() # call main function to execute program 