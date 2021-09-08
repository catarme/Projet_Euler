
def Is_divisible(n):
    for i in range(19):
        if n%(i+1) != 0:
            return False
    return True

if __name__ == '__main__':
    iteration = 1
    while Is_divisible(iteration) == False:
        iteration += 1

    print(iteration)
