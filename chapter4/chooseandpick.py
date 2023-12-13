def factorial(val):
    if val == 0:
        return 1
    elif val == 1:
        return 1
    elif val > 1:
        return val * factorial(val-1)

porc = ""
left = 0
right = 0
while porc != "c":
    porc = input("P or C? ")
    if left != "q":
        left = float(input("What is the left value? "))
        right = float(input("What is the right value? "))
        if porc.lower() == "c":
            print((factorial(left))/(factorial(right)*(factorial(left-right))))
        else:
            print((factorial(left))/(factorial(left-right)))

