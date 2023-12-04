from re import findall as regex_find

INPUT_FILENAME = "input.txt"
GAME_REGEX = "Game (\d+): (.*)"


class CubeBag:
    allowed_contents = {"red": 12, "blue": 14, "green": 13}

    def __init__(self, arg_game_id):
        self.game_id = arg_game_id
        self.cubes = {"red": 0, "blue": 0, "green": 0}

    def update_cubes(self, color, count):
        if self.cubes[color] < count:
            self.cubes[color] = count

    def bag_is_possible(self):
        for ball_color in self.allowed_contents.keys():
            if self.allowed_contents[ball_color] < self.cubes[ball_color]:
                return False
        return True

    def power_of_colors_calc(self):
        result = 1
        for value in self.cubes.values():
            result = result * value
        return result


if __name__ == '__main__':
    possible_games_counter = 0
    power_calc = 0

    with open(INPUT_FILENAME) as open_file:
        lines_as_list = open_file.readlines()

    for line in lines_as_list:
        line_without_linebreak = line.rstrip()

        regex_output = regex_find(GAME_REGEX, line_without_linebreak)[0]
        game_id = int(regex_output[0])
        game_sets = regex_output[1].split(";")

        actual_bag_contents = CubeBag(arg_game_id=game_id)

        for game_set in game_sets:
            print(game_set)
            for pulled_balls in game_set.split(", "):
                number_and_color_combined = pulled_balls.strip().split(" ")
                print(number_and_color_combined)
                number_of_balls = int(number_and_color_combined[0])
                color_of_balls = number_and_color_combined[1]

                actual_bag_contents.update_cubes(color=color_of_balls, count=number_of_balls)

        if actual_bag_contents.bag_is_possible():
            possible_games_counter += game_id
        power_calc += actual_bag_contents.power_of_colors_calc()

    print(f"Summed Up IDs of possible Games: {possible_games_counter}")
    print(f"Summed Up Power of all Games: {power_calc}")
