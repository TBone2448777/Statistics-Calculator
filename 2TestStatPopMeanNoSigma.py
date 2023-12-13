import math, scipy.stats
def findMeanOfList():
    lst = []
    total = 0
    while True:
        val = input("Append what? ")
        if val == "q":
            break
        elif " " in val:
            val = val.split()
            for i in range(int(val[0])):
                lst.append(float(val[1]))
        elif val == "l":
            commas = input("What splitter? ")
            val = input("Append what? ")
            val = val.split(commas)
            for j in val:
                lst.append(float(j))
        elif val == "stem":
            multiplier = float(input("What is the leaf value? "))
            while val != "q":
                stem = float(input("What is the stem? "))
                val = 0
                while val != "n" and val != "q":
                    val = input("What is leaf value? ")
                    if val != "n" and val != "q":
                        val = float(val)
                        lst.append(stem*10*multiplier + val*multiplier)
            val = "x"
        else:
            lst.append(float(val))
    lst.sort()
    for i in lst:
        total += i
    count = len(lst)
    if len(lst) > 1:
        mean = total/count
    return mean
xBar1 = input("What is sample mean 1? ")
if xBar1 == "list":
    xBar1 = findMeanOfList()
else:
    xBar1 = float(xBar1)
n1 = float(input("What is sample size 1? "))
s1 = float(input("What is sample standard deviation 1? "))
xBar2 = input("What is sample mean 2? ")
if xBar2 == "list":
    xBar2 = findMeanOfList()
else:
    xBar2 = float(xBar2)
n2 = float(input("What is sample size 2? "))
s2 = float(input("What is sample standard deviation 2? "))
tNumerator = (xBar1-xBar2)
tDenominator = math.sqrt(((s1)**2)/n1 + ((s2)**2)/n2)
t = tNumerator/tDenominator
print()
print("T is: " + str(t) + ".")
print()
ci = float(input("What is the confidence interval? "))
if ci >= 1:
    ci = ci/100
    ci = 1 - ci
    ci = ci/2
hypo = input("What sign is hypothesis? ")
pooled = input("Pooled or non-pooled? ").lower()
if pooled == "pooled":
    df = n1 + n2 - 2
else:
    df = min(n1, n2)-1
if hypo == "=":
    t = abs(t)
    tAlpha = abs(scipy.stats.t.ppf(ci/2, df))
elif hypo =="<":
    tAlpha = -abs(scipy.stats.t.ppf(ci, df))
elif hypo ==">":
    tAlpha = abs(scipy.stats.t.ppf(ci, df))
print()
print("Z Alpha is: " + str(tAlpha))
if abs(t) < tAlpha:
    print("Fail to reject H0.")
else:
    print("Reject H0.")
print()