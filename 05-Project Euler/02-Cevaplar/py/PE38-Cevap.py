pandijital = list()

for i in range(1,10000):
    basamak = 1
    birleşim = ""
    while True:
        sayı = i * basamak
        birleşim += str(sayı)
        if len(birleşim) > 9:
            break
        if len(birleşim) == 9:
            if sorted(birleşim) == ['1', '2', '3', '4','5','6', '7', '8','9']:
                pandijital.append(int(birleşim))
                break
        basamak += 1
        
print(pandijital)