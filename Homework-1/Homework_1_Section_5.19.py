print("Davy's auto shop services")
print("Oil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")

first = input("Select first service:\n")
second = input("Select second service:\n")


def theCost(m):
    if m== "Oil change":
        return 35
    if m== "Tire rotation":
        return 19
    if m== "Car wash":
        return 7
    if m== "Car wax":
        return 12


print ("\nDavy's auto shop invoice\n")
uno = theCost(first)
dos = theCost(second)
tres = 0
if first == '-':
    print("Service 1: No service")
else:
    print("Service 1:",first+",","$"+str(uno))
if second == '-':
    print ("Service 2: No service")
else:
    print("Service 2:",second+",","$"+str(dos)+"\n")

if first == "-":
    print ("Total:","$"+str(tres+dos))
elif second == "-":
    print("\nTotal:", "$" + str(tres + uno))

else:
    print("Total:","$"+str(uno+dos))











