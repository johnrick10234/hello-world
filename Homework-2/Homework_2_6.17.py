#John Rick Santillan            ID: 1910045

pw = input()
mp = ''

p=0
while p<len(pw):
    np = pw[p]
    if np == 'a':
        mp+= '@'
    else:
        mp+=np
    p+=1
print(mp)

