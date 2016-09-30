#
# PROMPT: Finding Your Future Savings.
# An investment firm wants you to develop a program for their website that will allow a customer to calculate how much they would have to deposit
# now it that wanted to accumulate a specific amount at the end of 10 years. Your job is to design and test the program for the firm.
#
# NOTES:
# formula: p = f / ( 1 + r ) ^ n
#          p = deposit today
#          f = desired future value
#          r = annual interest rate
#          n = number of years desired
#
# FLOWCHART:
# +---------------+
# | interest rate +------------------------+
# +---------------+                        |
#                                          |
# +---------------+                        |
# |amount of years+-----------------------------------+
# +---------------+                        |          |
#                                          |          |
# +---------------+                        |          |
# | desired total +-------+                |          |
# |  after years  |       |                |          |
# +---------------+       |                |          |
#                         |                |          |
#                         |                |          |
#                         v                v          v
# deposit needed = desired value ( 1 + interest ) ^ years
#       |
#       +--------------------+
#                            |
# +--------------------------v--------------------------+
# |                       output                        |
# +-----------------------------------------------------+
#

def getNumberInput(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            continue
def theActualCalculation(futureValue, interestRate, years):
    return futureValue/(1+(interestRate/100))**years

annualInterestRate = getNumberInput("What is the annual interest rate (%)? ")
totalYears = getNumberInput("How many years are you able to wait? ")
desiredValue = getNumberInput("How much money do you want after those " + str(totalYears) + " years at a " + str(annualInterestRate) + " interest rate? ")
print("To have $" + str(desiredValue) + " after " + str(totalYears) + " you would need to deposit " + str(theActualCalculation(desiredValue, annualInterestRate, totalYears)) + " today.")
