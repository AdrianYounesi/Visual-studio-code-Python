P_lista =["PC1", "PC2", "PC3", "PC4", "PC5"]
print("computer " + P_lista[1])

service = ["PC6", "PC7", "PC8", "PC9", "PC10"]
problems = ["nätverkskort", "graffikkort", "överhetad", "Förstörd skärm", "överkörd"]
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