def average_list(n):
    sum = 0
    for i in n:
        sum += i
    return sum/len(n)
print(average_list([1,2,3]))