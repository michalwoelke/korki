def main():
    with open("dane/liczby.txt") as dane:
        arr = [x for x in dane.read().strip().split("\n")]
    zad1(arr)
    zad2(arr)
    zad3(arr)
    zad4(arr)
    zad5(arr)


def zad1(arr):
    result = sum(1 if el[-1] == '8' else 0 for el in arr)
    print(f'zad 6.1: {result}')

    # result = 0
    # for el in arr:
    #     if int(el[-1]) == 8:
    #         result += 1
    # print(f'zad 6.1: {result}')


def zad2(arr):
    result = 0
    for el in arr:
        if int(el[-1]) == 4 and '0' not in el:
            result += 1
    print(f'zad 6.2: {result}')


def zad3(arr):
    result = 0
    for el in arr:
        if int(el[-1]) == 2 and el[-2] == '0':
            result += 1
    print(f'zad 6.3: {result}')


def zad4(arr):
    result = 0
    for el in arr:
        if el[-1] == '8':
            result += int(el[:-1], base=8)
    print(f'zad 6.4: {result}')


def zad5(arr):
    smallest_num = arr[0]
    biggest_num = arr[0]
    for el in arr:
        if value_from_code(el) > value_from_code(biggest_num):
            biggest_num = el
        elif value_from_code(el) < value_from_code(smallest_num):
            smallest_num = el
    print(f'zad 6.5:')
    print(f'\tthe smallest: {smallest_num}, {value_from_code(smallest_num)}')
    print(f'\tthe biggest: {biggest_num}, {value_from_code(biggest_num)}')


def value_from_code(code):
    return int(code[:-1], base=int(code[-1]))


if __name__ == '__main__':
    main()
