from sympy import isprime as asalMı
from itertools import permutations as permütasyon

rakamlar = "1234567"
sayilar = list(permütasyon(rakamlar))
pandijitalSayilar = ["".join(sayi) for sayi in sayilar]

sonuc = list()

for sayi in pandijitalSayilar:
    if asalMı(int(sayi)):
        sonuc.append(sayi)
        
max(sonuc)