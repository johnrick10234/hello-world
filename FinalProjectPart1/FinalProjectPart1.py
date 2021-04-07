#John Rick Santillan        #1910045
import csv
from operator import itemgetter
from datetime import date, datetime

mfl=[]
prl=[]
sdl=[]

with open('ManufacturerList.csv') as manlist:
    ml=csv.reader(manlist)
    for line in ml:
        mfl.append(line)

with open('PriceList.csv') as pricelist:
    pl = csv.reader(pricelist)
    for line in pl:
        prl.append(line)

with open("ServiceDatesList.csv") as sdlist:
    sl = csv.reader(sdlist)
    for line in sl:
        sdl.append(line)

new_mfl=(sorted(mfl, key=itemgetter(0)))
new_prl=(sorted(prl, key=itemgetter(0)))
new_sdl=(sorted(sdl, key=itemgetter(0)))

for x in range (0,len(new_mfl)):
    new_mfl[x].insert(3,new_prl[x][1])

for x in range(0,len(new_mfl)):
    new_mfl[x].insert(4,new_sdl[x][1])
final_list = new_mfl
full_inventory = (sorted(final_list, key=itemgetter(1)))

with open ('FullInventory.csv','w') as f:
    asd = csv.writer(f)

    for i in range(0,len(full_inventory)):
        asd.writerow(full_inventory[i])

with open('LaptopInventory.csv','w') as f:
    lf = csv.writer(f)

    for item in (final_list):
        if item[2] == 'laptop':
            lf.writerow(item)

with open('PhoneInventory.csv','w') as f:
    PI = csv.writer(f)

    for item in (final_list):
        if item[2] == 'phone':
            PI.writerow(item)

with open('TowerInventory.csv','w') as f:
    TI =csv.writer(f)

    for item in (final_list):
        if item[2] == 'tower':
            TI.writerow(item)

today = date.today()
current_date = today.strftime('%m/%d/%Y')
curr = datetime.strptime(current_date,'%m/%d/%Y')

final_list_past = sorted(final_list, key=lambda row: datetime.strptime(row[4],'%m/%d/%Y'))

with open ('PastServiceDateInventory.csv','w') as f:
    pastDate = csv.writer(f)

    for item in (final_list_past):
        item_date = datetime.strptime(item[4],'%m/%d/%Y')
        if (item_date) < curr:
            pastDate.writerow(item)

final_list_damage = sorted(final_list, key=lambda x: int(x[3]),reverse=True)
with open('DamagedInventory.csv','w') as f:
    item_dmg = csv.writer(f)

    for item in(final_list_damage):
        if item[5] == 'damaged':
            item_dmg.writerow(item)


