tests = []
means = []
deviations = []
vals = []
val = ""
while val != "q":
    val = input("What is the test name? ")
    if val != "q":
        tests.append(val)
        means.append(float(input("What is the mean? ")))
        deviations.append(float(input("What is the deviation? ")))
        vals.append(float(input("What was the achieved value? ")))
results = []
for i in range(len(tests)):
    results.append((vals[i]-means[i])/deviations[i])
for i in range(len(tests)):
    print(tests[i] + " had a z-score of " + str(results[i]))