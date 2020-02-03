def camelCasing(yazi):
    yazi = yazi.replace("_"," ")
    kelimeler = yazi.split(" ")
    kelimeler[0] = kelimeler[0].lower()
    for i in range(1,len(kelimeler)):
        kelimeler[i] = kelimeler[i].title()
    return "".join(kelimeler)