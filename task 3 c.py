def min3(num1,num2,num3):
    if ((num1 < num2) and (num1 < num3)):
        return num1
    elif ((num2 < num1) and (num2 < num3)):
        return num2
    else:
        return num3

print(min3(4,7,5))
print(min3(4,5,5))
print(min3(4,4,4))
print(min3(-2,-6,-100))
print(min3("Z","B","A"))