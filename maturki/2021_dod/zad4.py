def main():
    with open('dane/napisy.txt', 'r') as dane:
        arr = [x for x in dane.read().strip().split("\n")]
    zad1(arr)
    zad2(arr)
    zad3(arr)
    zad4(arr)


def zad1(arr: list):
    result = 0
    for line in arr:
        for char in line:
            if char.isnumeric():
                result += 1
    print(f'zad 4.1: {result}')


def zad2(arr):
    result = ''
    counter = 0
    for i in range(19, len(arr), 20):
        result += arr[i][counter]
        counter += 1
    print(f'zad 4.2: {result}')


def zad3(arr):
    result = ''
    palindromes = []
    for word in arr:
        if can_be_palindrome(word):
            palindromes.append(turn_into_palindrome(word))
    for palindrome in palindromes:
        result += palindrome[len(palindrome) // 2]
    print(f'zad 4.3: {result}')


def zad4(arr: list):
    pairs = get_all_number_pairs(arr)
    nums = get_valid_ascii_nums(pairs)
    result = ''
    for x in nums:
        result += chr(x)
        # check for end (XXX)
        if result[-3:] == 'XXX':
            break
    print(f'zad 4.4: {result}')


def get_valid_ascii_nums(pairs):
    nums = []
    for n in pairs:
        num = int(n)
        if 65 <= num <= 90:
            nums.append(num)
    return nums


def get_all_number_pairs(arr):
    pairs = []
    for line in arr:
        line_numbers = get_numbers_str_in_line(line)
        line_pairs = [line_numbers[i - 1] + line_numbers[i] for i in range(1, len(line_numbers), 2)]
        pairs += line_pairs
        # if len(line_numbers) % 2 != 0:
        #     line_numbers = line_numbers[:-1]
        # pair = []
        # for number in line_numbers:
        #     if len(pair) == 0:
        #         pair.append(number)
        #     elif len(pair) == 1:
        #         pair.append(number)
        #         pairs.append(pair)
        #         pair = []
    return pairs


def get_numbers_str_in_line(line):
    line_numbers = []
    for char in line:
        if char.isnumeric():
            line_numbers.append(char)
    return line_numbers


def can_be_palindrome(word):
    if is_palindrome(word[1:]) or is_palindrome(word[:-1]):
        return True
    return False


def turn_into_palindrome(word: str):
    if is_palindrome(word[1:]):
        return word + word[0]
    elif is_palindrome(word[:-1]):
        return word[-1] + word


def is_palindrome(word: str):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


if __name__ == '__main__':
    main()
