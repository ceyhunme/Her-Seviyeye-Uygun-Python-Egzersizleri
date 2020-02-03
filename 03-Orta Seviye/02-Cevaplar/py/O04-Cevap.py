def ping_pong(liste,kazanma):
    sonuc = ["Ping!","Pong!"]*len(liste)
    if kazanma:
        return sonuc
    else:
        return sonuc[:-1]
    
def ping_pong2(liste,kazanma):
    sonuc = ["Ping!","Pong!"]*len(liste)
    return sonuc if kazanma else sonuc[:-1]