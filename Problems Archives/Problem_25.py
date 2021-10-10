
if __name__ == "__main__":
    first = 1
    second = 1
    tree = 0
    index = 2

    while (len(str(tree)) != 1000):
        tree = first + second
        first = second
        second = tree
        index += 1

    print(f"F{index} -> \t {tree}")