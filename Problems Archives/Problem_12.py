def divisors(nb, extremum = False):
    divisor = []
    inf = 1 if extremum else 2
    for i in range(inf, int(nb ** 0.5) + 1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisor.append(i)
                if q > i:
                    divisor.append(nb // i)
    return divisor


if __name__ == "__main__":
    triangle = 3
    i = 2
    nb_divisors = 0
    while nb_divisors < 500:
        i += 1
        triangle += i
        nb_divisors = len(divisors(triangle, True))
    print(triangle)
