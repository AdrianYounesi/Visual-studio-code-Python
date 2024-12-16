import random
siffran =random.randint(1,10)
#print(f"Generar {siffran}")

print("MONI gissar siffran?")
ans = int(input())

if siffran == ans :
    print("MONI gissade rätt nummer")
    
else:
    print("MONI gissade fel nummer")

