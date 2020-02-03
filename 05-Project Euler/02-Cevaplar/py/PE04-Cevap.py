palindromSayilar = list()
for i in range(100,1000):
    for j in range(100,1000):
        carpim = i *j
        if str(carpim)==str(carpim)[::-1]:
            palindromSayilar.append(carpim)
max(palindromSayilar)
            
            