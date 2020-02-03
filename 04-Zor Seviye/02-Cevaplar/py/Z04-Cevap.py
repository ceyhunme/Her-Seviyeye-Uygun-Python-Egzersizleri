def deger(s):
    harfler = " abcdefghijklmnopqrstuvwxyz"
    deger = 0
    for i in s:
        if i.isalpha():
            deger += harfler.index(i)
        else:
            deger += int(i)
    return deger

def asal_mı(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return n != 1

def kelime_asallığı(cümle):
    cümle = "".join([i for i in cümle if i.isalnum() or i == " "]).split()
    s = [deger(i.lower()) for i in cümle]
    if asal_mı(sum(s)):
        return "Asal Cümle"
    else:
        for i in range(len(s)):
            if asal_mı(sum(s)-s[i]):
                return "Neredeyse Asal Cümle (" + cümle[i] +")"
    return "Kompozit Cümle"