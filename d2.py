# 2. n ees m hurtelh sondgoi toonuudyn niilber ol
n, m = [int(x) for x in input().split()]
niilber = 0
for i in range(n, m+1):
    if i % 2 == 1:
        print(i)
        niilber = niilber + i
print( "niilber", niilber)