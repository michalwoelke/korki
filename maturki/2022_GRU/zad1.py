def main():
    file = open('Dane_2212/mecz.txt', 'r').read().strip()
    print(zad3(file))


def zad1(file):
    different_winners = 0
    for i in range(len(file)):
        if file[i] != file[i - 1]:
            different_winners += 1
    return different_winners


def zad2(file):
    a_wins = 0
    b_wins = 0
    current_winner = ''
    for char in file:
        if char == 'A':
            a_wins += 1
            current_winner = 'A'
            if a_wins - b_wins >= 3 and a_wins >= 1000:
                break
        else:
            b_wins += 1
            current_winner = 'B'
            if b_wins - a_wins >= 3 and b_wins >= 1000:
                break
    return f'{current_winner} {a_wins}:{b_wins}'


def zad3(file):
    current_passa = 0
    best_passa = 0
    best_passa_team = ''
    passa_count = 0
    for i in range(len(file)):
        if file[i] != file[i - 1]:
            if current_passa >= 10:
                passa_count += 1
            current_passa = 1
        else:
            current_passa += 1
            current_passa_team = file[i]
            if current_passa > best_passa:
                best_passa = current_passa
                best_passa_team = current_passa_team
    return f'{passa_count} {best_passa_team} {best_passa}'


if __name__ == '__main__':
    main()
