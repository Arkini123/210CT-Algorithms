def count (x):
    i = 5
    zeros = 0
    while x / i >= 1:
        zeros += x // i
        i *= 5
    return zeros

x = int(input(" Enter Factorail Number "))

print(count(x))
