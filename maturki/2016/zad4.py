import math
import datetime

CENTER = [200, 200]
RADIUS = 200


def main():
    with open("dane/punkty.txt") as dane:
        arr = [[int(y) for y in x.split(" ")] for x in dane.read().strip().split("\n")]
    # print(arr)
    zad1(arr)
    zad2(arr)
    zad3(arr)


def zad1(arr):
    border_points = []
    count_inside = 0
    for point in arr:
        if calculate_radius_squared(point[0], point[1]) == RADIUS ** 2:
            border_points.append(tuple(point))
        elif calculate_radius_squared(point[0], point[1]) < RADIUS ** 2:
            count_inside += 1
    print(f'zad 4.1: border points: {border_points}, inside count: {count_inside}')


def zad2(arr):
    print(f'zad 4.2:')
    print(f'\tfirst 1000 points: {round(calculate_pi(arr[:1000]), 4)}')
    print(f'\tfirst 5000 points: {round(calculate_pi(arr[:5000]), 4)}')
    print(f'\tall of the points: {round(calculate_pi(arr), 4)}')


def zad3(arr):
    result = []
    for i in range(1700):
        approx_pi = calculate_pi(arr[:i + 1])
        error = abs(math.pi - approx_pi)
        result.append(error)
    write_to_file("output-wykres.txt", result)
    print(f'zad 4.3:')
    print(f'\terror nr 1000: {round(result[999], 4)}')
    print(f'\terror nr 1700: {round(result[1699], 4)}')


def write_to_file(filename, arr):
    file = open(filename, "w")
    for el in arr:
        file.write(str(el) + "\n")
    file.close()


def calculate_pi(arr):
    square_field = (2 * RADIUS) ** 2
    ratio = count_points_in_circle(arr) / len(arr)
    return ratio * square_field / RADIUS ** 2


def count_points_in_circle(arr):
    result = 0
    for point in arr:
        if calculate_radius_squared(point[0], point[1]) <= RADIUS ** 2:
            result += 1
    return result


def calculate_radius_squared(x, y):
    return (x - CENTER[0]) ** 2 + (y - CENTER[1]) ** 2


if __name__ == '__main__':
    main()
