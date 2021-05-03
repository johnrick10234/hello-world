#John Rick Santilla #1910045

d = input().split()
n = d[0]
while n != '-1':
    try:
        a = int(d[1])+1
    except ValueError:
        a = 0
    print (n,a)

    d = input().split()
    n = d[0]