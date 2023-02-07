def main():
    with open('dane/sygnaly.txt', 'r') as dane:
        arr = [x for x in dane.read().strip().split('\n')]
    zad1(arr)
    zad2(arr)
    zad3_prev(arr)
    zad3(arr)


#  0 → 1
#  1 → 2
#  ...
#  39 → 40
#  79 → 80
def zad1(arr):
    word = ''
    # startujemy od 39 bo arr jest indeksowany od 0 a nie od 1 jak wiersze pliku 39 to 40 linijka
    for i in range(39, len(arr), 40):
        word += arr[i][9]
    print(f'zad 4.1: {word}')


def zad2(arr):
    current_word = ''
    max_diff_letters_count = 0
    for word in arr:
        current_diff_letters = len(set(word))
        if current_diff_letters > max_diff_letters_count:
            max_diff_letters_count = current_diff_letters
            current_word = word
    print(f'zad 4.2: {current_word} {max_diff_letters_count}')


def zad3_prev(arr):
    words = []
    for word in arr:
        is_ok = True
        for i in range(len(word)):
            for j in range(len(word)):
                if abs(ord(word[i]) - ord(word[j])) > 10:
                    is_ok = False
                    break
        if is_ok:
            words.append(word)
    print(f'zad 4.3: <uncomment to see :D>')
    print(len(words))
    # for word in words:
    #     print(word)


def zad3(arr):
    words = []
    for word in arr:
        # sorted_letters = sorted(set(word))  # O(nlogn)
        # first_letter = sorted_letters[0]
        # last_letter = sorted_letters[-1]
        # diff = ord(last_letter) - ord(first_letter)
        min_val = 1000
        max_val = 0
        for char in word:
            curr_val = ord(char)
            min_val = curr_val if curr_val < min_val else min_val
            max_val = curr_val if curr_val > max_val else max_val
        diff = max_val - min_val
        if diff <= 10:
            words.append(word)
    print(len(words))


if __name__ == '__main__':
    main()
