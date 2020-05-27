for a in range(1,1000):
    for b in range(1,1000-a):
        c = 1000 - a - b
        if c**2 == a**2 + b**2:
            print(a*b*c)
            print(a,b,c)
            break