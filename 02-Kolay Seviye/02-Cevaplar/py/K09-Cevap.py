def say(yazi):
    ara  = yazi.lower()
    harfler = set("abcçdefgğhıijklmnoöprsştuüvyz")
    rakam = set("0123456789")
    sayılanHarf = 0
    sayılanRakam = 0
    for karakter in ara:
        if karakter in harfler:
            sayılanHarf += 1
        elif karakter in rakam:
            sayılanRakam +=1
    return {"Harfler":sayılanHarf,"Sayılar":sayılanRakam}

def say2(yazi):
    dict = {"Harfler":0,"Sayılar":0}
    for karakter in yazi:
        if karakter.isalpha():
            dict["Harfler"] += 1
        if karakter.isdigit():
            dict["Sayılar"] += 1
    return dict