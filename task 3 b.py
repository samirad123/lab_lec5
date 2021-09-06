def multiply(num):
    total = 1
    for x in num:
        total *= x
    return total
print(multiply((8, 2, 3, -1, 7)))