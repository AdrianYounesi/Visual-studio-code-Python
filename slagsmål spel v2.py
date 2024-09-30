player1 = "ice" 
player2 = "fire"
hp1 = 100
hp2 =100
hit = 10

while(hp1 > 0 and hp2 > 0):
    print(player1,"has",hp1 ," hp")
    hp1 = hp1 - hit

    print(player2,"has",hp2 ," hp")
    hp2 = hp2 - hit

if(hp1 == 0 ):
    print("game over ice has won")

else:

    if(hp2 == 0):
        print("game over fire has won")

print(player1,"or", player2, "wants to fight again")
answer = input("should they fight yes or no ?")

if(answer == "yes"):
    
    player1 = "ice" 
    player2 = "fire"
    hp1 = 100
    hp2 =100
    hit = 10

    while(hp1 > 0 and hp2 > 0):
        print(player1,"has",hp1 ," hp")
        hp1 = hp1 - hit
   
        print(player2,"has",hp2 ," hp")
        hp2 = hp2 - hit

    if(hp1 == 0 ):
        print("game over ice has won")

    else:

        if(hp2 == 0):
            print("game over fire has won")



else:
    print("game over")