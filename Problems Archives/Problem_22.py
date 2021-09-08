import os

def tri_namestxt():
    f = open("p022_names.txt", "r")
    names = f.read()
    names = names.split(",")
    names = sorted(names)
    total = 0
    for i in range(len(names)):
        names[i] = names[i].replace("\"", "")
        names[i] = names[i].replace("\n", "")
        names[i] = names[i].replace(" ", "")
        names[i] = names[i].lower()
        score = 0
        for j in range(len(names[i])):
            score += (ord(names[i][j]) - 96)
        score = score * (i+1)
        total += score
    print(total)

def main():
    

if __name__ == "__main__":
    print("Problem 21")
    
    