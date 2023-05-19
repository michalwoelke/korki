def main():
    with open('dane/kody.txt', 'r') as kody, open('dane/cyfra_kodkreskowy.txt', 'r') as cyfry:
        arr = [x for x in kody.read().strip().split('\n')]
        arr2 = [x for x in cyfry.read().strip().split('\n')]
    arr3 = []
    for el in arr2[1:]:
        arr3.append(el[2:])
    zad1(arr)
    zad2(arr, arr3)
    zad3(arr, arr3)


def zad1(arr):
    result = []
    for el in arr:
        even_sum = 0
        odd_sum = 0
        for i in range(len(el)):
            index = len(el) - 1 - i
            if index % 2 == 0:
                even_sum += int(el[index])
            else:
                odd_sum += int(el[index])
        result.append([even_sum, odd_sum])
    print(f'Zad 1: {result}')


def zad2(arr, kody):
    result = []
    for n in arr:
        result.append([control_number(n), kody[control_number(n)]])
    print(f'Zad 2: {result}')


def zad3(arr, kody):
    result = []
    for n in arr:
        result.append(encode(n, kody))
    print(f'Zad 3: {result}')


def control_number(number):
    even_sum = 0
    odd_sum = 0
    for i in range(len(number)):
        index = len(number) - 1 - i
        if index % 2 == 0:
            even_sum += int(number[i])
        else:
            odd_sum += int(number[i])
    return (10 - (3 * even_sum + odd_sum) % 10) % 10


def encode(number, kody):
    START = '11011010'
    END = '11010110'
    result = START
    for n in number:
        result += kody[int(n)]
    return result + kody[control_number(number)] + END


if __name__ == '__main__':
    main()
