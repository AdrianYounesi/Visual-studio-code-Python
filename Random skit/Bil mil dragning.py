mil2 = int(input("mätarinställning idag? "))
mil1 = int(input("mätarinställning för ett år sedan? "))
print("antal körda mil:", mil2 - mil1)
if(mil1>mil2):
    print("fel mätarinställning angiven")

else:
 liter = float(input("antal liter bensin? "))
print(f'förbruknining per mil: {liter/(mil2-mil1):.2f}')
 