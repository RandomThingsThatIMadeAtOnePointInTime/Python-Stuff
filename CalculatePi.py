def calcPi(n):
    pi, numerator = 0, 4.0
    for i in range(n):
        denominator = (2 * i + 1)
        term = numerator / denominator
        if i % 2:
            pi -= term
        else:
            pi += term
        if i % 1000 == 0: print(str(i) + "/" + str(n) + "=" + str(i/n))
    return pi

print(calcPi(int(input("How many terms? "))))
