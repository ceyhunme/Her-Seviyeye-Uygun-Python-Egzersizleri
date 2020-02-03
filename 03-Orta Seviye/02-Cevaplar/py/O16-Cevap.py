def sansür(sansürlü,sesli):
    k=0
    cevap = ""
    for i in sansürlü:
        if i == "*":
            cevap += sesli[k]
            k+=1
        else:
            cevap += i
    return cevap