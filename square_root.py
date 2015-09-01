"""A program that asks the user for a positive number and then outputs the approximated square root of the number."""
while True:
    try:
        num = float(input('Please input a number:  '))
        break
    except:
        print("ERROR: Input not a number")
        continue

#print(num)

def sqrt (num):
    """Approximates square root of parameter to 2 decimal places"""
    neg=""
    if num < 0:
        num = abs(num)
        neg = 'i'
    guess1 = 1
    guess2 = 0
    count = 0
    while round(guess1, 2) != round(guess2, 2):
        count += 1
        guess2 = guess1
        guess1 = (guess1 + num/guess1)/2
        print("This loop has iterated", count, "times and the current guess is", str(guess1)+".")
    return (str(round(guess1,2))+neg)

print("The square root of", num, "is", sqrt(num))
