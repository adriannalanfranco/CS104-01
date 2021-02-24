total = 0
average = 0
howMany = 0
howManyEntered=0

howMany = int(input("How many test scores would you like to enter: "))

while (howManyEntered < howMany):
    testscore=int(input("Enter test score: "))
    total= total+ testscore
    howManyEntered = howManyEntered + 1

average= total/ howMany

print("The average for the test scores you entered is: "+str (average))


