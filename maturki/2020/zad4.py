def main():
     arr = [[y for y in x.split(' ')] for x in open('Dane_PR2/pary.txt', 'r').read().strip().split('\n')]
     # print(goldbach(arr))
     print(goldbach(arr))


def goldbach(arr:list):
    int_arr = []
    for el in arr:
        if int(el[0]) % 2 == 0 and int(el[0]) > 4:
            int_arr.append(int(el[0]))
    wszystkie_skl = []
    for el in int_arr:
        skladniki = [el]
        for i in range(1, el):
            skladniki.append(i)
        wszystkie_skl.append(skladniki)
        wszystkie_pary = []
    # print(wszystkie_skl)
    for el in wszystkie_skl:
        para_liczb = [el[0], 0, 0]
        # print(para_liczb)
        for i in range(len(el)):
            if is_prime(el[i]):
                j = el[0] - el[i]
                if is_prime(j):
                    # print(el[i], j)
                    if para_liczb[1] - para_liczb[2] == 0 and el[i] - j == 0:
                        if el[i] > para_liczb[1] or j > para_liczb[2]:
                            para_liczb[1] = el[i]
                            para_liczb[2] = j
                    if el[i] - j > para_liczb[1] - para_liczb[2]:
                        para_liczb[1] = el[i]
                        para_liczb[2] = j
        parapresorted = [para_liczb[1], para_liczb[2]]
        parasorted = sorted(parapresorted)
        para_liczb = [el[0]]
        para_liczb.extend(parasorted)
        wszystkie_pary.append(para_liczb)

    str_arr = []
    for el in arr:
        str_arr.append(el[1])
        all_streaks = []
    for word in str_arr:
        # print(word)
        best_streak = ''
        str_streak = ''
        current_streak = str(str_streak)
        for i in range(len(word) - 1):
            if word[i] == word[i - 1]:
                str_streak = str(str_streak) + word[i]
                str_streak = word[i] + str_streak[1:]
                if len(str_streak) > len(best_streak):
                    best_streak = str_streak
            else:
                str_streak = word[0]
                if len(str_streak) > len(best_streak):
                    best_streak = str_streak
        # print(best_streak, len(best_streak))
        if best_streak != '':
            out = (best_streak, len(best_streak))
            all_streaks.append(out)

    equal_pairs = []
    for el in arr:
        if int(el[0]) == len(el[1]):
            equal_pairs.append(el)
    smallest_pair = []
    for pair in equal_pairs:
    # print(equal_pairs)
        for other_pair in equal_pairs:
            if int(pair[0]) < int(other_pair[0]) or int(pair[0] == int(other_pair[0])):
                if int(pair[0]) < int(other_pair[0]):
                    continue
                else:
                    lpair = []
                    lotherpair = []
                    for char in pair[1]:
                        lpair.append(char)
                    for char in other_pair[1]:
                        lotherpair.append(char)
                    if len(list(set(lpair))) < len(list(set(lotherpair))):
                        break
            else:
                break
    smallest_pair.append(pair)


    return f'wszystkie pary(zad1) to: {wszystkie_pary}, a wszystkie ciągi liter(zad2) to: {all_streaks}, a najmniejsza para(zad3) to: {smallest_pair}'

def is_prime(x):
    if x > 1:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    return False


if __name__ == '__main__':
    main()
