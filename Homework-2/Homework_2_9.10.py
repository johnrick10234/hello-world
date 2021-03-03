import csv

input1 = input()
freq ={}
with open(input1,'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for word in row:
            if word not in freq.keys():
                freq[word] = 1
            else:
                freq[word] +=1

for key in freq.keys():
    print(key+' '+str(freq[key]))