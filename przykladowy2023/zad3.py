def podpunkt_2():
    print(potega(2, 5, 7))
    print(potega(3, 3, 11))
    print(potega(5, 2, 31))
    print(potega(2, 6, 59))
    print(potega(9, 2, 80))


# ZADANIE 3.2
def potega(a, x, M):
    if M == 1:
        return 0
    if x == 0:
        return 1
    if x % 2 == 0:
        w = potega(a, x / 2, M)
        return w * w % M
    if x % 2 == 1:
        w = potega(a, (x - 1) / 2, M)
        return a * w * w % M


# ZADANIE 3.3 - 3.5
def wczytaj_dane():
    file = open('Dane_2203/liczby.txt', 'r')
    lines = file.read().strip().split('\n')
    file.close()
    dane = [[int(x) for x in x.split(' ')] for x in lines]
    return dane


def zad_3_3():
    prime_ms = 0
    for arr in wczytaj_dane():
        if isprime(arr[0]):
            prime_ms += 1
    print(f'zad 3.3: {prime_ms}')


def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def zad_3_4():
    ans = 0
    for arr in wczytaj_dane():
        if nwd(arr[0], arr[1]) == 1:
            ans += 1
    print(f'zad 3.4: {ans}')


def nwd(a, b):
    return nwd(b, a % b) if b else a


def zad_3_5():
    ans = 0
    for arr in wczytaj_dane():
        if check_x(arr[0], arr[1], arr[2]):
            ans += 1
    print(f'zad 3.5: {ans}')


def check_x(M, a, b):
    for x in range(0, M):
        if potega(a, x, M) == b:
            return True
    return False


if __name__ == '__main__':
    zad_3_3()
    zad_3_4()
    zad_3_5()
