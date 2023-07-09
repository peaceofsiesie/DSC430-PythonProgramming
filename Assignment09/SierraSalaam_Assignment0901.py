# Name: Sierra Salaam
# Date: March 06, 2023
# Assignment: 0901 - Numpy Intro 
# Video Links: https://youtu.be/hiD4sMe5qF0
# Honor Statement: "I have not given or receive any unauthorized 
# assistance on this assignment."


#1
import numpy as np #import the library


#2
a = np.arange(100) # create  a 1D array
print(a) # print array
print("") # print space

#3
b = np.arange(0, 100, 10) # creat 1 1D array that goes up to 100 and step by 10
print(b) # print array
print("") # print space

#4
c = np.linspace(0.0, 10.0)
print(c)  # print array
print("") # print space

#5
d = np.random.random((10,10))
print(d)  # print array
print("") # print space

#6
a = np.arange(100).reshape(10,10)
print(a)  # print array
print("") # print space


#7
print(a[4,5]) # print the spot within array
print("") # print space

#8
print(a[4]) # print the spot within array
print("") # print space

#9
print(np.sum(d)) # add up sum within array
print("") # print space

#10
print(np.max(a)) # find the max in array
print("") # print space

#11
print(np.transpose(b)) #transpose the array
print("") # print space

#12
print(np.multiply(a,d)) #multiply both arrays
print("") # print space

#14
print(np.dot(a,d)) # compute dot product within array
print("") # print space

print()
