INPUT_FILENAME = "input.txt"

if __name__ == '__main__':
    with open(INPUT_FILENAME) as open_file:
        lines_as_list = open_file.readlines()

    for line in lines_as_list:
        line_without_linebreak = line.rstrip()
