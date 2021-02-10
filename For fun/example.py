print("Birthday Calculator")
print("\nCurrent day\n")

m1 = int(input("Month: "))
d1 = int(input("Day: "))
y1 = int(input("Year: "))

print("\nBirthday\n")
m2 = int(input("Month: "))
d2 = int(input("Day: "))
y2 = int(input("Year: "))

years = y1 - y2

if m2<m1:
    years-=1
elif m2 < m1 and d2 < d1:
    years-=1
elif m2 == m1 and d2 > d1:
    years
elif m2 == m1 and d2 < d1:
    years-=1

if (m1 == m2 and d1 == d2):
    print("\nHappy Birthday!")

print("You are",years,"years old.")