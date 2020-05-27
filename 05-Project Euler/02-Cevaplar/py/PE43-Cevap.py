from itertools import permutations as permütasyon

rakamlar = "0123456789"

sayılar = permütasyon(rakamlar)
pandijitalSayılar = ["".join(sayı) for sayı in sayılar if not sayı[0] == "0" ]
asallar = [2,3,5,7,11,13,17]

toplam = 0

for sayı in pandijitalSayılar:
    kontrol = True
    for i in range(0,len(asallar)):
        if int(sayı[i+1:i+4]) % asallar[i] != 0:
            kontrol = False
            break
    if kontrol:
        toplam += int(sayı)
    
print(toplam)