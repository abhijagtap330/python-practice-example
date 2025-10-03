import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Example usage
num1 = 12
num2 = 15

result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")