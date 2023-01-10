def main():
    file = open('Dane_2205/liczby.txt')
    numbers = file.read().strip().split('\n')
    file.close()

    ex_1(numbers)
    ex_2(numbers)
    ex_3(numbers)


def ex_1(numbers: list):
    filtered_numbers = [num for num in numbers if num[0] == num[-1]]
    print(f'Zad 4.1\n\tliczb: {len(filtered_numbers)}\n\tpierwsze wystapienie: {filtered_numbers[0]}')


def ex_2(numbers: list):
    nums = [int(num) for num in numbers]
    nums_factors = [{'number': num, 'factors': factorize(num)} for num in nums]
    max_factors = {'number': 0, 'no_factors': 0}
    max_diff_factors = {'number': 0, 'no_factors': 0}
    for num_factor in nums_factors:
        if len(num_factor['factors']) > max_factors['no_factors']:
            max_factors = {'number': num_factor['number'], 'no_factors': len(num_factor['factors'])}
        if len(set(num_factor['factors'])) > max_diff_factors['no_factors']:
            max_diff_factors = {'number': num_factor['number'], 'no_factors': len(set(num_factor['factors']))}
    print('Zad 4.2')
    print(f'\tNajwiecej czynnikow - liczba: {max_factors["number"]}, czynnikow: {max_factors["no_factors"]}')
    print(
        f'\tNajwiecej roznych czynnikow - liczba: {max_diff_factors["number"]}, czynnikow: {max_diff_factors["no_factors"]}')


def factorize(number: int):
    result = []
    factor = 2
    if number < 2:
        return [number]
    while number != 1:
        if number % factor == 0:
            result.append(factor)
            number /= factor
        else:
            factor += 1
    return result


def ex_3(numbers: list):
    nums = [int(num) for num in numbers]
    # posortowane wiec nie rozpatrujemy juz przypadkow kiedy poprzednie liczby sa wieksze od kolejnych
    nums.sort()
    found_triples = find_triples(nums)
    found_fives = find_fives(nums)
    print('Zad 4.3')
    print(f'\tdobrych trojek: {len(found_triples)}')
    print(f'\tdobrych piatek: {len(found_fives)}')
    # PAMIETAJ ZE W TRESCI ZADANIA PODALI ZE NALEZY ZAPISAC TROJKI DO PLIKU trojki.txt
    file = open('trojki_h.txt', 'w')
    for found_triple in found_triples:
        file.write(f'{found_triple[0]} {found_triple[1]} {found_triple[2]}\n')
    file.close()


def find_triples(numbers):
    return find_multiples([], numbers, 3)


def find_fives(numbers):
    return find_multiples([], numbers, 5)


def find_multiples(starting_with: list, rest_numbers, multiple):
    if len(starting_with) == multiple:
        # w zasadzie masz juz multipla
        return [starting_with]
    if len(rest_numbers) == 0:
        # konca i nie udalo sie znalezc multipla
        return []
    result = []
    for i in range(len(rest_numbers)):
        num = rest_numbers[i]
        if len(starting_with) == 0:
            result.extend(find_multiples([rest_numbers[i]], rest_numbers[i + 1:], multiple))
        elif num % starting_with[-1] == 0:
            new_starting_with = []
            new_starting_with.extend(starting_with)
            new_starting_with.append(num)
            result.extend(find_multiples(new_starting_with, rest_numbers[i + 1:], multiple))
    return result


if __name__ == '__main__':
    main()
