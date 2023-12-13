import scipy.stats, math

x = float(input("What is x? "))
n = int(input("What is n? "))
phat = x/n
print("PHat = " + str(phat))
c = float(input("What is the confidence level? "))
if c >= 1:
    c = c/100
    c = c + (1-c)/2
    c = c*2
z = abs(scipy.stats.norm.ppf(c/2))
e = z*math.sqrt(((phat*(1-phat))/n))
print("Critical value = " + str(z))
print("E = " + str(e))
print("(" + str(phat-e) + ", " + str(phat+e) + ")")