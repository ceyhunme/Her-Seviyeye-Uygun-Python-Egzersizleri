def saklı(yazi):
    liste = yazi.split(" ")
    yeni = list()
    tire = 0
    for deger in liste:
        if len(deger) > 2:
            tire = len(deger)-2
        else:
            tire = 0
        yeni.append(deger[0]+"-"*tire+deger[-1])
    return " ".join(yeni)