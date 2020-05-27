import sympy

liste = list()

for i in range(2,1000000):
    if sympy.isprime(i):
        stringI = str(i)
        sayac = 0
        for j in range(0,len(stringI)):
            
            if sympy.isprime(int(stringI[j : ] + stringI[ : j])):
                sayac += 1
            if sayac == len(stringI):
                liste.append(i)    
    
print(liste)


print(len(liste))