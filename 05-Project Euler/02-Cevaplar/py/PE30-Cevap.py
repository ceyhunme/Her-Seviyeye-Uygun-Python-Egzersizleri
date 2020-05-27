liste = list()

for i in range(2,1000000):
    toplam = 0
    for j in str(i):
        toplam += int(j) ** 5
    if toplam == i:
        liste.append(i)
        
sum(liste)