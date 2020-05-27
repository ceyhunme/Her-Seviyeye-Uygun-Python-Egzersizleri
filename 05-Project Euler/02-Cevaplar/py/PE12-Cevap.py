def bolenSayi(x):
    bolenSayisi = 0
    for i in range(1,x+1):
        if x % i == 0:
            bolenSayisi += 1
    return bolenSayisi

n = 1
while True:
    ucgenselSayi = (n*(n+1)) // 2
    if bolenSayi(ucgenselSayi) > 500:
        print(ucgenselSayi)
        break
    n += 1

