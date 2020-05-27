cevreler = dict()

for a in range(1,1000):
    for b in range(1,1000):
        c = (a**2 + b**2)**(1/2)
        cevre = a + b + c
        if cevre <= 1000 and c % 1 == 0 :
            if cevre in cevreler:
                cevreler[cevre] += 1
            else:
                cevreler[cevre] = 1
        
for k,v in cevreler.items():
    if v == max(cevreler.values()):
        print(k)
    

 