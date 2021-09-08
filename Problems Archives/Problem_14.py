
def is_even(x:int) -> bool:
    if x % 2 == 0:
        return True
    return False

if __name__ == "__main__":
    most = []
    most_temp = []
    
    for i in range(1, 1000000):
        most_temp.append(i)
        while i != 1:
            if is_even(i):
                i /= 2
            else:
                i = i * 3 + 1
            most_temp.append(i)
        if len(most_temp) > len(most):
            most = most_temp
        most_temp = []
    
    print(most[0])
