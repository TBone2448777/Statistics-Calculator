import math, scipy.stats
xBar = float(input("What is sample mean? "))
mu = float(input("What is population mean? "))
n = float(input("What is sample size? "))
s = float(input("What is standard deviation? "))
t = (xBar-mu)/(s/(math.sqrt(n)))
print()
print("T is: " + str(t) + ".")
print()
ci = float(input("What is the confidence interval? "))
if ci >= 1:
    ci = ci/100
    ci = 1 - ci
    ci = ci/2
state=False
df = n-1
tAlpha = abs(scipy.stats.t.ppf(ci/2, n-1))
if abs(t) >= tAlpha:
    state = True
print()
print("T Alpha is: " + str(tAlpha))
if state:
    print("Reject H0.")
else:
    print("Fail to reject H0.")
print()