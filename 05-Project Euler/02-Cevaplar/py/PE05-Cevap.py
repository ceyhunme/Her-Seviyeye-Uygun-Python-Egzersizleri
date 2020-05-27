from math import gcd as ebob
import functools
def ekok(x,y):
    return (x*y) // ebob(x,y)
liste = range(1,21)
sonuc = functools.reduce(ekok,liste)
print(sonuc)
