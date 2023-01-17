def main():
    with open('Dane_PR/liczby.txt', 'r') as file:
        arr = [int(x) for x in file.read().strip().split('\n')]
    print(f'zad 4.1: {count_powers_of_3(arr)}')
    print(f'zad 4.2: {numbers_equal_to_factorials_sum(arr)}')
    print(f'zad 4.3:\n{find_longest_series_in(arr)}')


def count_powers_of_3(arr: list):
    numbers = 0
    for num in arr:
        if is_power_of_3(num):
            numbers += 1
    return numbers


def is_power_of_3(num):
    if num == 1:
        return True
    elif num % 3 != 0:
        return False
    else:
        return is_power_of_3(num / 3)


def numbers_equal_to_factorials_sum(arr: list):
    result = []
    mem = {0: 1, 1: 1}
    for num in arr:
        factorials = [factorial(int(digit), mem) for digit in str(num)]
        if sum(factorials) == num:
            result.append(num)
    return result


def factorial(n: int, mem: dict):
    if mem.get(n) is None:
        mem[n] = n * factorial(n - 1, mem)
    return mem[n]


def find_longest_series_in(arr: list):
    longest_ans = [0, 0, 0]
    for i in range(len(arr)):
        ans = find_longest_series([arr[i]], arr[i], arr[i + 1:])
        longest_ans = ans if ans[1] > longest_ans[1] else longest_ans
    return f'pierwsza liczba: {longest_ans[0][0]}\ndlugosc ciagu: {longest_ans[1]}\nnwd: {longest_ans[2]}'


def find_longest_series(current_series: list, curr_nwd: int, rest: list):
    if len(rest) == 0 or nwd(curr_nwd, rest[0]) == 1:
        return [current_series, len(current_series), curr_nwd]
    current_series.append(rest[0])
    return find_longest_series(current_series, nwd(curr_nwd, rest[0]), rest[1:])


def nwd(a, b): return nwd(b, a % b) if b else a


if __name__ == '__main__':
    main()
