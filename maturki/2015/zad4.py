def main():
    with open('dane/liczby.txt', 'r') as dane:
        arr = [x for x in dane.read().strip().split('\n')]
    # arr = ['101011010011001100000', '10001001', '100100', '101010010101011011000', '100011']
    zad1(arr)
    zad2(arr)
    zad3(arr)


def zad1(numbers):
    result = 0
    for n in numbers:
        zeros = len([1 for digit in n if digit == '0'])
        ones = len(n) - zeros
        # for digit in n:
        #     if digit == '0':
        #         zeros += 1
        #     else:
        #         ones += 1
        if zeros > ones:
            result += 1
    print(f'Zad 1: {result}')


def zad2(arr):
    by_two = len([1 for number in arr if number.endswith('0')])
    by_eight = len([1 for number in arr if number.endswith('000')])
    # for n in arr:
    #     if n[-1] == '0':
    #         by_two += 1
    #         if n[-3:-1] == '00':
    #             by_eight += 1
    print(f'Zad 2:\npodzielne przez 2: {by_two}\npodzielne przez 8: {by_eight}')


def zad3(arr):
    greatest_index = 0
    smallest_index = 0
    for i in range(len(arr)):
        if compare(arr[i], arr[greatest_index]) > 0:
            greatest_index = i
        if compare(arr[i], arr[smallest_index]) < 0:
            smallest_index = i
    print(
        f'Zad 3: najmniejsza liczba w wierszu: {smallest_index + 1}, największa liczba w wierszu: {greatest_index + 1}')


def compare(num1, num2):
    if len(num1) == len(num2):
        for i in range(len(num1)):
            if num1[i] == num2[i]:
                continue
            return int(num1[i]) - int(num2[i])
            # if num1[i] == '0' and num2[i] != '0':
            #     return -1
            # elif num1[i] != '0' and num2[i] == '0':
            #     return 1
        return 0
    else:
        return len(num1) - len(num2)


if __name__ == '__main__':
    main()
