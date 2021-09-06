#1
def permutations(n,r):
    return (factorial(n)/(factorial(n-r)))
#2
def combinations(n,r):
    return(factorial(n) / (factorial(r) * (factorial(n-r))))
#3
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
#4
def armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return temp == sum
#5
def reverse(n):
    return int(str(n)[::-1])


