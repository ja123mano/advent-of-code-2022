def get_data():
    with open("Day 4\\input.txt", "r") as file:
        guide = file.readlines()
    return guide

def strip_breaks(string: str):
    return string.strip()

def day_4_function():
    assign_collisions = get_data()
    assign_collisions = list(map(strip_breaks, assign_collisions))

    full_contains = 0
    partial_contains = 0
    for pair in assign_collisions:
        list_pair = pair.split(",")

        elf1 = list_pair[0].split("-")
        elf1 = set(range(int(elf1[0]), int(elf1[1])+1))

        elf2 = list_pair[1].split("-")
        elf2 = set(range(int(elf2[0]), int(elf2[1])+1))

        if elf2.issubset(elf1) or elf1.issubset(elf2):
            full_contains += 1
        
        if len(elf1.intersection(elf2)) > 0:
            partial_contains += 1

    return full_contains, partial_contains

if __name__ == "__main__":
    contains, collisions = day_4_function()
    print(contains)
    print(collisions)