def kısalt(kelime):
    yeni_kelime = ""
    karakterler = list()
    for i in kelime:
        karakterler.append(i)
    k=0
    for karakter in karakterler:
        if k == len(karakterler) -1 :
            yeni_kelime += karakter
            break
        if karakter != karakterler[k+1]:
            yeni_kelime += karakter
        k+=1
    return yeni_kelime
        