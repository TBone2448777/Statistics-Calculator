import scipy.stats, math
n1 = float(input("What is n1? "))
phat1 = float(input("What is phat1? "))
n2 = float(input("What is n2? "))
phat2 = float(input("What is phat2? "))
ci = float(input("What is the confidence interval? "))
if ci >= 1:
    ci = ci/100
    ci = 1 - ci
    ci = ci/2
z = abs(scipy.stats.norm.ppf(ci))
e = z*math.sqrt(((phat1*(1-phat1))/n1)+((phat2*(1-phat2))/n2))
print()
print("Point estimate is: " + str(phat1-phat2))
print("E is " + str(e))
print("(" + str(phat1-phat2-e) + ", " + str(phat1-phat2+e) + ")")