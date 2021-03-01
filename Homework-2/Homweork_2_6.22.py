a= int(input())
b= int(input())
c= int(input())
# variables
d= int(input())
e= int(input())
f= int(input())

for x in range(-10,11):
    for y in range (-10,11):
        if a * x + b * y == c and d * x + e * y == f:
            print (x,y)
        else:
            print ('No solution')
# this solution is not right