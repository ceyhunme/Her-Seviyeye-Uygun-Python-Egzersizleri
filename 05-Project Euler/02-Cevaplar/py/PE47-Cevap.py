def asalCarpanSayısı(x):
    i = 2
    çarpanlar = set()
    while i < x**0.5:
        if x % i == 0:
            çarpanlar.add(i)
            x //= i
            i -= 1
        i += 1
    return len(çarpanlar) + 1
    
    
sayi = 2*3*5*7

while True:
    olurMu = True
    for i in range(0,4):
        if asalCarpanSayısı(sayi+i) != 4:
            olurMu = False
            break
    if olurMu:
        print(sayi)
        break
    sayi += 1
    