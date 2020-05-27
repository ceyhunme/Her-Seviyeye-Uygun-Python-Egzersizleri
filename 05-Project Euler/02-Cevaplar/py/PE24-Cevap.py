from itertools import permutations

rakamlar = "0123456789"

sayilar = list(permutations(rakamlar))

sonuc = sayilar[999999]

print(sonuc)