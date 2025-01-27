frukter = ["banan","melon","päron", "äpple", "mango"]
tvättmedel = ["vatten", "kolsyratvatten"]


x = frukter[0]
y = tvättmedel[0]

x = len(frukter)
y = len(tvättmedel)

for x in frukter:
    print(x)
for y in tvättmedel:
    print(y)


frukter.remove("melon")
frukter.append("honnungmelon")

print("pelle tvättar sin",[x], "med" ,[y], )

