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
    return mean, lst
def findSDevOfList(lst, mean):
    svariance = 0
    for i in lst:
        svariance += (i-mean)**2
    svariance /= (len(lst)-1)
    sdeviation = math.sqrt(svariance)
    return sdeviation
state=False
xBar1 = input("What is sample mean 1? ")
if xBar1 == "list":
    xBar1, lst1 = findMeanOfList()
else:
    xBar1 = float(xBar1)
n1 = float(input("What is sample size 1? "))
s1 = input("What is sample standard deviation 1? ")
if s1 == "list":
    s1 = findSDevOfList(lst1, xBar1)
else:
    s1 = float(s1)
xBar2 = input("What is sample mean 2? ")
if xBar2 == "list":
    xBar2, lst2 = findMeanOfList()
else:
    xBar2 = float(xBar2)
n2 = float(input("What is sample size 2? "))
s2 = input("What is sample standard deviation 2? ")
if s2 == "list":
    s2 = findSDevOfList(lst2, xBar2)
else:
    s2 = float(s2)
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
df = min(n1, n2)-1
if hypo == "=":
    tAlpha = abs(scipy.stats.t.ppf(ci/2, df))
    if abs(t) >= tAlpha:
        state = True
elif hypo =="<":
    tAlpha = -abs(scipy.stats.t.ppf(ci, df))
    if t <= tAlpha:
        state = True
elif hypo ==">":
    tAlpha = abs(scipy.stats.t.ppf(ci, df))
    if t >= tAlpha:
        state = True
print()
print("T Alpha is: " + str(tAlpha))
if state:
    print("Reject H0.")
else:
    print("Fail to reject H0.")
print()