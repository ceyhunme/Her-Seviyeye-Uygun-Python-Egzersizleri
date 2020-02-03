def blok_adam(x):
    yukseklik = []
    for i in range(len(x[0])):
        kontrol = []
        for j in range(len(x)):
            kontrol.append(x[j][i])
        if 1 in kontrol: yukseklik.append(len(x)-kontrol.index(1)) 
        else: yukseklik.append(0)
    for i in x:
        print(i)
    print(yukseklik)
    for i in range(len(yukseklik)-1):
        if yukseklik[i+1] > yukseklik[i] + 1 or yukseklik[i+1] < yukseklik[i] -1: return False
    return True