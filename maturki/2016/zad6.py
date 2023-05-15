def main():
    with open("dane/dane_6_1.txt") as dane1:
        arr1 = [x for x in dane1.read().strip().split("\n")]
    with open("dane/dane_6_2.txt") as dane2:
        arr2 = [[y for y in x.split(" ")] for x in dane2.read().strip().split("\n")]
    for el in arr2:
        if el[1].isnumeric():
            el[1] = int(el[1])
    with open("dane/dane_6_3.txt") as dane3:
        arr3 = [[y for y in x.split(" ")] for x in dane3.read().strip().split("\n")]
    # print(arr2)
    zad2(arr2)
    # zad2(fix_arr2(arr2))
    # print(zad3(arr3))


def zad1(arr):
    k = 107
    result = []
    for word in arr:
        result.append(encrypt(word, k))
    print(f'zad 6.1: {result}')
    print(f'writing... {write_to_file("wyniki_6_1.txt", result)}')


def zad2(arr):
    result = []
    for el in arr:
        print(el)
        word = el[0]
        k = el[1]
        decrypted = decrypt(word, k)
        result.append(decrypted)
    print(f'zad 6.2: {result}')
    print(f'writing... {write_to_file("wyniki_6_2.txt", result)}')


def fix_arr2(arr2):
    fixed = []
    for el in arr2:
        word = el[0]
        if el[1] == '':
            el = [word, 0]
        fixed.append(el)
    return fixed


def write_to_file(filename, content):
    file = open(filename, 'w')
    for el in content:
        file.write(el + "\n")
    file.close()
    return "Done!"


def decrypt(word, k):
    k *= -1
    return encrypt(word, k)


def encrypt(word: str, k: int):
    result = ""
    word = word.upper().strip().replace(" ", "")
    for char in word:
        result += chr((ord(char) + k - 65) % 26 + 65)
    return result


if __name__ == '__main__':
    main()
    # ord("A") <-- 65
    # chr(65) <-- "A"
