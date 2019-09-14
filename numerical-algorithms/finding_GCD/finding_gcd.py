
def find_gcd(number1, number2):
    while number2 != 0:
        remainder = number1 % number2
        number1 = number2
        number2 = remainder
    return number1


print(find_gcd(4851, 3003))
