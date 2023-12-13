import scipy.stats
lst = []
lst2=[]
while True:
    val = input("Append what? ")
    if val == "q":
        break
    elif " " in val:
        val = val.split()
        for i in range(int(val[0])):
            lst.append(float(val[1]))
    elif val == "l":
        commas = input("What splitter? ")
        val = input("Append what? ")
        val = val.split(commas)
        for j in val:
            lst.append(float(j))
    elif val == "stem":
        multiplier = float(input("What is the leaf value? "))
        while val != "q":
            stem = float(input("What is the stem? "))
            val = 0
            while val != "n" and val != "q":
                val = input("What is leaf value? ")
                if val != "n" and val != "q":
                    val = float(val)
                    lst.append(stem*10*multiplier + val*multiplier)
        val = "x"
    else:
        lst.append(float(val))
try:
    e = float(input("What is the expected value? "))
    for i in lst:
        lst2.append(e)
except:
    val = ""
    while val != "q":
        val = input("Enter value: ")
        if "/" in val:
            lst2.append(float(val.split("/")[0])/float(val.split("/")[1]))
        elif "*" in val:
            lst2.append(float(val.split("*")[0])*float(val.split("*")[1]))
        elif val != "q":
            lst2.append(float(val))
sig = float(input("What is the level of significance? "))
chisquared = 0
for i in range(len(lst)):
    chisquared += ((lst[i]-lst2[i])**2)/lst2[i]
chisquaredalpha = scipy.stats.chi2.ppf(1-sig, len(lst)-1)
print()
print("Chi Squared of sample is " + str(chisquared))
print("Chi Squared supposed to be " + str(chisquaredalpha))
if chisquared >= chisquaredalpha:
    print("Reject H0")
else:
    print("Fail to reject H0")