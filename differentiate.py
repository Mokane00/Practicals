import math
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
original_function = "f(x) = math.cos**3*(x^2+1)"
coeff = 1
power = 3
derivative = differentiate_monomial(coeff, power)
print(f"Derivative of {original_function} is f'(x) = {derivative}")