# print all odd numbers in range
# ene arga ni ehlehees tugsgul hurtelh buh sondgoi toonuudyn neg shugam dotor haruulna
''' start , end = 1, 15

for num in range(start, end + 1):
    if num % 2 == 1:
        print(num, end=" ")
'''
# n ees m hurtelh sondgoi buh toonuudyg hevle
n, m = [int(x) for x in input().split()]
for i in range(n, m+1):
    if i % 2 == 1:
        print(i) 