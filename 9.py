import statistics

a = int(input("Anfang: "))
b = int(input("Ende: "))

liste = []

for i in range (a,b):
    liste.insert(0,i)


print(statistics.median(liste))