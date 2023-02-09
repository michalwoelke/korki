def main():
    with open("dane/dane.txt", "r") as dane:
        arr = [[int(y) for y in x.split(" ")] for x in dane.read().strip().split("\n")]
    zad1(arr)
    zad2(arr)
    zad3(arr)
    zad4(arr)


def zad1(arr):
    lowest_value = 255
    highest_value = 0
    for row in arr:
        for value in row:
            if value > highest_value:
                highest_value = value
            elif value < lowest_value:
                lowest_value = value
    print(f'zad 6.1: najciemniejszy: {lowest_value}, najjaśniejszy: {highest_value}')


def zad2(arr):
    result = 0
    for row in arr:
        if not is_symmetrical(row):
            result += 1
    print(f'zad 6.2: {result}')


def is_symmetrical(row):
    for i in range(len(row) // 2):
        if row[i] != row[-i - 1]:
            return False
    return True


def zad3(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if has_contrast_neighbour(arr, i, j):
                result += 1
    print(f'zad 6.3: {result}')


def has_contrast_neighbour(arr, i, j):
    return check_horizontal(arr, i, j) or check_vertical(arr, i, j)


def check_horizontal(arr, i, j):
    if j == 0:
        return abs(arr[i][j] - arr[i][j + 1]) > 128
    if j == len(arr[i]) - 1:
        return abs(arr[i][j] - arr[i][j - 1]) > 128
    return abs(arr[i][j] - arr[i][j - 1]) > 128 or abs(arr[i][j] - arr[i][j + 1]) > 128


def check_vertical(arr, i, j):
    if i == 0:
        return abs(arr[i][j] - arr[i + 1][j]) > 128
    if i == len(arr) - 1:
        return abs(arr[i][j] - arr[i - 1][j]) > 128
    return abs(arr[i][j] - arr[i - 1][j]) > 128 or abs(arr[i][j] - arr[i + 1][j]) > 128


def zad4(arr):
    result = 0
    for j in range(len(arr[0])):
        curr_line_longest = longest_line_in_column(arr, j)
        if curr_line_longest > result:
            result = curr_line_longest
    print(f'zad 6.4: {result}')


def longest_line_in_column(arr, j):
    result = 0
    current_length = 1
    for i in range(1, len(arr)):
        if arr[i - 1][j] == arr[i][j]:
            current_length += 1
            if current_length > result:
                result = current_length
        else:
            current_length = 1
    return result


if __name__ == '__main__':
    main()
