def main():
    with open("dane/binarne.txt") as dane:
        arr = [x for x in dane.read().strip().split("\n")]
    # print(arr)
    zad1(arr)
    zad2(arr)
    zad3(arr)


def zad1(arr):
    result = 0
    longest_word = ""
    for el in arr:
        if is_two_cycled(el):
            result += 1
            if len(el) > len(longest_word):
                longest_word = el
    print(f'zad 4.1: {result}, longest word: {longest_word}, length: {len(longest_word)}')


def zad2(arr):
    shortest_word_len = float('+inf')
    result = 0
    for el in arr:
        if not is_valid_BCD(el):
            result += 1
            if len(el) < shortest_word_len:
                shortest_word_len = len(el)

    print(f'zad 4.2: {result}, shortest word: {shortest_word_len}')


def zad3(arr):
    biggest_number = 0
    for el in arr:
        n = int(el, base=2)
        if n <= 65535:
            if n > biggest_number:
                biggest_number = n
    print(f'zad 4.3: {bin(biggest_number)}, {biggest_number}')


def is_valid_BCD(word):
    for number in divide_word(word):
        if int(number, base=2) > 9:
            return False
    return True


def divide_word(word):
    divided = []
    for i in range(0, len(word), 4):
        number = word[i:i+4]
        divided.append(number)
    return divided


def is_two_cycled(word):
    return word[len(word) // 2:] == word[:len(word) // 2]


if __name__ == '__main__':
    main()
