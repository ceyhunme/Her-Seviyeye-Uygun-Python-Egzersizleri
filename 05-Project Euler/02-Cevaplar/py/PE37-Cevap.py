from sympy import isprime as asalMı

def soldanKontrol(n):
    sayi = str(n)
    for i in range(0,len(sayi)):
        sayi2 = int(sayi[i::]) 
        if asalMı(sayi2) == False:
            return False
    return True

def sagdanKontrol(n):
    sayi = str(n)
    for i in range(0,len(sayi)):
        sayi2 = int(sayi[:i+1:]) 
        if asalMı(sayi2) == False:
            return False
    return True

sayac = 0
gercekSayi = 10
liste = list()

while True:
    if asalMı(gercekSayi) and soldanKontrol(gercekSayi) and sagdanKontrol(gercekSayi):
        liste.append(gercekSayi)  
    if len(liste) == 11:
        break
    gercekSayi += 1
    
print(liste)
sum(liste)