gecmisSayilar = dict()
def collatz(sayi,gecmisSayilar):
    verilen = sayi
    kacAdim = 1
    while sayi != 1:
        if sayi in gecmisSayilar:
            kacAdim += gecmisSayilar[sayi] - 1
            break
        if sayi % 2 == 0:
            sayi //= 2
            kacAdim += 1
        else: 
            sayi = 3* sayi + 1
            kacAdim += 1
    gecmisSayilar[verilen] = kacAdim
    return kacAdim

maksimumAdimSayaci = list()

for i in range(1,1000001):
    maksimumAdimSayaci.append(collatz(i,gecmisSayilar))

for sayi, adim in gecmisSayilar.items():
    if adim == 525:
        print(sayi)