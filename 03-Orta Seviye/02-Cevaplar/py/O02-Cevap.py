def kazanc(bilgi):
    a=bilgi["maliyet"]
    b=bilgi["satış"]
    c=bilgi["envanter"]
    toplam_maliyet = a*c
    toplam_satış = b*c
    kazanc = round(toplam_satış-toplam_maliyet)
    return kazanc