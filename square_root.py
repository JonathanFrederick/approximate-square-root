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
