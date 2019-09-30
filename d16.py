# 16. Tsifruudiin niilber ni k baih buh 3 orontoi toonuudyn toog ol
k = int(input())
for i in range(101, 1000):
    too = 0
    if i // 100 + i % 100 // 10 + i % 10 == k:
        print(i)
        too+=1
print("Tsifruudiin niilber ni k baih buh 3 orontoi toonuudyn too: ", too)