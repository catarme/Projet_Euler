
def Is_palindrome(x):
    """
    regarde sur le nombre si il est palindrome
    """
    return str(x) == str(x)[::-1]

def Largest_palindrome_product():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    THEBIGEST = 0
    for i in range(999):
        for x in range(999):
            if Is_palindrome(i*x):
                THEBIGEST = max(THEBIGEST, i*x)
    return THEBIGEST

if __name__ == '__main__':
    print(Largest_palindrome_product())