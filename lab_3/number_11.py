def gcd_rec(num1, num2):
    if num1 == 0:
        return num2
    return gcd_rec(num2 % num1, num1)

def gcd_while(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1 or num2