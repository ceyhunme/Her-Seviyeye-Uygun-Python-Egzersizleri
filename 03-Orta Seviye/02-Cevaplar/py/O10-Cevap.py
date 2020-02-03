def saat_cevir(saat):
    if len(saat) > 5:
        sd, ek=saat.split()
        if ek == "pm":
            s,d = sd.split(":")
            s = str(int(s)+12)
            return s+":"+d
        elif ek == "am":
            if sd == "12:00":
                return "0:00"
            return sd
    s,d = saat.split(":")
    if int(s) <= 12:
        return saat + " am"
    s =str(int(s)-12)
    return s + ":" + d + " pm"