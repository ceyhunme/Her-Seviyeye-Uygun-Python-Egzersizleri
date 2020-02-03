def carpanlar(sayi):
    liste = []
    #liste = list()
    for i in range(1,sayi+1):
        if sayi % i == 0:
            liste.append(i)
    return liste