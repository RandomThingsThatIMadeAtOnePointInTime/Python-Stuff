# http://www.public.asu.edu/~atrow/ser101/assignments/16Fall/lab5.html

import math
import random

values = []

if str.startswith(str.lower(input("Populate values with 499 random values? (y/n) ")), "y"):
    for x in range(0, 499): values.append(float(random.randint(0, 100)))

values = sorted(values)

while len(values) < 500:
    newValue = input("Value " + str(len(values) + 1) + ": ")
    if newValue == "":
        if len(values) == 0:
            print("You need to give at least one input")
            continue
        else:
            print("Ending input with " + str(len(values)) + " total values")
            break

    try:
        values.append(float(newValue))
    except ValueError:
        print(newValue + " is not a valid number")
        continue
if (len(values)) == 500: print("Value input limit exceeded [" + str(len(values)) + " total], ending input")
print()

neaterNumbers = []
for x in values: neaterNumbers.append(str("%.2f" % x))
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

print("Standard Deviation: " + str("%.2f" % math.sqrt(variance)))
