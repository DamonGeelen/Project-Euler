'''
Problem 4: Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

from math import floor

def is_palindrome(number):
    if isinstance(number, float):
        return False
    
    if isinstance(number, str):
        str_number = number
    elif isinstance(number, int):
        str_number = str(number)
    else:
        return False
    
    reversed_str = str_number[::-1]
    
    return str_number == reversed_str

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


# -------------------------- Unit Testing --------------------------

# Tests that the function returns True for a palindrome number
def test_palindrome_number(self):
    assert is_palindrome(121) == True

# Tests that the function returns False for a non-palindrome number
def test_non_palindrome_number(self):
    assert is_palindrome(123) == False

# Tests that the function returns True for a single digit number
def test_single_digit_number(self):
    assert is_palindrome(5) == True

# Tests that the function returns False for a negative number
def test_negative_number(self):
    assert is_palindrome(-121) == False

# Tests that the function returns True for zero
def test_zero(self):
    assert is_palindrome(0) == True

# Tests that the function returns True for a string that is a palindrome number
def test_string_input(self):
    assert is_palindrome('1221') == True

# Tests that the function returns False for a float input
def test_float_input(self):
    assert is_palindrome(12.21) == False

# Tests that the function returns True for a palindrome string input
def test_palindrome_string_input(self):
    assert is_palindrome('racecar') == True

# Tests that the function returns False for a non-palindrome string input
def test_non_palindrome_string_input(self):
    assert is_palindrome('hello') == False