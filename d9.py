# 9. n ees m hurtelh buh tegsh toonuudyn toog ol
n, m = [int(x) for x in input().split()]
too = 0
for i in range(n, m+1):
    if i % 2 == 0:
        print(i)
        too+=1
print("hariu: ", too)