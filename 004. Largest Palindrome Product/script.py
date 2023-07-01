'''
Problem 4: Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
from math import floor

def is_palindrome(number):

    str_number = str(number)
    length = len(str_number)

    for i in range(floor(length / 2)):
        if str_number[i] != str_number[length - (i + 1)]:
            return False
    
    return True

palindromes = []

a = 999
while a >= 100:

    b = a
    while b >= 100:

        if is_palindrome(a * b):
            palindromes.append(a * b)
        
        b -= 1

    a -= 1

print("The largest palendrome made from the product")
print("of two 3-digit numbers is", max(palindromes))