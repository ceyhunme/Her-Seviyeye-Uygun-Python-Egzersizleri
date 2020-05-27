def bolenToplam(n):
    toplam = 0
    for i in range(1,n):
        if n % i == 0:
            toplam += i
    return toplam

bagdasikSayilar = list()
for i in range(1,10000):
    if bolenToplam(bolenToplam(i)) == i and i != bolenToplam(i):
        bagdasikSayilar.append(i)
        
sum(bagdasikSayilar)

