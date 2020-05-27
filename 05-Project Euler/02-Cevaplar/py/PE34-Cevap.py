from math import factorial as faktöriyel
liste = list()

for sayi in range(0,1000000):
    toplam = 0
    sayi = str(sayi)
    for basamak in sayi:
        toplam += faktöriyel(int(basamak))
    sayi = int(sayi)
    if toplam == sayi:
        liste.append(sayi)

liste.pop(0)
liste.pop(0)
sum(liste)