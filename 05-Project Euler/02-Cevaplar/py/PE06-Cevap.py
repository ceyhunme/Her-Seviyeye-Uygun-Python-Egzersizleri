toplam1 = 0
for i in range(1,101):
    toplam1 +=i**2
toplam2=0
for j in range(1,101):
    toplam2 += j
toplam2 = toplam2**2
print(toplam2-toplam1)