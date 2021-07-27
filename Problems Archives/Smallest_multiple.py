
def estdivisible(n):
    for i in range(19):
        if n%(i+1) != 0:
            return False
    return True

def main():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    iteration = 1
    while estdivisible(iteration) == False:
        iteration += 1
    return iteration
    
if __name__ == '__main__':
    print(main())