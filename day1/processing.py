from re import findall as regex_find

INPUT_FILENAME = "input.txt"
REGEX_PATTERN_VALID_DIGIT = "\d"
NUMBER_MATRIX = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

if __name__ == '__main__':
    counter = 0
    buffer_list = list()

    with open(INPUT_FILENAME) as open_file:
        lines_as_list = open_file.readlines()

    for line in lines_as_list:
        line_without_linebreak = line.rstrip()

        # this block id needed for part 2, if only part 1 comment it out
        for written_number in NUMBER_MATRIX.keys():
            line_without_linebreak = line_without_linebreak.replace(
                written_number,
                written_number+str(NUMBER_MATRIX[written_number])+written_number
            )

        all_valid_numbers_as_list = regex_find(REGEX_PATTERN_VALID_DIGIT, line_without_linebreak)

        wanted_numbers = all_valid_numbers_as_list[0] + all_valid_numbers_as_list[-1]
        counter += int(wanted_numbers)
    print(counter)
