
def name_score(name):
    score = 0
    for i in name:
        score += ord(i) - 64
    return score

if __name__ == "__main__":
    fichier = open("p022_names.txt", "r")
    names = list(eval(fichier.read()))
    fichier.close()
    names.sort()
    resultat = 0
    for i, name in enumerate(names):
        resultat += name_score(name)*(i+1)
    print(resultat)