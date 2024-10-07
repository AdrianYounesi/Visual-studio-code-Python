player1 = "ice" 
player2 = "fire"
hp1 = 100
hp2 =100
hit = 10
hitcombo = 0         #"x amount of hit on player1 or player 2"
counter = 0          #"amount of fighs"

while counter < 3: 

    counter +=1 
    while(hp1 > 0 and hp2 > 0):
        hitcombo +=1
        print(player1,"has",hp1 ," hp")
        hp1 = hp1 - hit

        hitcombo +=1
        print(player2,"has",hp2 ," hp")
        hp2 = hp2 - hit
        
    if(hp1 == 0 ):
        print("game over ice has won")
        print("ice has hit the other player 10 times")

    else:

        if(hp2 == 0):
            print("game over fire has won")
            print("ice has hit the other player 10 times")

    print(player1,"or", player2, "wants to fight again")
    answer = input("should they fight yes or no ?")

    if(answer == "yes"):
        
        player1 = "ice" 
        player2 = "fire"
        hp1 = 100
        hp2 =100
        hit = 10

        while(hp1 > 0 and hp2 > 0):
            hitcombo +=1
            print(player1,"has",hp1 ," hp")
            hp1 = hp1 - hit
    
            hitcombo +=1
            print(player2,"has",hp2 ," hp")
            hp2 = hp2 - hit

        if(hp1 == 0 ):
            print("game over ice has won")
            print("ice has hit the other player 10 times")


        else:

            if(hp2 == 0):
                print("game over fire has won")
                print("ice has hit the other player 10 times")

    else:
        print("game over")

print("the fighting game is done")