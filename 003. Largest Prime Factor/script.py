'''
Problem 3: Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

from math import isqrt

def is_prime(number):
    """
    Check if a number is prime.
    
    Args:
        number (int): The number to check.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number == 2 or number == 3:
        return True
    
    if number % 2 == 0:
        return False

    if number <= 1:
        return False

    for i in range(3, isqrt(number) + 1, 2):
        if number % i == 0:
            return False

    return True

def prime_factors(number):
    """
    Returns a list of prime factors of the given number.
    """
    factors = []
    for i in range(2, isqrt(number) + 1):
        if not number % i:
            if is_prime(i):
                factors.append(i)
    return factors

print('The largest prime factor of the number 600851475143 is: ')
print(prime_factors(600851475143)[-1])