import math, scipy.stats
def getList():
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
    return lst
def difflist(lst1, lst2):
    diffList = []
    if len(lst1) == len(lst2):
        for i in range(len(lst1)):
            diffList.append(lst2[i]-lst1[i])
    return diffList
def getDBar(lst):
    total=0
    for i in lst:
        total += i
    return total/len(lst)
def getSSubD(dBar, lst):
    numerator = 0
    for i in lst:
        numerator += (i-dBar)**2
    return math.sqrt(numerator/(len(lst)-1))
muD = float(input("What is mu sub d? "))
print()
print("What items are in list 1? ")
lst1 = getList()
print()
print("What items are in list 2? ")
lst2 = getList()
print()
diffList = difflist(lst1, lst2)
dBar = getDBar(diffList)
sSubD = getSSubD(dBar, diffList)
t = (dBar-muD)/(sSubD/math.sqrt(len(diffList)))
print("D Bar = " + str(dBar))
print("S Sub = " + str(sSubD))
print("T = " + str(t))
print()
ci = float(input("What is the confidence interval? "))
if ci >= 1:
    ci = ci/100
    ci = 1 - ci
    ci = ci/2
state=False
hypo = input("What sign is hypothesis? ")
df = len(diffList)-1
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
print(tAlpha)
if state:
    print("Reject H0.")
else:
    print("Fail to reject H0.")