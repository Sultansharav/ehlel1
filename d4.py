# 4. n ees m hurtelh 3t huvaagdah toonuudyn niilber ol
n, m = [int(x) for x in input().split()]
niilber = 0
for i in range(n, m+1):
    if i % 3 == 0:
        print(i)
        niilber = niilber + i
print("niilber", niilber)