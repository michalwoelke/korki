def main():
    with open("dane/dane1.txt") as dane1, open("dane/dane2.txt") as dane2:
        arr1 = [[int(y) for y in x.split(" ")] for x in dane1.read().strip().split("\n")]
        arr2 = [[int(y) for y in x.split(" ")] for x in dane2.read().strip().split("\n")]
    zad1(arr1, arr2)
    zad2(arr1, arr2)
    zad3(arr1, arr2)
    zad4(arr1, arr2)


def zad1(arr1, arr2):
    result = 0
    for i in range(len(arr1)):
        if arr1[i][-1] == arr2[i][-1]:
            result += 1
    print(f'zad 4.1: {result}')


def zad2(arr1, arr2):
    result = 0
    for i in range(len(arr1)):
        line_1 = arr1[i]
        line_2 = arr2[i]
        if count_even_and_odd(line_1) == [5, 5] and count_even_and_odd(line_2) == [5, 5]:
            result += 1
    print(f'zad 4.2: {result}')


def zad3(arr1, arr2):
    lines = []
    for i in range(len(arr1)):
        if set(arr1[i]) == set(arr2[i]):
            lines.append(i + 1)
    print(f'zad 4.3: Pary ciągów: {len(lines)}, numery wierszy: {lines}')


def zad4(arr1, arr2):
    results = []
    for i in range(len(arr1)):
        results.append(merge(arr1[i], arr2[i]))
    write_to_file('wynik4_4.txt', results)


def merge(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] <= arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
        else:
            result.append(arr2[p2])
            p2 += 1
    if p1 < len(arr1):
        result.extend(arr1[p1:])
    else:
        result.extend(arr2[p2:])
    return result


def write_to_file(filename, content: list):
    output_file = open(filename, 'w')
    for elements in content:
        line = ''
        for el in elements:
            line += str(el) + ' '
        output_file.write(line.strip() + '\n')
    output_file.close()
    print(f'zad 4.4: saved in file {filename}')


def count_even_and_odd(arr):
    result = [0, 0]
    for n in arr:
        if n % 2:
            result[0] += 1
        else:
            result[1] += 1
    return result


if __name__ == '__main__':
    main()
