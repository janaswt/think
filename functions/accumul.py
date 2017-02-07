def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x
    return runningtotal
toSquare = 9
squareResult = square(toSquare)
print("The result of", toSquare, "squared is", squareResult)
