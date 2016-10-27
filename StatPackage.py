# http://www.public.asu.edu/~atrow/ser101/assignments/16Fall/lab5.html

import math # math.sqrt(x)
import random # random number generation for sample input

values = [] # our list containing all of our inputted floats

# allow the user to generate 499 random inputs to simulate a large input set without having to enter every number
# 499 instead of 500 because it allows the user to enter the 500th number, makes them feel special on the inside
if str.startswith(str.lower(input("Populate values with 499 random values? (y/n) ")), "y"):
    for x in range(0, 499): values.append(float(random.randint(0, 100)))

values = sorted(values) # sort the list from least to greatest

while len(values) < 500: # only accept numbers until our maximum of 500 is hit
    newValue = input("Value " + str(len(values) + 1) + ": ") # ask for next input value giving it's to-be count
    if newValue == "": # user gave a blank input; they want to stop inputting numbers
        if len(values) == 0:
            print("You need to give at least one input")
            continue
        else:
            print("Ending input with " + str(len(values)) + " total values")
            break

    try:
        # try to append given value as a float to the values list, if it's not a float then except & continue
        values.append(float(newValue))
    except ValueError:
        print(newValue + " is not a valid number")
        continue
if (len(values)) == 500: print("Value input limit exceeded [" + str(len(values)) + " total], ending input") # maximum of 500 values because prompt says so
print() # extra line to look nicer

neaterNumbers = []
for x in values: neaterNumbers.append(str("%.2f" % x)) # generate a string array containing all the numbers to two decimal places because the prompt wants that
print("For numbers [" + str(len(values)) + "]: " + ", ".join(neaterNumbers))

mean = sum(values) # add up all numbers in list array
mean /= len(values) # divide sum of all numbers by amount of numbers to get average
print("Mean: " + str("%.2f" % mean))

middleIndex = int(values[len(values) // 2]) - 1 # get middle index by getting amount of items divided by two
median = values[middleIndex] # get that middle number from middle index
if len(values) % 2 == 0: # even number, need to do some extra math because our middleIndex is actually the whole number after our middle point
    median = ((values[middleIndex - 1] + median) / 2.0) # average current median with index - 1
print("Median: " + str("%.2f" % median))

variance = 0 # initial value
for x in values: variance += (mean - x) ** 2 # for every value add the square and stuff
variance /= len(values) # divide by amount of numbers that we added before
print("Variance: " + str("%.2f" % variance))

print("Standard Deviation: " + str("%.2f" % math.sqrt(variance))) # print the square root of the variance [standard deviation] to two decimal places
