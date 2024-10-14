#a_list = ["liv", "Mohammed", "Henrik", "Mikael", "Karim", "Johan"]
#print("Hello"  +  a_list[2])

names = ["Eric", "Yunus", "Lianm", "Max", "Adrian", "Miranda"]
colours =["purple", "red", "blue", "green", "orange", "blue"]

index = 0 #where we begin

##
#while (index < len(names)):
#    print("{names[0]} has favourite colour {colours[index]}")
#    index +=1

for name in names:
    print("hello " + name)

print(f"{names[0]} has favourite colour {colours[0]}")  #same as:print(names[0])
