x = 1
y = 1
adim = 2
while True:
    x, y = y, x+y
    adim += 1
    if len(str(y)) == 1000:
        print(adim)
        break