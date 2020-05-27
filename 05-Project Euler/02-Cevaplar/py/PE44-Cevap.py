pentagonSayılar = list()
liste = list()
for n in range(1,10000):
    pentagonSayılar.append((n*(3*n-1))//2)

def kontrol(x):
    return ((1+(1+24*x)**(1/2))/6).is_integer()

for i in range(0,5000):
    for j in range(i+1,4999):
        if kontrol(pentagonSayılar[i]+pentagonSayılar[j]) and kontrol(pentagonSayılar[j]-pentagonSayılar[i]):
            liste.append(pentagonSayılar[j]-pentagonSayılar[i])
            break
            
print(liste)