def sesli_kaldir(cumle):
    sesliHarfler = "aeiıoöuüAEİIOÖUÜ"
    yeni = ""
    for i in cumle:
        if i not in sesliHarfler:
            yeni += i
    return yeni