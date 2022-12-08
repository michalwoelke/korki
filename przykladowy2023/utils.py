def read_file(file: str):
    file = open(file, 'r')
    content = file.read()
    file.close()
    return content
