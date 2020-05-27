import sympy

liste = list()

for a in range(-1000,1000):
    for b in range(-1000,1001):
        sayac = 0
        n = 0
        while sympy.isprime(n**2+a*n+b):
            sayac += 1
            n += 1          
        liste.append((sayac,a*b))
        