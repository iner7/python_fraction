#!/usr/bin/python3

def FloatToFraction(n):
    import fractions
    # used from https://fooobar.com/questions/2379201/python-find-repeated-substring-in-string/6210495#6210495
    def repeats(string):
        for x in range(1, len(string)):
            substring = string[:x]
            if substring * (len(string)//len(substring))+(substring[:len(string)%len(substring)]) == string:
                return substring
        return None
    s = str("%.17f"%n)
    ss = s.split('.')[1]
    ss = ss[:-1]
    nd = "" # nd - после запятой, но до периода
    rr = repeats(ss) # rr - период
    while (rr == None):
        nd += ss[0]
        ss = ss[1:]
        rr = repeats(ss)
    # used from https://your-online.ru/math-calculators/periodic-ordinary-fraction
    P = len(rr)
    DP = len(nd)
    if (nd == ""): nd = "0"
    ALL = int(nd+rr)
    ALL_DP = int(nd)
    CHISL = ALL - ALL_DP
    ZNAM  = int("9"*P + "0"*DP)
    a = fractions.Fraction(CHISL, ZNAM)
    a = a.limit_denominator()
    CHISL = a.numerator
    ZNAM  = a.denominator
    return CHISL, ZNAM

c, z = FloatToFraction(403/19980)
print(c, z)

c, z = FloatToFraction(5)
print(c, z)
