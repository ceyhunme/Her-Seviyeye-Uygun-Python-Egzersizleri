toplam = 0
x=1
y=2
while x <4000000:
    if x % 2 == 0:
        toplam += x
    x,y=y,x+y
print(toplam)
