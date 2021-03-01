#John Rick Santillan            ID: 1910045

pw = input()
mp = ''

p=0
while p<len(pw):
    np = pw[p]
    if np == 'a':
        mp+= '@'
    elif np == 'i':
        mp+= '!'
    elif np == 'B':
        mp+= '8'
    elif np == 'm':
        mp+='M'
    elif np=='o':
        mp+='.'
    else:
        mp+=np
    p+=1
print(mp+str('q*s'))

