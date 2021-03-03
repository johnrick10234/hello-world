# John Rick Santillan ID# 1910045 Part C

from datetime import datetime
from datetime import date
x= date.today()
months = {"January":"1", 'February':'2','March':'3','April':'4','May':'5','June':'6', 'July':'7', 'August':'8','September':'9','October':'10','November':'11','December':'12'}

inputs = open("inputDates.txt","r")
outputs = open("parsedDates.txt",'w')
input_line = inputs.read().splitlines()
for i in input_line:

    user_input = i
    if user_input.find(' ') ==-1:
        continue
    var1 = user_input.split(' ')

    var2 = var1[0]
    if var1[1].find(',')==-1:
        continue

    var4 = var1[1][:-1]
    var5 = var1[2]

    if var2 in months:
        var6 = months.get(var2)+'/'+var4+'/'+var5

        var7 =datetime.strptime(var6,"%m/%d/%Y").date()
        if var7 < x:
            outputs.write(var6)
            outputs.write('\n')








