Lj=float(input("Enter amount of lemon juice (in cups):\n"))
Wc=float(input("Enter amount of water (in cups):\n"))
Nc=float(input("Enter amount of agave nectar (in cups):\n"))
Sc=float(input("How many servings does this make?\n"))

print("\nLemonade ingredients - yields", '{:.2f}'.format(Sc))
print('{:.2f}'.format(Lj), "cup(s) lemon juice")
print('{:.2f}'.format(Wc), "cup(s) water ")
print('{:.2f}'.format(Nc), "cup(s) agave nectar")

Serv=float(input("\nHow many servings would you like to make?\n"))
print("Lemonade ingreduents - yields", '{:.2f}'.format(Serv))
print('{:.2f}'.format(Lj*Serv/Sc), "cup(s) lemon juice")
print('{:.2f}'.format(Wc*Serv/Sc), "cup(s) water")
print('{:.2f}'.format(Nc*Serv/Sc), "cup(s) agave nectar")

VolLj=Lj*Serv/Sc
VolWc=Wc*Serv/Sc
VolNc=Nc*Serv/Sc

print("\nLemonade ingredients - yields",'{:.2f}'.format(Serv))
print('{:.2f}'.format((VolLj)/16), "gallon(s) lemon juice")
print('{:.2f}'.format((VolWc)/16), "gallon(s) water")
print('{:.2f}'.format((VolNc)/16), "gallon(s) agave nectar")







