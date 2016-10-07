import datetime
print()

def numberCheck(x):
    try:
        int(x)
    except ValueError:
        pass

def test(given, iterations):
    start = int(datetime.datetime.now().strftime("%f"))
    print("Testing \"" + given + "\" with " + str(iterations) + " iterations")
    print("Start: " + str(start))
    for i in range(0, iterations):
        numberCheck(given)
    end = int(datetime.datetime.now().strftime("%f"))
    print("End: " + str(end))
    print("Total: " + str((end-start)/1000) + " milliseconds\n")

test("15", 10)
test("15a", 10)
test("15", 100000)
test("15a", 100000)