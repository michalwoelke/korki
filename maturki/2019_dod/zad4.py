def main():
    with open("dane/pierwsze.txt", "r") as primaries_file, open("dane/liczby.txt", "r") as numbers_file:
        primaries_array = [int(x) for x in primaries_file.read().strip().split("\n")]
        numbers_array = [int(x) for x in numbers_file.read().strip().split("\n")]
    zad1(numbers_array)
    zad2(primaries_array)
    zad3(primaries_array)


def zad1(arr):
    result = []
    for n in arr:
        if 100 <= n <= 5000 and is_prime(n):
            result.append(n)
    print(f'zad 4.1: {result}')


def zad2(arr):
    result = []
    for n in arr:
        if is_prime(mirror_number(n)):
            result.append(n)
    print(f'zad 4.2: {result}')


def zad3(arr):
    result = 0
    for n in arr:
        if wage_of_number(n) == 1:
            result += 1
    print(f'zad 4.3: {result}')


def wage_of_number(n):
    if n < 10:
        return n
    return wage_of_number(sum_of_digits(n))


def mirror_number(n):
    return int(str(n)[::-1])


def sum_of_digits(n):
    # return sum(int(digit) for digit in str(n))
    result = 0
    for digit in str(n):
        result += int(digit)
    return result


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
