
def Is_palindrome(value: int) -> bool:
    return str(value) == str(value)[::-1]

if __name__ == '__main__':
    bigest = 0
    for i in range(999):
        for x in range(999):
            if Is_palindrome(i*x):
                bigest = max(bigest, i * x)

    print(bigest)