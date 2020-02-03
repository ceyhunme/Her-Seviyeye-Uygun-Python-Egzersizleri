def kelime_çift_mi(cümle):
    harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
    toplam = 0
    for harf in cümle.lower():
        if harf in harfler:
            toplam += harfler.index(harf) + 1
    return toplam % 2 == 0