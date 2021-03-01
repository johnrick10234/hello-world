# variable 1
a= int(input())
b= int(input())
c= int(input())
# variables 2
d= int(input())
e= int(input())
f= int(input())

solution=False
for x in range(-10,10):
    for y in range (-10,10):
        c = a * x + b * y
        f = d * x + e * y
        # if a * x + b * y == c and d * x + e * y == f:
        if c == f:
            print (x,y)
            solution=True
if not solution:
    print ("No Solution")

