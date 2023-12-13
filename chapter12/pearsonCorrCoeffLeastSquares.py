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
def listTotal(lst):
    total = 0
    for i in lst:
        total+= i
    return total
def doubleListTotal(lst1, lst2):
    total = 0
    for i in range(len(lst1)):
        total+= lst1[i]*lst2[i]
    return total
def leastSquares(lst1, lst2):
    b1num = len(lst1)*doubleListTotal(lst1, lst2)-listTotal(lst1)*listTotal(lst2)
    b1denom = len(lst1)*doubleListTotal(lst1, lst1)-listTotal(lst1)**2
    b1 = b1num/b1denom
    b0 = listTotal(lst2)/len(lst1)-b1*(listTotal(lst1)/len(lst1))
    return b0, b1
state = False
print()
print("What items are in list x? ")
lstx = getList()
print()
print("What items are in list y? ")
lsty = getList()
print()
rNum = len(lstx)*doubleListTotal(lstx, lsty)-listTotal(lstx)*listTotal(lsty)
rDen = math.sqrt((len(lstx)*doubleListTotal(lstx, lstx))-(listTotal(lstx)**2))*math.sqrt((len(lsty)*doubleListTotal(lsty, lsty))-(listTotal(lsty)**2))
r = rNum/rDen
print("r is equal to " + str(r))
t = r/math.sqrt((1-(r**2))/(len(lstx)-2))
print("t is equal to " + str(t))
print("Coefficient of determination: " + str(r**2))
print()
ci = float(input("What is the confidence level? "))
if ci >= 1:
    ci = ci/100
    ci = 1 - ci
    ci = ci/2
hypo = input("What sign is hypothesis? ")
df = len(lstx)-2
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
print("t alpha is " + str(tAlpha))

print("Reject H0.")
print()
b0, b1 = leastSquares(lstx, lsty)
print("b0 is " + str(b0))
print("b1 is " + str(b1))
