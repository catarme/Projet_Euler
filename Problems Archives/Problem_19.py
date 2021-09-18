import datetime

if __name__ == "__main__":

    resultat = 0
    for i in range(1901, 2001):
        for j in range(1, 13):
            if datetime.date(i, j, 1).weekday() == 6:
                resultat += 1
    print(resultat)
