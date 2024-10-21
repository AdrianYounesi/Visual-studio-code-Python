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