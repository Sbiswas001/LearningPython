import math

num = int(input("Enter a number: "))


def is_even(number):
    return number % 2 == 0


def digit_count(number):
    return len(str(number))


def digit_sum(number):
    return sum(int(digit) for digit in str(number))


def digit_product(number):
    product = 1
    num = number
    while num != 0:
        digit = num % 10
        product *= digit
        num = num // 10  # Use integer division for Python 3
    return product


def reverse(number):
    return str(number)[::-1]


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def is_perfect_square(number):
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def decimal_to_binary(number):
    return bin(number)[2:]


def decimal_to_octal(number):
    return oct(number)[2:]


def decimal_to_hexadecimal(number):
    return hex(number)[2:].upper()


result = ""
result += "Number is Even\n" if is_even(num) else "Number is Odd\n"
result += f"Number of digits is {digit_count(num)}\n"
result += f"Sum of digits is {digit_sum(num)}\n"
result += f"Product of digits is {digit_product(num)}\n"
result += f"Reverse of number is {reverse(num)}\n"
result += f"Binary representation is {decimal_to_binary(num)}\n"
result += f"Octal representation is {decimal_to_octal(num)}\n"
result += f"Hexadecimal representation is {decimal_to_hexadecimal(num)}"

print(result)
