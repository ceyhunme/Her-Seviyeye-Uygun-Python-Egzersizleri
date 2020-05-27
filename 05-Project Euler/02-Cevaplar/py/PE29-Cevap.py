kume = set()

for a in range(2,101):
    for b in range(2,101):
        sayi = a ** b
        kume.add(sayi)
        
len(kume)