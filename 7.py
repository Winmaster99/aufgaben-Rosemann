L = []
 

for i in range(0, 7):
    for j in range(0, 7):

        if (i, j) not in L and (j, i) not in L:
            L.append((i, j))

print(L)
print("Steine: ", len(L))