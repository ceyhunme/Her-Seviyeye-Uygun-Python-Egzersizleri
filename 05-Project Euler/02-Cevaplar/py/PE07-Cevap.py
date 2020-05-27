import math
def asalKontrol(x):
    asalMı= True
    if x == 2:
        return True
    else:
        for i in range(2,int(math.sqrt(x)+1)):
            if x % i == 0:
                asalMı = False
                break
        return asalMı
asalListesi = list()
i = 2
while len(asalListesi) < 10001:
    if asalKontrol(i):
        asalListesi.append(i)
    i += 1
print(asalListesi[-1])