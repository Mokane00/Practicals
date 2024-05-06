#a) Sum of Natural Numbers


def sum_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural_numbers(n - 1)

# Example usage:
result = sum_natural_numbers(5)
print("Sum of natural numbers up to 5:", result)


#b) Product of a Number with 4


def multiply_by_4(num):
    if num == 0:
        return 0
    else:
        return 4 + multiply_by_4(num - 1)

# Example usage:
result = multiply_by_4(5)
print("Product of 3 with 4:", result)


#c) Recursive Division


def recursive_division(dividend, divisor):
    if dividend < divisor:
        return 0
    else:
        return 1 + recursive_division(dividend - divisor, divisor)

# Example usage:
result = recursive_division(10, 3)
print("10 divided by 3 using recursion:", result)


#d) Predicate Function for Even Numbers


def is_even(num):
    if num == 0:
        return True
    elif num == 1:
        return False
    else:
        return is_even(num - 2)

# Example usage:
result = is_even(6)
print("Is 6 even?", result)


#e) Power Calculation using Recursion


def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

# Example usage:
result = power(2, 3)
print("2 raised to the power of 3:", result)


#f) Binomial Coefficient Calculation


def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

# Example usage:
result = binomial_coefficient(5, 2)
print("Binomial coefficient C(5, 2):", result)


#g) Sum of a List of Numbers


def sum_list_recursive(nums):
    if not nums:
        return 0
    else:
        return nums[0] + sum_list_recursive(nums[1:])

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = sum_list_recursive(numbers)
print("Sum of numbers in the list:", result)


#h) Number of Digits in a Positive Integer


def count_digits_recursive(num):
    if num < 10:
        return 1
    else:
        return 1 + count_digits_recursive(num // 10)

# Example usage:
result = count_digits_recursive(12345)
print("Number of digits in 12345:", result)


#i) Geometric Sum Calculation


def geometric_sum(n):
    if n == 0:
        return 1
    else:
        return 1 / (2 ** n) + geometric_sum(n - 1)

# Example usage:
result = geometric_sum(3)
print("Geometric sum of 3:", result)


#j) Reverse a String using Recursion


def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

# Example usage:
result = reverse_string("hello")
print("Reversed string:", result)


#k) Hailstone Sequence


def hailstone(n):
    print(n, end=" ")
    if n == 1:
        return
    elif n % 2 == 0:
        hailstone(n // 2)
    else:
        hailstone(3 * n + 1)

# Example usage:
hailstone(5)


#l) Sum of Digits until Single Digit


def sum_digits_until_single(num):
    if num < 10:
        return num
    else:
        return sum_digits_until_single(sum(int(digit) for digit in str(num)))

# Example usage:
result = sum_digits_until_single(1996)
print("Sum of digits until single digit:", result)
