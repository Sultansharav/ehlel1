# 6. a toog b zeregt devshuul
# 2**5 = 2*2*2*2*2 = 32
a, b = [int(x) for x in input().split()]
res = 1
for i in range(b):
    res = res * a
print("hariu", res)