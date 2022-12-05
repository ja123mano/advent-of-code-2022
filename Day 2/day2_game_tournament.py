# Elves play:
#   A - rock
#   B - paper
#   C - scissors

# You play:
#   Par I:
#   X - rock
#   Y - paper
#   Z - scissors
#   Part II:
#   X - need to lose
#   Y - need to draw
#   Z - need to win

# Points:
#   1 - choose rock
#   2 - choose paper
#   3 - choose scissors
#   AND
#   0 - lose
#   3 - draw
#   6 - win

scores = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
scores_b = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

def get_data():
    with open("Day 2\\input.txt", "r") as file:
        guide = file.readlines()
    return guide

def strip_breaks(string: str):
    return string.strip()

def day_2_function(part: str="PartI", verbose: bool=False):
    guide = get_data()
    guide = list(map(strip_breaks, guide))
    
    points = 0
    if part == "PartI":
        print(part + "\n")
    else:
        print("PartII" + "\n")

    for i, game in enumerate(guide):
        if part == "PartI":
            game_points = scores.get(game)
        else:
            game_points = scores_b.get(game)
        points += game_points

        if verbose:
            print(f"Game {i+1}: {game_points}   -   total: {points}")
    
    return points

def day_2_function_b():
    return 0

if __name__ == "__main__":
    total_points = day_2_function(part="PartI", verbose=False)
    print(total_points)

    print("\n\n")

    total_points = day_2_function(part="PartII", verbose=False)
    print(total_points)