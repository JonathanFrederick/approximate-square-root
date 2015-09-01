"""A program that asks the user for a positive number and then outputs the approximated square root of the number."""
while True:
    try:
        num = float(input('Please input a positive number:  '))
        if num < 0:
            num/0
        break
    except:
        continue


print(num)

def sqrt (num):
    """Approximates square root of parameter to 2 decimal places"""
    guess1 = 1
    guess2 = 0
    while round(guess1, 2) != round(guess2, 2):
        guess2 = guess1
        guess1 = (guess1 + num/guess1)/2
    return guess1

print("The square root of", num, "is", round(sqrt(num),2))
