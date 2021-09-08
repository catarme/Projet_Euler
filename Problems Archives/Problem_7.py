import sympy

if __name__ == '__main__':
    number = []
    iteration = 2
    while len(number) != 10_001:
        if sympy.isprime(iteration) == True:
            number.append(iteration)
        iteration += 1

    print(number[-1])