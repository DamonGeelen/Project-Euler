"""
Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

multiples_of_three_and_five = []
i = 1
while i < 1000:
    if not (i % 3) or not (i % 5):
        multiples_of_three_and_five.append(i)
    i += 1

print(
    "The sum of all the multiples of 3 or 5 below 1000 is",
    str(sum(multiples_of_three_and_five)) + "."
)
