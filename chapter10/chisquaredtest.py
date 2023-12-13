import scipy.stats
length = int(input("What is the matrix length? "))
height = int(input("What is the matrix height? "))
rows=[]
for i in range(height):
    print("\nRow " + str(i+1))
    columns = []
    for j in range(length):
        columns.append(float(input("Enter number: ")))
    rows.append(columns)
irows=[]
totalSum = 0
for i in rows:
    for j in i:
        totalSum += j
for iInd, i in enumerate(rows):
    icolumns=[]
    rowSum = 0
    for j in i:
        rowSum += j
    for jInd, j in enumerate(i):
        columnSum = 0
        for item in range(len(rows)):
            columnSum+=rows[item][jInd]
        icolumns.append((columnSum*rowSum)/totalSum)
    irows.append(icolumns)
chisquared = 0
for i in range(height):
    for j in range(length):
        chisquared+=(((rows[i][j]-irows[i][j])**2)/irows[i][j])
print()
sig = float(input("What is the level of significance? "))
chisquaredalpha = scipy.stats.chi2.ppf(1-sig, (height-1)*(length-1))
print()
for i in irows:
    for j in i:
        print(round(j, 7), end=", ")
    print()
print()
print("Chi squared is: " + str(chisquared))
print("Chi squared alpha is: " + str(chisquaredalpha))
print()
if chisquared >= chisquaredalpha:
    print("Reject H0")
else:
    print("Fail to reject H0")