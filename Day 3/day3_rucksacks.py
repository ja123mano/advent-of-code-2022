def get_data():
    with open("Day 3\\input.txt", "r") as file:
        guide = file.readlines()
    return guide

def strip_breaks(string: str):
    return string.strip()

def get_priority(letter: str):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def day_3_function():
    ruck_sacks = get_data()
    ruck_sacks = list(map(strip_breaks, ruck_sacks))

    sum_priorities = 0
    for r in ruck_sacks:
        middle = int(len(r)/2)

        for letter in r:
            dup = r.find(letter, middle)

            if dup != -1:
                sum_priorities += get_priority(letter)
                break
    
    return sum_priorities

def day_3_function_b():
    ruck_sacks = get_data()
    ruck_sacks = list(map(strip_breaks, ruck_sacks))

    sum_badges = 0
    for i in range(0, len(ruck_sacks)-2, 3):
        r1 = ruck_sacks[i]
        r2 = ruck_sacks[i+1]
        r3 = ruck_sacks[i+2]

        for letter in r1:
            if r2.find(letter) != -1 and r3.find(letter) != -1:
                sum_badges += get_priority(letter)
                break
    
    return sum_badges

if __name__ == "__main__":
    sum_priorities = day_3_function()
    print(sum_priorities)

    sum_badges = day_3_function_b()
    print(sum_badges)
