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