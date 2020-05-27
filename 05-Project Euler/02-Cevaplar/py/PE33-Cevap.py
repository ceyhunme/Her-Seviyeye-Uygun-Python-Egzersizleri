import math 

cevap = list()
carpimPay = 1
carpimPayda = 1
pay = i
payda = j

for i in range(10,100):
    for j in range(i+1,100):
        if i % 10 == 0 or j % 10 == 0:
            continue
            
        stringi = str(i)
        stringj = str(j)
        
        if stringi[1] == stringj[0]:
            if int(stringi[0]) / int(stringj[1]) == i / j:
                cevap.append(str(i)+"/"+str(j))
                carpimPay *= i
                carpimPayda *= j
                
        if stringi[0] == stringj[1]:
            if int(stringi[1]) / int(stringj[0]) == i / j:
                cevap.append(str(i)+"/"+str(j))
                carpimPay *= i
                carpimPayda *= j
                
        if stringi[0] == stringj[0]:
            if int(stringi[1]) / int(stringj[1]) == i / j:
                cevap.append(str(i)+"/"+str(j))
                carpimPay *= i
                carpimPayda *= j
                
        if stringi[1] == stringj[1]:
            if int(stringi[0]) / int(stringj[0]) == i / j:
                cevap.append(str(i)+"/"+str(j))
                carpimPay *= i
                carpimPayda *= j

print(cevap)
print(carpimPayda / math.gcd(carpimPayda,carpimPay))