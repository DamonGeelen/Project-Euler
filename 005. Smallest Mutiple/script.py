'''
Problem 5: Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to 20?
'''

def smallest_multiple(max_divisor):
    """
    Returns the smallest positive integer that is divisible by all numbers from 1 to max_divisor (inclusive).

    Args:
        max_divisor (int): The maximum divisor to consider.

    Returns:
        int: The smallest positive integer that is divisible by all numbers from 1 to max_divisor.
    """
    smallest_multiple = 1
    i = 1
    while i <= max_divisor:
        remainder = smallest_multiple % i
        if remainder == 0:
            i += 1
        else:
            smallest_multiple += 1
            i = 2
    return smallest_multiple

print('The smallest positive number is evenly divisible by each of the numbers from 1 to 20 is ')
print(smallest_multiple(20))

# -------------------------- Unit Testing --------------------------

# Test for known values
assert smallest_multiple(1) == 1
assert smallest_multiple(2) == 2
assert smallest_multiple(3) == 6
assert smallest_multiple(4) == 12
assert smallest_multiple(5) == 60
assert smallest_multiple(10) == 2520