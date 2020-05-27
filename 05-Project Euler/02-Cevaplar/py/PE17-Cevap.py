birler = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

onlar = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def ingilizce(n):
    if 0 <= n < 20:
        return birler[n]
    elif 20 <= n < 100:
        return onlar[n//10] + (birler[n%10] if (n%10!=0 ) else "")
    elif 100 <= n < 1000:
        return birler[n//100] + "hundred" + (("and" + ingilizce(n%100)) if (n % 100 != 0) else "")
    elif 1000 == n:
        return "onethousand"
    
    
toplam = 0
for i in range(1,1001):
    toplam += len(ingilizce(i))
print(toplam)