
def Sum_square_difference():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    res1 = 0
    for i in range(100):
        res1 += (i+1)**2
    res2 = 0
    for x in range(100):
        res2 += x+1
    res2 = res2**2
    return res2 - res1

if __name__ == "__main__":
    print(Sum_square_difference())
        