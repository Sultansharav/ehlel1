# 18. m too hurtel heden anhny too baigaag ol
n = int(input())
too = 0
for i in range(2, n + 1):
    k = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            k +=1
    if k == 0:
        print(i)
        too+=1
print("Anhny toonuudyn too ni: ", too)