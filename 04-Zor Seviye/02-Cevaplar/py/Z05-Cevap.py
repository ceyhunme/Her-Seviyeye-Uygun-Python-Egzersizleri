def hapishaneden_kaçış(mahkum):
    if mahkum[0] == 0:
        return (0)
    say = 1
    for i in range(1,len(mahkum)):
        if mahkum[i] != mahkum[i-1]:
            say += 1
    return say