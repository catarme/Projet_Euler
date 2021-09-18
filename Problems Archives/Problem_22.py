def name_score(name) -> int:
    score = 0
    for i in name:
        score += ord(i) - 64
    return score


if __name__ == "__main__":
    file = open("p022_names.txt", "r")
    names = list(eval(file.read()))
    file.close()
    names.sort()
    result = 0
    for i, name in enumerate(names):
        result += name_score(name) * (i + 1)
    print(result)
