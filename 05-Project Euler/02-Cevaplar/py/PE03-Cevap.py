import math
def asal_mı(x):
    asalKontrol = True
    for i in range(2,x):
        if x % i == 0:
            asalKontrol = False
            break
    return asalKontrol

sayi = 600851475143
enBuyukAsal = 1

for k in range(2,int(math.sqrt(sayi)+1)):
    if sayi % k == 0 and asal_mı(k):
        enBuyukAsal = k
print(enBuyukAsal)

# Bir sayının karekökünden daha büyük bir asal çarpan yoktur!!!