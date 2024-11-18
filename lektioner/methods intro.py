def kollaSax():
    motstandare= random.choice(ssp)
    print(f"din motståndare valde {motstandare}")
    if motstandare== "sax":
        print("oavgjort")
    elif motstandare == "sten" :
        print("du har förlorat")
    else:
        print("du har vunnit!")        
        
def kollaPase():
    motstandare= random.choice(ssp)
    print(f"din motståndare valde {motstandare}")
    if motstandare== "påse":
        print("oavgjort")
    elif motstandare == "sax" :
        print("du har förlorat")
    else:
        print("du har vunnit!")
    
def kollaSten():
    motstandare= random.choice(ssp)
    print(f"din motståndare valde {motstandare}")
    if motstandare== "sten":
        print("oavgjort")
    elif motstandare == "påse" :
        print("du har förlorat")
    else:
        print("du har vunnit!")        
    print(val)


import random
val= input("sten, sax, påse?")
ssp=["sten","sax","påse"]
if val == "sax":
    kollaSax()
if val == "påse":
    kollaPase()
if val == "sten":
    kollaSten()