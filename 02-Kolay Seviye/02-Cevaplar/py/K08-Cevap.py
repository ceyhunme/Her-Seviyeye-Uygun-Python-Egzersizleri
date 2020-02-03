def index_carpici(liste):
    toplam = 0
    for i in range(len(liste)):
        toplam += liste[i]*i
    return toplam

def index_carpici2(liste):
    return sum([index*sayi for index,sayi in enumerate(liste)])