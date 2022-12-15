def read_string(file_name: str):
    # TODO: 'string.txt' should be imported as it is
    file = open(file_name, 'r')
    content = file.read()
    file.close()
    return content.strip()


def read_space_list(file_name: str):
    # TODO: 'space-list.txt' should be imported as list of strings
    file = open(file_name, 'r')
    content = file.read().split(' ')
    file.close()
    return content


def read_list(file_name: str):
    # TODO: 'list.txt' should be imported as list of numbers
    file = open(file_name, 'r')
    content = file.read().strip().split('\n')
    file.close()
    # FOR LOOP APPROACH
    # new_list = []
    # for el in content:
    #     new_list.append(int(el))

    # MAPPING FUNCTION APPROACH
    # new_list = list(map(int, content))

    # PYTHON COMPREHENSIONS APPROACH
    return [int(x) for x in content]


def read_comma_list(file_name: str):
    # TODO: 'comma-list.txt' should be imported as list of numbers
    file = open(file_name, 'r')
    content = file.read().strip().split(',')
    file.close()
    return [int(x) for x in content]


def read_2d_table(file_name: str):
    # TODO: 'list_2d.txt' should be imported as 2d char table
    file = open(file_name, 'r')
    content = file.read().strip().split('\n')
    file.close()
    # FOR LOOP APPROACH
    # new_arr = []
    # for el in content:
    #     el_array = []
    #     for char in el:
    #         el_array.append(char)
    #     new_arr.append(el_array)

    # PYTHON COMPREHENSIONS APPROACH
    return [[char for char in row] for row in content]


def read_2d_int_table(file_name: str):
    # TODO: 'int_list_2d.txt' should be imported as 2d ints table
    file = open(file_name, 'r')
    content = file.read().strip().split('\n')
    file.close()

    return [[int(x) for x in row] for row in content]


def read_curly_wrapped_list(file_name: str):
    # TODO: 'curly_wrapped_list.txt' should be imported as int list
    file = open(file_name, 'r')
    content = file.read().strip()
    file.close()
    return [int(x.strip()) for x in content[1:-1].split(',')]


def read_list_of_int_list(file_name: str):
    # TODO: 'list_of_int_list.txt' should be imported as list of integer list
    file = open(file_name, 'r')
    content = file.read().strip().split('\n\n')
    file.close()
    return [[int(x.strip()) for x in x.split(',')] for x in content]


def read_list_of_mixed_type(file_name: str):
    # TODO: 'list_of_mixed_types.txt' should be imported as list of string and ints - depending on element
    file = open(file_name, 'r')
    content = file.read().strip().split(', ')
    file.close()
    return [int(x) if x.isnumeric() or x.startswith('-') and x[1:].isnumeric() else x for x in content]


def read_weirdly_formatted_dictionary(file_name: str):
    # TODO: 'weirdly_formatted_dictionary.txt' should be imported as dictionary
    file = open(file_name, 'r')
    content = file.read().strip().split('\n')
    file.close()

    # FOR LOOP APPROACH
    # arr = [x.split(' - ') for x in content]
    # dictionary = {}
    # for el in arr:
    #     dictionary[el[0]] = el[1]
    # return dictionary

    # PYTHON COMPREHENSION APPROACH
    return {el[0].strip(): el[1].strip() for el in [x.split('-') for x in content]}
