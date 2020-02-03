def ters(yazi):
    kelimeler = yazi.split()
    cevap = ""
    for kelime in kelimeler:
        if len(kelime) < 5:
            cevap += kelime + " "
        else:
            cevap += kelime[::-1] + " "
    return cevap.strip()