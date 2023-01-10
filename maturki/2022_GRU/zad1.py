def main():
    file = open('Dane_2212/mecz.txt', 'r').read().strip()
    print(mecz(file))


def mecz(file):
    different_winners = 0
    current_passa = 0
    best_passa = 0
    current_passa_team = ''
    best_passa_team = ''
    passa_count = 0
    for i in range(len(file)):
        if file[i] != file[i - 1]:
            different_winners += 1
            if current_passa >= 10:
                passa_count += 1
            current_passa = 0
        else:
            current_passa += 1
            current_passa_team = file[i]
            if current_passa > best_passa:
                best_passa = current_passa
                best_passa_team = current_passa_team
    a_wins = 0
    b_wins = 0
    current_winner = ''
    for char in file:
        if char == 'A':
            a_wins += 1
            current_winner = 'A'
            if abs(a_wins - b_wins) > 3 and a_wins >= 1000:
                break
        else:
            b_wins += 1
            current_winner = 'B'
            if abs(a_wins - b_wins) > 3 and b_wins >= 1000:
                break
    return f'odp zad1: {different_winners}, zad2: {a_wins, b_wins, current_winner} zad3: {passa_count, best_passa + 1, best_passa_team}'



if __name__ == '__main__':
    main()
    