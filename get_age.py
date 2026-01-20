import random

def getUserAge():
    guessedRight = False
    guessedAges = [0]
    randomNum = 0

    print("Hello, I am going to try and guess your age.")

    userName = input("What is your name (first name, last name): ")

    while guessedRight != True:

        while randomNum in guessedAges:
            randomNum = random.randint(15, 30)
        guessedAges.append(randomNum)

        askUser = input("Are you " + str(randomNum) + " years old? (y/n): ")
        
        if askUser == "y":
            print(str(userName) + " is " + str(randomNum) + " years old.")
            guessedRight = True
        else:
            print("Rats!")

getUserAge()