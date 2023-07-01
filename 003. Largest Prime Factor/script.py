'''
Problem 3: Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

from math import floor

def is_prime(number):

    if number < 1:
        return False
    
    for i in range(2, floor(number / 2)):
        if not number % i:
            return False
        
    return True

def prime_factors(number):

    for i in range(2, floor(number / 2)):
        if (not number % i) and (is_prime(i)):
            print(i)

    return prime_factors

def solution(number):
    print(max(prime_factors(number)))

solution(600851475143)