import math
round(math.log(100,10))
def us_bul(a,b):
    return round(math.log(b,a))

def us_bul2(a,b):
    cevap = 1
    while b > a:
        b = b/a
        cevap += 1
    return cevap