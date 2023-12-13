# Horizontal table, top half is x, bottom half is y
# Vertical table, left half is x, right half is y

import scipy.stats, math
ans = input("What do you have (2lists, differences)? ")
differences= []
if ans == "2lists":
    lstx = []
    lsty = []
    while ans != "q":
        ans = input("What would you like to append to list 1? ")
        if ans != "q":
            lstx.append(float(ans))
        else:
            ans = ""
            break
    while ans != "q":
        ans = input("What would you like to append to list 2? ")
        if ans != "q":
            lsty.append(float(ans))
        else:
            break
    for i in range(len(lstx)):
        differences.append(lsty[i] - lstx[i])
    print()
    print(lstx)
    print(lsty)
elif ans == "differences":
    while ans != "q":
        ans = input("What would you like to append to difference list? ")
        if ans != "q":
            differences.append(float(ans))
print()
sigmaD = 0
for i in differences:
    sigmaD += i
dBar = sigmaD/len(differences)
print("d bar is " + str(dBar))
sigmaDD = 0
for i in differences:
    sigmaDD += (i-dBar)**2
sd = math.sqrt((sigmaDD)/(len(differences)-1))
print("sd is " + str(sd))
print()
ans = input("Do you want to calculate margin of error? ")
if ans != "q":
    n = len(differences)
    c = float(input("What is the confidence interval? "))
    if c >= 1:
        c = c/100
        c = 1 - c
    t = abs(scipy.stats.t.ppf(c/2, n-1))
    e = t*(sd/math.sqrt(n))
    print()
    print("E is " + str(e))
    print("(" + str(dBar-e) + ", " + str(dBar+e) + ")")