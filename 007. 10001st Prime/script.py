'''
Problem 7: 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
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

def nth_prime(n):
    """
    Returns the nth prime number.
    
    Parameters:
    n (int): The position of the prime number to be returned.
    
    Returns:
    int: The nth prime number.
    
    Raises:
    ValueError: If n is less than or equal to 0.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    if n == 1:
        return 2
    
    i = 3
    count = 1
    while count < n:
        if is_prime(i):
            count += 1
        i += 2
    
    return i - 2

print('The 10,001st prime number is: ')
print(nth_prime(10001))

# ---------------------------------- Unit Testing ----------------------------------

# Checks if the function correctly identifies the number 0 as a non-prime number.
assert is_prime(0) == False

# Checks if the function correctly identifies the number 2 as a prime number.
assert is_prime(2) == True

# Checks if the function correctly identifies the number 3 as a prime number.
assert is_prime(3) == True

# Checks if the function correctly identifies the number 4 as a non-prime number.
assert is_prime(4) == False

# Checks if the function correctly identifies the number 5 as a prime number.
assert is_prime(5) == True

# Checks if the funciton correctly identifies a negative number as non-prime.
assert is_prime(-1) == False
assert is_prime(-2) == False
assert is_prime(-3) == False

# returns 2 when n=1
assert nth_prime(1) == 2

# returns 3 when n is 2
assert nth_prime(2) == 3

# returns 5 when n is 3
assert nth_prime(6) == 13