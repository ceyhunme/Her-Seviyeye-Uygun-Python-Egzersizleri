from sympy import isprime as asalMı
i= 1
asallar = list()
while True:
    if asalMı(i):
        if sum(asallar) < 1000000:
            asallar.append(i)
        else:
            break
    i += 1

maksimumArdaşıkSayı = 0
toplam = 0

for i in range(0,len(asallar)):
    for j in range(i,len(asallar)):
        if asalMı(sum(asallar[i:j])):
            if j-i > maksimumArdaşıkSayı:
                maksimumArdaşıkSayı = j - i
                toplam = sum(asallar[i:j])
                
print(maksimumArdaşıkSayı)
print(toplam)
                