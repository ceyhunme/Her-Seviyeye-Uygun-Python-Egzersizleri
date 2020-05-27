toplam = 0

for n in range(1,10000):
    for i in range(1,n):
        if n % i == 0:
            birleş = str(n) + str(i) + str(n//i)
            if "".join(sorted(birleş)) == "123456789":
                toplam += n
                break
                
print(toplam)