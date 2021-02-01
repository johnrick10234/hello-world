Lj=float(input("Enter amount of lemon juice (in cups):\n"))
Wc=float(input("Enter amount of water (in cups):\n"))
Nc=float(input("Enter amount of agave nectar (in cups):\n"))
Sc=float(input("How many servings does this make?"))
print("\n")
print("Lemonade ingredients - yields", '{:.2f}'.format(Sc),"servings")
print('{:.2f} cup(s) lemon juice'.format(Lj))
print('{:.2f} cup(s) water'.format(Wc))
print('{:.2f} cup(s) agave nectar'.format(Nc),"\n")

Serv=float(input("How many servings would you like to make?"))
print("\n")
print("Lemonade ingredients - yields", '{:.2f}'.format(Serv),"servings")
print('{:.2f} cup(s) lemon juice'.format(Lj*Serv/Sc))
print('{:.2f} cup(s) water'.format(Wc*Serv/Sc))
print('{:.2f} cup(s) agave nectar'.format(Nc*Serv/Sc))

VolLj=Lj*Serv/Sc
VolWc=Wc*Serv/Sc
VolNc=Nc*Serv/Sc

print("Lemonade ingredients - yields",'{:.2f}'.format(Serv),"servings\n")
print('{:.2f} gallon(s) lemon juice'.format((VolLj)/16))
print('{:.2f} gallon(s) water'.format((VolWc)/16))
print('{:.2f} gallon(s) agave nectar'.format((VolNc)/16))







