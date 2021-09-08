
if __name__ == "__main__":
    L = [1, 2]
    i1 = 1
    i2 = 2
    for i in range(4_000_000):
        i3 = i1 + i2
        i1 = i2
        i2 = i3
        i3str = str(i3)
        if i3str[-1] is [2, 4, 6, 8]:
            L.append(i3)   

    print(sum(L))