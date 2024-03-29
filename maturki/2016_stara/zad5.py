COLUMNS = 20
ROWS = 12


def main():
    with open("dane/gra.txt") as dane:
        world = [[y for y in x] for x in dane.read().strip().split("\n")]
    # world = [
    #     ['X', 'X', '.', '.'],
    #     ['.', '.', '.', '.'],
    #     ['.', '.', 'X', '.'],
    #     ['.', '.', '.', '.'],
    # ]
    zad1(world)
    zad2(world)
    zad3(world)


def zad1(world):
    end_world = calculate_nth_population(37, world)
    print(f'zad 5.1: {count_alive_neighbours((18, 1), end_world)}')


def zad2(world):
    result = 0
    second_world = calculate_nth_population(2, world)
    for row in second_world:
        for cell in row:
            if cell == 'X':
                result += 1
    print(f'zad 5.2: {result}')


def zad3(world):
    for population in range(1, 100):
        cell_count = 0
        current_world = calculate_nth_population(population, world)
        next_world = calculate_next_population(current_world)
        if current_world == next_world:
            for row in current_world:
                for char in row:
                    if char == 'X':
                        cell_count += 1
            print(f'zad 5.3: {population + 1}, liczba komórek: {cell_count}')
            break


def calculate_nth_population(n, world):
    result = world
    for _ in range(n - 1):
        result = calculate_next_population(result)
    return result


def calculate_next_population(world):
    next_world = [['.' for x in range(COLUMNS)] for y in range(ROWS)]
    for x in range(COLUMNS):
        for y in range(ROWS):
            if is_alive_in_next_population((x, y), world):
                next_world[y][x] = 'X'
            else:
                next_world[y][x] = '.'
    return next_world


def is_alive_in_next_population(cell: tuple, world):
    x = cell[0]
    y = cell[1]
    if world[y][x] == 'X' and count_alive_neighbours(cell, world) in [2, 3]:
        return True
    if world[y][x] == '.' and count_alive_neighbours(cell, world) == 3:
        return True
    return False


def count_alive_neighbours(cell: tuple, world):
    neighbours = 0
    x = cell[0]
    y = cell[1]
    '''
    1 2 3
    4 # 5
    6 7 8
    '''
    if world[(y - 1) % ROWS][(x - 1) % COLUMNS] == "X":
        neighbours += 1
    if world[(y - 1) % ROWS][x] == "X":
        neighbours += 1
    if world[(y - 1) % ROWS][(x + 1) % COLUMNS] == "X":
        neighbours += 1
    if world[y][(x - 1) % COLUMNS] == "X":
        neighbours += 1
    if world[y][(x + 1) % COLUMNS] == "X":
        neighbours += 1
    if world[(y + 1) % ROWS][(x - 1) % COLUMNS] == "X":
        neighbours += 1
    if world[(y + 1) % ROWS][x] == "X":
        neighbours += 1
    if world[(y + 1) % ROWS][(x + 1) % COLUMNS] == "X":
        neighbours += 1
    return neighbours


def print_world(world):
    for line in world:
        line_to_print = ""
        for letter in line:
            line_to_print += letter
        print(line_to_print)


if __name__ == '__main__':
    main()
    # with open("dane/gra.txt") as dane:
    #     world = [[y for y in x] for x in dane.read().strip().split("\n")]
    # print_world(calculate_nth_population(50, world))
    # print_world(calculate_nth_population(51, world))