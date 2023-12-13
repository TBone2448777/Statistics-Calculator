def factorial(val):
    if val == 0:
        return 1
    elif val == 1:
        return 1
    elif val > 1:
        return val * factorial(val-1)
def choose(left, right):
    left = float(left)
    right = float(right)
    return (factorial(left))/(factorial(right)*(factorial(left-right)))
lowR = int(input("What is the lowest number? "))
highR = int(input("What is the highest number? "))
chosen = int(input("What is the target value? "))
numer = 0
denom = 0
for i in range(lowR, highR+1):
    denom += choose(highR, i)
    if i == chosen:
        numer += choose(highR, i)
print(numer/denom)