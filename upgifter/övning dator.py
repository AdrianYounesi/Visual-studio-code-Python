import random
P_lista =["PC1", "PC2", "PC3", "PC4", "PC5"]
print("computer " + P_lista[1])

service = ["PC6", "PC7", "PC8", "PC9", "PC10"]
problems = ["nätverkskort", "graffikkort", "överhetad", "Förstörd skärm", "överkörd"]

print(P_lista)
print(P_lista[3])
temp= P_lista.pop(3)
del P_lista[3]
print(P_lista)
print(temp)

print(service)
service.append(temp)
print(service)

temp(problems.pop(random))




#service.remove("PC7")
#service.pop(2)
#####
# temp= PC[0]
# PC.pop(0)
# ser.append(temp)

index = 0 #vilket problem har datorn

while(index < len(service)):
    print(f"{service[index]} has problem {problems[index]}")
    index +=1

for problem in problems:
    print("service " + problem)

print(f"{service[0]} has problem {problems[0]}")  #same as:print([0]) 

#a = 5 [P_lista]
#b = 5 [service]
#c = 10 [problems]


randomnummer= random.randint(5,5)
