import random
##
#välja ett tal

correctNumber = random.randint(0,9)
numberOFGuesses = 3

#be om en siffra

while(numberOFGuesses > 0):
    print("guess a number")
    guess=int(input())
    #print("you guessed ")
    #print(guess)


    numberOFGuesses -=1
    #kolla om siffran om är större

    if(guess> correctNumber):
        print("you guessed to large. try again ")
    #, mindre eller lika 
    elif(guess < correctNumber):
        print("you guessed to small. try again ")
    else:
        print("you guessed corect ")
        numberOFGuesses = 0

#göra tre gånger  

# Program to generate a random number between 0 and 9

# importing the random module


