def ucgenMi(x):
    return ((-1+(1+8*x)**(1/2))/2).is_integer()

def besgenMi(x):
    return ((1+(1+24*x)**(1/2))/6).is_integer()

def altıgenMi(x):
    return ((1+(1+8*x)**(1/2))/4).is_integer()

n=144
while True:
    altıgen = n * (2 *n -1)
    if ucgenMi(altıgen) and besgenMi(altıgen):
        print(altıgen)
        break
    n += 1