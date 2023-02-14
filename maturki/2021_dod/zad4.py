def main():
    with open('dane/przyklad.txt', 'r') as dane:
        arr = [x for x in dane.read().strip().split("\n")]
    zad1(arr)


def zad1(arr: list):
    result = 0
    for line in arr:
        for char in line:
            if char.isnumeric():
                result += 1
    print(f'zad 4.1: {result}')


if __name__ == '__main__':
    main()
