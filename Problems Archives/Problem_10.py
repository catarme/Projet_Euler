
def isprime(x:int) -> bool:
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    result = 0
    for i in range(1, 2_000_000):
        if isprime(i):
            result += i

    print(result)