import scipy.stats, math

p = input("What is p? ")
try:
    p = float(p)
except:
    p = 0.5
c = float(input("What is the confidence interval? "))
if c >= 1:
    c = c/100
    c = c + (1-c)/2
z = abs(scipy.stats.norm.ppf(c))
e = float(input("What is e? "))
n = p*(1-p)*((z/e)**2)
print(math.ceil(n))