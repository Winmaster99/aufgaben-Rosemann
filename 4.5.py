satz = input("Gebe einen Satz ein: ")

wort = input("Wonach soll gesucht werden?: ")

if wort in satz:
    print("Wahr")
else:
    print("Falsch")
