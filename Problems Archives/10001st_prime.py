import sympy

def main():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    
    What is the 10 001st prime number?
    """
    number = []
    iteration = 2
    while len(number) != 10_001:
        if sympy.isprime(iteration) == True:
            number.append(iteration)
        iteration += 1
    return number[-1]

if __name__ == '__main__':
    print(main())