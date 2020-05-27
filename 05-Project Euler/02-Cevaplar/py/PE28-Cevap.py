köşe = 0
boşluk = 1
dörtKöşe = 4 

toplam = 0

for n in range(1,1001**2+1):
    if köşe == 0:
        toplam += n
        köşe = boşluk
        dörtKöşe -=1
    elif köşe != 0:
        köşe -= 1
    if dörtKöşe == 0:
        boşluk += 2
        dörtKöşe = 4
        
print(toplam)