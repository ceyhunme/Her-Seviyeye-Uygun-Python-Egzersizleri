def sadelestir(deger):
    if type(deger) == list:
        return sadelestir(deger[0])
    else:
        return deger