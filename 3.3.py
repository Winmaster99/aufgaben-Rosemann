MAX_NUM = 100000

sumCount = 0

for i in range(MAX_NUM,0,-1):
    print(i)
    sumCount += 1/(i+1)

print("Summe für",MAX_NUM,"vorgänge: ",sumCount)