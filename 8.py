import random

liste =[]

for i in range(6):
    Zahlen = round(random.uniform(1,50))
    liste.insert(0, Zahlen)

print(liste)
