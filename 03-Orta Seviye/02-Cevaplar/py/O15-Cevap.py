def agac(n):
    cevap = list()
    genislik = 2*n-1
    for i in range(1,n+1):
        kare = "#"*(i*2-1)
        cevap.append(kare.center(genislik))
    return cevap