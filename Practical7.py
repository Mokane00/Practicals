

def triangle_area(base, height):
    """
    Calculate the area of a triangle.

    Parameters:
    base (float): The base of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    return 0.5 * base * height
  
print(triangle_area(12,15))  

def isDivisibleBy5(n):
    """
    Check if a number is divisible by 5.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if divisible by 5, False otherwise.
    """
    return n % 5 == 0
  
print(isDivisibleBy5(20))  

def middleNumber(a, b, c):
    """
    Find the middle number among three integers.

    Parameters:
    a (int): First integer.
    b (int): Second integer.
    c (int): Third integer.

    Returns:
    int: The middle number.
    """
    return sorted([a, b, c])[1]
  
print(middleNumber(20,3,40))  


def swapFirstLast(word):
    """
    Swap the first and last characters of a word.

    Parameters:
    word (str): The word to swap.

    Returns:
    str: The word with first and last characters swapped.
    """
    return word[-1] + word[1:-1] + word[0]
  
print(swapFirstLast("money"))

def decimal_to_binary(n):
    """
    Convert a number from base 10 to binary.

    Parameters:
    n (int): The number in base 10.

    Returns:
    str: The binary representation of the number.
    """
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary
  
print(decimal_to_binary(2))

def differentiate_monomial(coeff, power):
    """
    Differentiate a monomial using the power rule.

    Parameters:
    coeff (int): Coefficient of the monomial.
    power (int): Power of the monomial.

    Returns:
    str: The differentiated monomial in string format.
    """
    if power == 0:
        return "0"
    new_coeff = coeff * power
    new_power = power - 1
    return f"{new_coeff}x^{new_power}"

# Example usage:
original_function = "f(x) = 4x^3"
coeff = 4
power = 3
derivative = differentiate_monomial(coeff, power)
print(f"Derivative of {original_function} is f'(x) = {derivative}")

def longer_word(word1, word2):
    """
    Find the longer word between two words.

    Parameters:
    word1 (str): First word.
    word2 (str): Second word.

    Returns:
    str: The longer word or "equal" if both words are of equal length.
    """
    if len(word1) > len(word2):
        return word1
    elif len(word2) > len(word1):
        return word2
    else:
        return "equal"
      
print(longer_word("Man","Women")) 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Thou shall not divide by zero!!!"
    return a // b

print("*************************** **** Arithmetic Operations **** ***************************")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Integer division")

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
choice = int(input("Enter choice of arithmetic operation to perform on two entered integers: "))

if choice == 1:
    print("Result:", add(a, b))
elif choice == 2:
    print("Result:", subtract(a, b))
elif choice == 3:
    print("Result:", multiply(a, b))
elif choice == 4:
    print("Result:", divide(a, b))
    
    
    