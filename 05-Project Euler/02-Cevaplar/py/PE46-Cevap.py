from sympy import isprime as asalMı

sayı = 2

while True:
    if asalMı(sayı) or sayı % 2==0:
        sayı += 1
        continue
    olurMu = False
    n = 1
    while sayı - 2 * n * n > 0:
        if asalMı(sayı - 2 * n * n):
            olurMu = True
            break
        n +=1
    if olurMu == False:
        print(sayı)
        break
    sayı += 1
    