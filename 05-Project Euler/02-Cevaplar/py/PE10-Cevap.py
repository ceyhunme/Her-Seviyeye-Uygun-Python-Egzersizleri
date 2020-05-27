import math
def asalKontrol(x):
    asalMı = True
    if x == 2:
        return True
    else:
        for i in range(2,int(math.sqrt(x)+1)):
            if x % i == 0:
                asalMı = False
                break
        return asalMı
    
toplam = 0
i = 2
while i < 2000000:
    if asalKontrol(i):
        toplam += i
    i += 1
print(toplam)