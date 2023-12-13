import scipy.stats, math

n = int(input("What is n? "))
s = float((input("What is s? ")))
c = float(input("What is the confidence interval? "))
m = float(input("What is the mean? "))
if c >= 1:
    c = c/100
    c = 1 - c
t = abs(scipy.stats.t.ppf(c/2, n-1))
e = t*(s/math.sqrt(n))
print("Critical value = " + str(t))
print("E = " + str(e))
print("(" + str(m-e) + ", " + str(m+e) + ")")