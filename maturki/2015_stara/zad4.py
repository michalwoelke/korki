def main():
    with open('dane/slowa.txt', 'r') as dane:
        arr = [x for x in dane.read().strip().split('\n')]
    # print(arr)
    # arr = ['100010000100', '001', '000', '10101001110000', '000011']
    zad2(arr)
    zad3(arr)


def zad1(arr=None):
    # idenytcznie zadanie jak z matury 2015 - zad 4.1 (zrobione tam)
    pass


def zad2(arr):
    result = 0
    for word in arr:
        if word[0] == '0' and len(divide_into_blocks(word)) == 2:
            result += 1
        # if len(divide_into_blocks(word)) == 2:
        #     if divide_into_blocks(word)[0][0] == '0' and divide_into_blocks(word)[1][0] == '1':
        #         result += 1
    print(result)


def zad3(arr):
    largest_block = 0
    result = []
    for word in arr:
        word_block_length = get_longest_zeros_block_length(word)
        if word_block_length > largest_block:
            largest_block = word_block_length
            result.clear()
            result.append(word)
        elif word_block_length == largest_block:
            result.append(word)
        # should_add_word = False
        # for block in divide_into_blocks(word):
        #     if block[0] == '0':
        #         if len(block) > largest_block:
        #             largest_block = len(block)
        #             result.clear()
        #             should_add_word = True
        #         elif len(block) == largest_block:
        #             should_add_word = True
        # if should_add_word:
        #     result.append(word)
    print(largest_block, result)


def get_longest_zeros_block_length(word) -> int:
    blocks = divide_into_blocks(word)
    result = 0
    for block in blocks:
        if block[0] == '0':
            result = len(block) if len(block) > result else result
    return result


def divide_into_blocks(word):
    blocks = []
    block = word[0]
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            block += word[i]
        else:
            blocks.append(block)
            block = word[i]
    blocks.append(block)
    return blocks


if __name__ == '__main__':
    main()
    # divide_into_blocks('100110001')
