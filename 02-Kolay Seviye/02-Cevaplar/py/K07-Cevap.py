def yuzyil(yil):
    n = yil//100
    if (yil%100>0):
        n+=1
    return "{s}. yüzyıl".format(s=n)