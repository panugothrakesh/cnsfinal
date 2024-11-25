def euclidean_algorithm(a, b):
    """Calculates the GCD of two numbers using the Euclidean Algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclidean_algorithm(a, b):
    """Calculates the GCD and coefficients x, y such that ax + by = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

a = 56
b = 98

gcd = euclidean_algorithm(a, b)
print(f"GCD of {a} and {b} using Euclidean Algorithm is {gcd}")

gcd, x, y = extended_euclidean_algorithm(a, b)
print(f"GCD of {a} and {b} using Extended Euclidean Algorithm is {gcd}")
print(f"Coefficients: x = {x}, y = {y}")