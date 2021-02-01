WH = int(input("Enter wall height (feet):\n"))
WW = int(input("Enter wall width (feet):\n"))
area = WH*WW
print("Wall area:",area,"square feet")

gal = float(area/350)
print("Paint needed:",'{:.2f} gallons'.format(gal))
print("Paint needed:",round(gal),"can(s)\n")

color = input('Choose a color to paint the wall:\n')
dict = {
    "red":35,
    "blue":25,
    "green":23
}
print('Cost of purchasing',color,'paint: $'+str(dict[color]))