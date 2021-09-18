
if __name__ == "__main__":
    result = 1
    for i in range(100):
        result *= i + 1
    result = str(result)
    res = 0
    for i in result:
        res += int(i)
    
    print("100! = ", res, "\n")
