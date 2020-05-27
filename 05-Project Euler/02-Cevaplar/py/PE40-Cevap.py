a = "".join(str(i) for i in range(1,1000005))

cevap = 1
for i in range(0,7):
    cevap *= int(a[10**i-1])
    
print(cevap)