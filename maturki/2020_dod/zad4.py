def main():
    with open("dane/identyfikator.txt", 'r') as dane:
        arr = [x for x in dane.read().strip().split('\n')]
    # print(arr)
    zad1(arr)
    zad2(arr)
    zad3(arr)


def zad1(arr):
    result = []
    max_sum = 0
    for identifier in arr:
        curr_digits_sum = calculate_sum_of_digits(identifier)
        if curr_digits_sum == max_sum:
            result.append(identifier)
        elif curr_digits_sum > max_sum:
            max_sum = curr_digits_sum
            # result = [identifier] # also valid approach
            result.clear()
            result.append(identifier)

    print(f'zad 4.1: {result}')


def zad2(arr):
    result = []
    for identifier in arr:
        if is_palindrome(identifier[:3]) or is_palindrome(identifier[3:]):
            result.append(identifier)
    print(f'zad 4.2: {result}')


def zad3(arr):
    # print(f'zad 4.3: {[identifier for identifier in arr if not is_valid(identifier)]}')
    result = []
    for identifier in arr:
        if not is_valid(identifier):
            result.append(identifier)
    print(f'zad 4.3: {result}')


def is_valid(identifier: str) -> bool:
    wages = [7, 3, 1]
    control_number = int(identifier[3])
    letter_part = [ord(x) - 55 for x in identifier[:3]]
    number_part = [int(x) for x in identifier[4:]]
    id_without_control = letter_part + number_part
    control_sum = 0
    for i in range(len(id_without_control)):
        control_sum += wages[i % 3] * id_without_control[i]
    return control_sum % 10 == control_number


def is_palindrome(word: str) -> bool:
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            return False
    return True


def calculate_sum_of_digits(identifier: str) -> int:
    digits = [int(n) for n in identifier[3:]]
    return sum(digits)


if __name__ == '__main__':
    main()
