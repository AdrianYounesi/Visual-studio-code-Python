import random

secret= random.randint(0,10) #hämligt tal
print(f"THE SECRET IS {secret}") # för att kunna testa
answer = input() #gissning
nummer= int(answer)# GÖR OM GISSNINGEN TILL ETT TAL

while(nummer != secret): #det här är gissningen, != inte lika med
    print("user guesses answer") #det här kommmer att först
    print("you guessed wrong") 
    print("try again")
    answer = input()
    nummer= int(answer)# GÖR OM GISSNINGEN TILL ETT TAL

 
print("you have guessed right")
