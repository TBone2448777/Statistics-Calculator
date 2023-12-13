import math
lst = []
total = 0
mean = 0
median = 0
rng = 0
pvariance = 0
pdeviation = 0
svariance = 0
sdeviation = 0
pcoeffvariation = 0
scoeffvariation = 0
occurrences= {}
mode = ""
iqr = 0

def calcmedian(mlst, Q = None):
    mcount = len(mlst)
    midindex = (mcount+1)/2
    if (mcount+1)%2 == 0:
        median = mlst[int((mcount+1)/2-1)]
        if Q == "Q":
            return median, mlst[:int(midindex-1)], mlst[int(midindex):]
        else:
            return median
    else:
        median = (mlst[int((mcount+1)/2-1)] + mlst[int((mcount+1)/2-1)+1])/2
        if Q == "Q":
            return median, mlst[:int(midindex)], mlst[int(midindex):]
        else:
            return median

def percentile(insert):
    percentileIndex = count*(insert/100)
    percentileIndex = math.ceil(percentileIndex)
    return lst[percentileIndex-1]

# Generate the list from user input
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
lst.sort()

# Get total value of list
for i in lst:
    total += i

# Get Length of List
count = len(lst)

# Performs a number of calculations
if len(lst) > 1:

    # Get Mean
    mean = total/count

    # Generate Median
    median, q1lst, q3lst = calcmedian(lst, "Q")

    # Generate Qs
    q1 = calcmedian(q1lst)
    q3 = calcmedian(q3lst)

    # Get range
    rng = lst[-1]-lst[0]

    # Get population variance
    for i in lst:
        pvariance += (i-mean)**2
    pvariance /= count

    # Get population standard deviation
    pdeviation = math.sqrt(pvariance)

    # Get sample variance
    for i in lst:
        svariance += (i-mean)**2
    svariance /= (count-1)

    # Get sample standard deviation
    sdeviation = math.sqrt(svariance)

    # Get population coefficienct of variation
    pcoeffvariation = pdeviation/mean

    # Get sample coefficienct of variation
    scoeffvariation = sdeviation/mean

    # Find mode
    for i in lst:
        if i not in occurrences:
            occurrences[i] = 1
        else:
            occurrences[i] = occurrences[i]+1
    mostappear = 0
    for i in occurrences:
        if occurrences[i] > mostappear:
            mostappear = occurrences[i]
    for i in occurrences:
        if occurrences[i] == mostappear:
            mode += str(i) + ", "
    mode += "with " + str(mostappear) + " occurences. "

    # Find IQR
    iqrindex = (count)/4
    if (count+1)%2 == 0:
        iqr = lst[int((count+1)/2-1)]
    else:
        iqr = (lst[int((count+1)/2-1)] + lst[int((count+1)/2-1)+1])/2

    # User input to get needed values
    while True:
        ans = input("What variable would you like? ")
        if ans == "q":
            break
        else:
            try:
                x = eval(ans)
                print(x)
            except NameError:
                print("Variable not found. Try again.")