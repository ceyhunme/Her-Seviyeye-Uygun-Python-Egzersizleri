def vezir(oyuncular):
    harfler = "ABCDEFGH"
    p1 = oyuncular[0]
    p2 = oyuncular[1]
    if p1[0] == p2[0] or p1[1] == p2[1]:
        return True
    poz1 = harfler.index(p1[0])
    poz2 = harfler.index(p2[0])
    yatay = abs(poz1-poz2)
    dikey = abs(int(p1[1])-int(p2[1]))
    if yatay == dikey:
        return True
    else:
        return False