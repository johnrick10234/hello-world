# John Rick Santillan ID# 1910045 Part A

from datetime import datetime
from datetime import date
x= date.today()
months = {"January":"1", 'February':'2','March':'3','April':'4','May':'5','June':'6', 'July':'7', 'August':'8','September':'9','October':'10','November':'11','December':'12'}

user_input = input()
if user_input.find(' ') !=1:
    exit()
var1 = user_input.split(' ')

var2 = var1[0]

# var3 = var1[1].split(',')
var4 = var1[1][:-1]
var5 = var1[2]
print(var1)
print(var4)
if var2 in months:
    var6 = months.get(var2)+'/'+var4+'/'+var5

    var7 =datetime.strptime(var6,"%m/%d/%Y").date()
    if var7 < x:
        print(var6)











