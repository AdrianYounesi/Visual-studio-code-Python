from os import remove
from typing import NoReturn

points = 0
player1 = "Jimmy"
player2 = "Anders"
player3 = "Jan"

#function for questions and answers
question1 = "what is the capital of France"
question2 = "What is the capital of Sweden"
question3 = "What is the capital of Norway"

#dictionary store answers answers
answers = {}

#loop trough each player and ask questions
print(question1)
ans1= input()
if (ans1 == "paris"):
    print("correct 3 points")
    points += 3
else:
    print("answer is not correct -3 points")
    points -= 3

print(question2)
ans2= input()
if (ans2 == "stockholm"):
    print("correct 3 points")
    points += 3
else:
    print("answer is not correct -3 points")
    points -=3

print(question3)
ans3= input()
if (ans3 == "oslo"):
    print("correct 3 points")
    points += 3
else:
    print("answer is not correct -3points")
    points -= 3

print(points)

   

