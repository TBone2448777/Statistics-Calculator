import scipy.stats, math
n = float(input("What is n? "))
dBar = float(input("What is dBar? "))
c = float(input("What is the confidence interval? "))
if c >= 1:
    c = c/100
    c = 1 - c
    c = c/2
sd = float(input("What is sd? "))
t = abs(scipy.stats.t.ppf(c, n-1))
e = t*(sd/math.sqrt(n))
print("E is " + str(e))
print("(" + str(dBar-e) + ", " + str(dBar+e) + ")")