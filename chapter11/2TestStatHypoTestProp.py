import math, scipy.stats
print()
state = False
x1 = float(input("What is x1? "))
n1 = float(input("What is n1? "))
x2 = float(input("What is x2? "))
n2 = float(input("What is n2? "))
phat1 = x1/n1
phat2 = x2/n2
pbar = (x1+x2)/(n1+n2)
zNum = (phat1-phat2)
zDenom = math.sqrt(pbar*(1-pbar)*((1/n1)+(1/n2)))
z = zNum/zDenom
print()
print("Z is " + str(z))
print()
ci = float(input("What is the confidence level? "))
if ci >= 1:
    ci = ci/100
    ci = 1 - ci
    ci = ci/2
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
print("Zalpha is " + str(zAlpha))
if state:
    print("Reject H0.")
else:
    print("Fail to reject H0.")