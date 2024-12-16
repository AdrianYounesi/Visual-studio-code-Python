
import random 
tal = random.randint(1,10)
print(f"FUSKARE! talet är {tal}")


print(f"x*6={tal*6}")
print("What is x")
ans =input()

if ans == tal:
    print("you have guessed right")

else:
    print("you have guessed wrong")


