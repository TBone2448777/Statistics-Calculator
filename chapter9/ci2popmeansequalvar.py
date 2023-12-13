import scipy.stats, math

n1 = float(input("What is n 1? "))
xbar1 = float(input("What is mean 1? "))
s1 = float(input("What is standard deviation 1? "))
n2 = float(input("What is n 2? "))
xbar2 = float(input("What is mean 2? "))
s2 = float(input("What is standard deviation 2? "))
ci = float(input("What is the confidence interval? "))
if ci >= 1:
    ci = ci/100
    ci = 1 - ci
t = abs(scipy.stats.t.ppf(ci/2, n1 + n2 - 2))
e = t*math.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2)/(n1+n2-2))*math.sqrt((1/n1)+(1/n2))
print()
print("T is " + str(t))
print("Point estimate is " + str(xbar1-xbar2))
print("E is " + str(e))
print("The confidence interval is (" + str(xbar1-xbar2-e) + ", " + str(xbar1-xbar2+e) + ").")