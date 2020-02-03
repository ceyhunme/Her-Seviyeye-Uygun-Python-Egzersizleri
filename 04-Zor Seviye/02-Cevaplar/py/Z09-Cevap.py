def faktör_uzunlugu(sayılar):
    liste, liste2 = [],[]
    for x in sayılar:
        c = 0
        for i in range(1,x+1):
            if(x%i==0):
                c += 1
        liste.append([c,x])
    liste.sort()
    liste.reverse()
    for j in liste:
        liste2.append(j[1])
    return liste2