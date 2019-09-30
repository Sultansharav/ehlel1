# 12. Ugugdsen n too anhny / prime number / too mun vv?
# anhny too gej zuvhun 1 bolon uurtuu huvaagddag eereg toog helne
n = int(input())
if n > 1:
    for i in range(2, n // 2):
        if n % i == 0:
            print(n, "bol anhny too bish")
            break
    else:
        print(n, " bol anhny too mun")
else:
    print(n," bol anhny too bish")