def get_data():
    with open("Day 1\\input.txt", "r") as file:
        calories = file.readlines()
    return calories

def strip_breaks(string: str):
    return string.strip()

def day_1_function(output_file: bool=False):
    calories = get_data()
    calories = list(map(strip_breaks, calories))
    sum_calories = list()
    first_number = True
    index = 0

    for num_calories in calories:
        if num_calories and first_number:
            sum_calories.append(int(num_calories))
            first_number = False
        elif num_calories:
            sum_calories[index] += int(num_calories)
        else:
            index += 1
            first_number = True

    calories_max = max(sum_calories)
    string_max = "Max Calories = " + str(calories_max)
    sum_calories.append("")
    sum_calories.append(string_max)

    if output_file:
        with open("Day 1\\sum_of_input.txt", "w") as file:
            str_sum_calories = ["\n".join(list(map(str, sum_calories)))]
            file.writelines(str_sum_calories)

    return calories_max

if __name__ == "__main__":
    max_calories = day_1_function(output_file=True)

    print(max_calories)