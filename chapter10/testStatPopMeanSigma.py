import math, scipy.stats
xBar = float(input("What is sample mean? "))
mu = float(input("What is population mean? "))
n = float(input("What is sample size? "))
sigma = float(input("What is population standard deviation? "))
z = (xBar-mu)/(sigma/(math.sqrt(n)))
print()
print("Z is: " + str(z) + ".")
print()
ci = float(input("What is the confidence interval? "))
if ci >= 1:
    ci = ci/100
    ci = 1 - ci
    ci = ci/2
zAlpha = abs(scipy.stats.norm.ppf(ci))
print()
print("Z Alpha is: " + str(zAlpha))
if z <= zAlpha:
    print("Fail to reject H0.")
else:
    print("Reject H0.")