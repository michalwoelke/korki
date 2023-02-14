def main():
    with open("dane/liczby.txt", 'r') as dane:
        arr = [int(x) for x in dane.read().strip().split("\n")]
    zad1(arr)
    zad2(arr)
    zad3(arr)
    zad4_array(arr)
    zad4(arr)


def zad1(arr):
    result = []
    for n in arr:
        mirror_number = mirror(n)
        if mirror_number % 17 == 0:
            result.append(mirror_number)
    print(f'zad 4.1: {result}')


def mirror(n):
    ans = str(n)[::-1]
    return int(ans)


def zad2(arr):
    max_diff = 0
    max_diff_n = 0
    for n in arr:
        diff = abs(n - mirror(n))
        if diff > max_diff:
            max_diff = diff
            max_diff_n = n
    print(f'zad 4.2: max difference: {max_diff_n}, max difference number: {max_diff}')


def zad3(arr):
    result = []
    for n in arr:
        if isprime(n) and isprime(mirror(n)):
            result.append(n)
    print(f'zad 4.3: {result}')


def isprime(n):
    if n <= 2:
        return False
    for i in range(2, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            return False
    return True


def zad4_array(arr):
    counts = [0] * 10_000
    for num in arr:
        counts[num] += 1

    distinctive_nums = 0
    repeated_twice = 0
    repeated_three_times = 0

    for num in range(10_000):
        if counts[num] > 0:
            distinctive_nums += 1
            if counts[num] == 2:
                repeated_twice += 1
            elif counts[num] == 3:
                repeated_three_times += 1

    print(f'zad 4.4: {distinctive_nums} {repeated_twice} {repeated_three_times}')


def zad4(arr):
    repeated_twice = 0
    repeated_three_times = 0
    counts = {}  # short-hand for dict()
    for num in arr:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1

    for key in counts:
        if counts[key] == 2:
            repeated_twice += 1
        elif counts[key] == 3:
            repeated_three_times += 1
    print(f'zad 4.4: {len(counts)} {repeated_twice} {repeated_three_times}')


if __name__ == '__main__':
    main()
