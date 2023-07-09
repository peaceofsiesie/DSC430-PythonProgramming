# Name: Sierra Salaam
# Date: January 30, 2023
# Assignment: 0402 - Human Pyramid
# Video Links: https://youtu.be/Osbl7xyMyac
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."


def userInput():
    '''This function will ask the user input of the row and column of pyramid''' #docstring

    try: # create a try block to test for input error 
        print("")
        row = int(input("Please choose a row number (whole numbers only) >  ")) # ask the user for row input and convert to int
        column = int(input("Please choose a column number (whole numbers only) > ")) # ask the user for column input and convert to int
    except ValueError: # when a vaildation error is produce
        print("Invaild Entry! Please enter a whole number and try again!") # print statement letting user know if is an error
        userInput() #call input function again
  
    return row, column # produce and save values of row and column


def humanPyramid(row, column): # a function that will determine the weight depending on position
    '''This function will execute the program to determine the weight depending on which position they are in the pyramid''' #docstring
    if row == 0: # if row is equal to 0
        return 0 # produce number 0 weight
    elif (column == 0): # if the column is equal to 0
        return ((humanPyramid(row-1, column) + 128)/2) # rerun the function but subtract a number from row
    elif (row == column): # if the column and row are equal 
        return ((humanPyramid(row -1, column - 1) + 128/2)) #rerun the function to subtract the row and column
    else: # if all the conditions above are not met
        return ((humanPyramid(row -1, column) + humanPyramid(row-1, column -1)+ 128)/2) # rerun funciton by adding both sides of the weight together for people in the middle 

def main():
    '''This function is the main function that will run the program''' #docstring
    row, column = userInput() # call function to allow the user to enter the row and column values 
    weight = humanPyramid(row, column) # call function to execute the caculation of weight of person and assign value
    print("\nThe total weight of what the person is holding is: ", weight) # print out the wieght
    print("\nThis Program Has Ended! Have A Great Day!") # let the user know the program has ended. 


main()  # call main function to execute program