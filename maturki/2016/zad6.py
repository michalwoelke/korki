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
    zad1(arr1)
    zad2(fix_arr2(arr2))
    zad3(arr3)


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
        word = el[0]
        k = el[1]
        decrypted = decrypt(word, k)
        result.append(decrypted)
    print(f'zad 6.2: {result}')
    print(f'writing... {write_to_file("wyniki_6_2.txt", result)}')


def zad3(arr3):
    result = []
    for pair in arr3:
        if not is_valid_encryption(pair[0], pair[1]):
            result.append(pair[0])
    print(f'zad 6.3: {result}')
    print(f'writing... {write_to_file("wyniki_6_3.txt", result)}')


def is_valid_encryption(word, encrypted):
    k = calculate_k(word[0], encrypted[0])
    for i in range(1, len(word)):
        if calculate_k(word[i], encrypted[i]) != k:
            return False
    return True


def calculate_k(l1, l2):
    return (ord(l1) - ord(l2)) % 26


def fix_arr2(arr2):
    fixed = []
    for el in arr2:
        word = el[0]
        if el[1] == '':
            el = [word, 0]
        fixed.append(el)
    return fixed


def write_to_file(filename, content):
    with open(filename, 'w') as file:
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
