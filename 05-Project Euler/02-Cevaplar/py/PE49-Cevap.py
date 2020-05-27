from sympy import primerange 
asallar = list(primerange(1488,10000))

def aynıBasamak(x,y,z):
    return sorted(str(x)) == sorted(str(y)) == sorted(str(z))

for i in range(0,len(asallar)):
    for j in range(i+1,len(asallar)):
        asal1 = asallar[i]
        asal2 = asallar[j]
        asal3 = asal2 + (asal2-asal1)
        if asal3 in asallar:
            if aynıBasamak(asal1,asal2,asal3):
                print(asal1,asal2,asal3)
                break