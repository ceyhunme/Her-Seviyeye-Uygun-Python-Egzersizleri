sayac = 0
for ikiyüz in range(0,2):
    for yüz in range(3):
        if 200*ikiyüz+100*yüz > 200:
            break
        for elli in range(5):
            if 200*ikiyüz+100*yüz+50*elli > 200:
                break
            for yirmi in range(11):
                if 200*ikiyüz+100*yüz+50*elli+20*yirmi > 200:
                    break
                for on in range(21):
                    if 200*ikiyüz+100*yüz+50*elli+20*yirmi+10*on > 200:
                        break
                    for beş in range(41):
                        if 200*ikiyüz+100*yüz+50*elli+20*yirmi+10*on+5*beş > 200:
                            break
                        for iki in range(101):
                            if 200*ikiyüz+100*yüz+50*elli+20*yirmi+10*on+5*beş+2*iki > 200:
                                break
                            for bir in range(201):
                                if 200*ikiyüz+100*yüz+50*elli+20*yirmi+10*on+5*beş+2*iki+1*bir == 200:
                                    sayac += 1
                            
print(sayac)