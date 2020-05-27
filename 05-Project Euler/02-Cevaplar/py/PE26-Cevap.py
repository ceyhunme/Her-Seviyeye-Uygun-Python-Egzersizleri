bolen = 2
liste = list()

while bolen < 1000:
    bolunen = 1
    kalanlar = []
    while True:
        kalan = bolunen % bolen
        if kalan in kalanlar:
            ilkIndex = kalanlar.index(kalan)
            sonIndex = len(kalanlar)
            sayi = bolen
            liste.append(((sonIndex-ilkIndex),sayi))
            break
        bolunen = 10 * kalan
        kalanlar.append(kalan)
    bolen += 1
    
max(liste)