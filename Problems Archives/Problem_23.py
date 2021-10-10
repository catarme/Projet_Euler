
def divisors(nb: int, extremum: bool = False) -> list:
    divisors = []
    inf = 1 if extremum else 2
    for i in range(inf, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(nb//i)
    return divisors


def is_abundant(n: int) -> bool:
    return sum(divisors(n))+1 > n


if __name__ == '__main__':

    abundants = [i for i in range(2, 28124) if is_abundant(i)]
    sommes = {}
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            somme = abundants[i] + abundants[j]
            if somme > 28123:
                break
            sommes[somme] = 1

    resultat = (28123*28124)//2 - sum(sommes.keys())
    print(resultat)
