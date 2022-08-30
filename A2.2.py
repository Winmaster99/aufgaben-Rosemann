a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))
c = int(input("Zahl 3: "))

if a > b or a > c:
    print(a)

elif b > a or b > c:
    print(b)

elif c > a or c > b:
    print(c)