my_list = input().split()
ans=[]
for n in my_list:
    n = int(n)
    if n >=0:
        ans.append(n)
ans.sort()
for n in ans:
    print(n,end=' ')

