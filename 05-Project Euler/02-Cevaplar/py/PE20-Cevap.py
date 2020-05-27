sayi = 1

for i in range(1,101):
    sayi *= i
    
sayi = str(sayi)

toplam = 0
for i in range(0,len(sayi)):
    toplam += int(sayi[i])
    
print(toplam)


