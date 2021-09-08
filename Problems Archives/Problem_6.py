

if __name__ == "__main__":
    res1 = 0
    for i in range(100):
        res1 += (i+1)**2
    res2 = 0
    for x in range(100):
        res2 += x+1
    res2 = res2**2

    print(res2 - res1)