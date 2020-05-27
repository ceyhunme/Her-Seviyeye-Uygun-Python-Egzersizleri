def bolenToplamı(x):
    toplam = 0 
    for i in range(1,x):
        if x % i == 0:
            toplam += i
    return toplam

def zenginKontrol(x):
    if bolenToplamı(x) > x:
        return True
    else:
        return False
        
zenginSayilar = list()
toplam = 0
zenginSayilarinToplamı = list()

for i in range(1,28124):
    if zenginKontrol(i):
        zenginSayilar.append(i)
        
zenginSayilarinToplamı = [0]*28124

for i in range(0,len(zenginSayilar)):
    for j in range(i,len(zenginSayilar)):
        if zenginSayilar[i] + zenginSayilar[j] <= 28123:
            zenginSayilarinToplamı[zenginSayilar[i] + zenginSayilar[j]] = zenginSayilar[i] + zenginSayilar[j]
 
for i in range(0,len(zenginSayilarinToplamı)):
    if zenginSayilarinToplamı[i] == 0:
        toplam += i
print(toplam)
