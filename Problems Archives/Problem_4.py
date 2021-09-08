
def Is_palindrome(x):
    return str(x) == str(x)[::-1]

if __name__ == '__main__':
    THEBIGEST = 0
    for i in range(999):
        for x in range(999):
            if Is_palindrome(i*x):
                THEBIGEST = max(THEBIGEST, i*x)

    print(THEBIGEST)