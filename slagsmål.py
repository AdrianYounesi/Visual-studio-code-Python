player1 = "robber"
player2 = "fighter"
hp1 = 100
hp2 = 100

print(player1, " has hp ", hp1)
hp1= hp1 -10

#print("robber or fighter gets hit")
print("robber gets hit")

print(player1, " has hp ", hp1)
print(player2, " has hp ", hp2)
hp2= hp2 -10

print("fighter gets hit")
print(player2, " has hp ", hp2)

hp2= hp2 -10

while(hp1 > 0 and hp2 > 0):
    print(player1, " has hp ", hp1)
    hp1= hp1 -10
    print(player1, " has hp ", hp1)
    print(player2, " has hp ", hp2)
    hp2= hp2 -10

    print("fighter gets hit")
    print(player2, " has hp ", hp2)

if(hp1 == 0):
    print("player2 has won")
else:
    print("player1 has won")

    

   

    
    



