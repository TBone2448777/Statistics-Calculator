import scipy.stats, math
n1 = float(input("What is n1? "))
x1 = float(input("What is x1? "))
n2 = float(input("What is n2? "))
x2 = float(input("What is x2? "))
ci = float(input("What is the confidence interval? "))
if ci >= 1:
    ci = ci/100
    ci = 1 - ci
phat1 = x1/n1
phat2 = x2/n2
z = abs(scipy.stats.norm.ppf(ci/2))
e = z*math.sqrt(((phat1*(1-phat1))/n1)+((phat2*(1-phat2))/n2))
print()
print("Point estimate is: " + str(max(phat1,phat2)-min(phat1,phat2)))
print("E is " + str(e))
print("(" + str(max(phat1,phat2)-min(phat1,phat2)-e) + ", " + str(max(phat1,phat2)-min(phat1,phat2)+e) + ")")