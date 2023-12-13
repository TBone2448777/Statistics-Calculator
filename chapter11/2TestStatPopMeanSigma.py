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
sigma1 = float(input("What is population standard deviation 1? "))
xBar2 = input("What is sample mean 2? ")
if xBar2 == "list":
    xBar2 = findMeanOfList()
else:
    xBar2 = float(xBar2)
n2 = float(input("What is sample size 2? "))
sigma2 = float(input("What is population standard deviation 2? "))
zNumerator = (xBar1-xBar2)
zDenominator = math.sqrt(((sigma1)**2)/n1 + ((sigma2)**2)/n2)
z = zNumerator/zDenominator
print()
print("Z is: " + str(z) + ".")
print()
ci = float(input("What is the confidence level? "))
if ci >= 1:
    ci = ci/100
    ci = 1 - ci
    ci = ci/2
state=False
hypo = input("What sign is hypothesis? ")
df = min(n1, n2)-1
if hypo == "=":
    z = abs(z)
    zAlpha = abs(scipy.stats.norm.ppf(ci/2))
    if abs(z) >= zAlpha:
        state = True
elif hypo =="<":
    zAlpha = -abs(scipy.stats.norm.ppf(ci))
    if z <= zAlpha:
        state = True
elif hypo ==">":
    zAlpha = abs(scipy.stats.norm.ppf(ci))
    if z >= zAlpha:
        state = True
print()
print("Z Alpha is: " + str(zAlpha))
if state:
    print("Reject H0.")
else:
    print("Fail to reject H0.")
print()