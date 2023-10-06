'''
Problem 6: Sum Square Difference

The sum of the squares of the first ten natural numbers is,

                                    1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is,

                                (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_square_diff(limit):
    """
    Calculates the difference between the square of the sum of numbers from 1 to the given limit and the sum of the squares of those numbers.

    Args:
        limit (int): The upper limit of the range of numbers to be considered.

    Returns:
        int: The difference between the square of the sum and the sum of squares.

    Example:
        result = sum_square_diff(10)
        print(result)  # Output: 2640
    """
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Limit must be a positive integer.")
    try:
        sum_of_squares = 0
        square_of_sum = 0
        for i in range(1, limit + 1):
            # Calculate the sum of squares
            sum_of_squares += i**2
            # Calculate the sum of numbers
            square_of_sum += i
        # Calculate the difference between the square of the sum and the sum of squares
        return square_of_sum**2 - sum_of_squares
    except TypeError:
        return "Invalid input: limit must be an integer."

print("The difference between the sum of squares of the first 100 natural numers and the square of the sum is: ")
print(sum_square_diff(100))

# -------------------- Unit Testing -------------------- 

# Test with limit = 1
result = sum_square_diff(1)
assert result == 0

# Test with limit = 10
result = sum_square_diff(10)
assert result == 2640
