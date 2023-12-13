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
def bprob(trials, success, probability):
    return choose(trials, success)*(probability**success)*((1-probability)**(trials-success))
success = int(input("What is the number of successes? "))
trials = int(input("What is the number of trials? "))
probability = float(input("What is the probability of success? "))
special = input("Above or below a value? ")
# uses or equal to
if special.lower() == "above":
    total = 0
    for i in range(success, trials+1):
        total+=bprob(trials, i, probability)
    print(total)
elif special.lower() == "below":
    total = 0
    for i in range(0, success+1):
        total+=bprob(trials, i, probability)
    print(total)
else:
    print(bprob(trials, success, probability))