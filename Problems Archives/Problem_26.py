
if __name__ == "__main__":
    sequence = 0
    i = 1000
    while i > 1:
        if sequence >= i:
            break
        foundRemainders = []
        value = 1
        position = 0
        while foundRemainders[value] == 0 and value != 0:
            foundRemainders[value] = position
            value *= 10
            value %= i
            position += 1
        
        if position - foundRemainders[value] > sequence:
            sequence = position - foundRemainders[value]
        i -= 1
