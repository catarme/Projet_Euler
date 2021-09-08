
def Multiples_of_3_or_5():
    L = []
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            L.append(i)
    result = 0
    for i in L:
        result+= i
    
    return result

if __name__ == "__main__":
    L = []
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            L.append(i)
    result = 0
    for i in L:
        result+= i

    print(result)