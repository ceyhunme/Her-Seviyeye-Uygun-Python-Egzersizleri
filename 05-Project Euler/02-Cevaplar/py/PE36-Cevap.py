def ikilikTaban(n):
    kalanlar= list()
    while n != 0:
        kalan = n % 2
        kalanlar.append(str(kalan))
        n //= 2
    sonuc = "".join(kalanlar)[::-1]
    return sonuc

toplam = 0

for sayi in range (0,1000000):
    if str(sayi) == str(sayi)[::-1] and ikilikTaban(sayi) == ikilikTaban(sayi)[::-1]:
        toplam += sayi
        
print(toplam)