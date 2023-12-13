import math
vals = []
ratio = []
mean = 0
variance = 0
ans = ""
while ans != "q":
    ans = input("What is the value? ")
    if ans != "q":
        vals.append(float(ans))
        ans = input("What is the ratio? ")
        try:
            ratio.append(float(ans))
        except:
            numer = ""
            denom = ""
            focus = "n"
            for i in ans:
                if focus == "n":
                    if i != "/":
                        numer += i
                    else:
                        focus = "d"
                else:
                    denom += i
            ratio.append(float(numer)/float(denom))
for i in range(len(vals)):
    mean+= vals[i] * ratio[i]
for i in range(len(vals)):
    variance += ((vals[i]-mean)**2)*ratio[i]
print("The mean is " + str(mean))
print("The variance is " + str(variance))
print("The standard deviation is " + str(math.sqrt(variance)))