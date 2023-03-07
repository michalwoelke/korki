def main():
    with open("dane/punkty.txt") as dane:
        arr = [[int(y) for y in x.split(" ")] for x in dane.read().strip().split("\n")]
    zad1(arr)
    zad2(arr)
    zad3(arr)
    zad4(arr)


def zad1(arr):
    result = 0
    for point in arr:
        if is_prime(point[0]) and is_prime(point[1]):
            result += 1
    print(f'zad 4.1: {result}')


def zad2(arr):
    result = 0
    for point in arr:
        x_set = {x for x in str(point[0])}
        y_set = set(y for y in str(point[1]))
        if x_set == y_set:
            result += 1
    print(f'zad 4.2: {result}')


def zad3(arr):
    max_distance = 0
    max_distance_points = []
    for point1 in arr:
        for point2 in arr:
            d = distance(point1, point2)
            if d > max_distance:
                max_distance = d
                max_distance_points = [point1, point2]
    print(f'zad 4.3: max distance is: {round(max_distance)}, for {max_distance_points}')


def zad4(arr):
    inside_count = 0
    side_count = 0
    outside_count = 0
    for point in arr:
        if is_inside(point):
            inside_count += 1
        elif is_on_side(point):
            side_count += 1
        elif is_outside(point):
            outside_count += 1
    print(f'zad 4.4: inside: {inside_count}, sides: {side_count}, outside: {outside_count}')


def is_outside(point):
    return abs(point[0]) > 5000 or abs(point[1]) > 5000


def is_on_side(point):
    return abs(point[0]) == 5000 or abs(point[1]) == 5000


def is_inside(point):
    return abs(point[0]) < 5000 and abs(point[1]) < 5000


def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**(1 / 2)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1 / 2) + 1)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
