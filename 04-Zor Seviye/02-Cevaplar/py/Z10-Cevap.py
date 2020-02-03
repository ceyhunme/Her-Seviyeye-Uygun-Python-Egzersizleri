def en_yüksek_çift(kartlar):
    çiftler = set([ord(x) for x in kartlar if kartlar.count(x) >1 ])
    if len(çiftler) == 0:
        return False
    else:
        if 65 in çiftler:
            return [True, chr(65)]
        else:
            return [True, chr(max(çiftler))]
        