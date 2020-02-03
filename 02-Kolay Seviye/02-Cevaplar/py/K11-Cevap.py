def buyuk_kucuk(deger):
    yeni = deger.split()
    yeni = [int(i) for i in yeni]
    buyuk = max(yeni)
    kucuk = min(yeni)
    return str(buyuk)+ " " + str(kucuk)