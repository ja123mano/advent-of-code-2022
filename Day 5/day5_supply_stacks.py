def get_data():
    with open("Day 5\\input.txt", "r") as file:
        guide = file.readlines()
    return guide

def strip_breaks(string: str):
    return string.strip("\n")

def day_5_function(cols: int=9, part: str="PartI", verbose: bool=False):
    supply_stacks = get_data()
    supply_stacks = list(map(strip_breaks, supply_stacks))

    arrange = [[] for _ in range(cols)]
    for line in supply_stacks:
        if line[1] == '1':
            break

        for i, container in enumerate(line):
            if container.isalpha():
                good_index = (i-1)//4
                arrange[good_index].append(container)
    
    for container in range(len(arrange)):
        arrange[container].reverse()
    
    for inst in range(10, len(supply_stacks)):
        numbers = supply_stacks[inst].split(" ")
        numbers = [int(numbers[1]), int(numbers[3])-1, int(numbers[5])-1]

        if verbose:
            print(arrange, "\n")
            print(supply_stacks[inst])

        if part == "PartI":
            for i in range(numbers[0]):
                if verbose:
                    print(f"-------------------------------------------------------------------------- Move {i+1}")
                    print(f"arrange[{numbers[1]}] = {arrange[numbers[1]]}")
                    print(f"arrange[{numbers[2]}] = {arrange[numbers[2]]}")

                des = numbers[2]
                cont = arrange[numbers[1]].pop()
                arrange[des].append(cont)

                if verbose:
                    print("\nAfter the arrange")
                    print(f"arrange[{numbers[1]}] = {arrange[numbers[1]]}")
                    print(f"arrange[{numbers[2]}] = {arrange[numbers[2]]}")
        else:
            if verbose:
                print(f"arrange[{numbers[1]}] = {arrange[numbers[1]]}")
                print(f"arrange[{numbers[2]}] = {arrange[numbers[2]]}")

            src = numbers[1]
            des = numbers[2]
            pnt = len(arrange[src]) - numbers[0]

            for i in range(numbers[0]):
                arrange[des].append(arrange[src].pop(pnt))

            if verbose:
                print("\nAfter the arrange")
                print(f"arrange[{numbers[1]}] = {arrange[numbers[1]]}")
                print(f"arrange[{numbers[2]}] = {arrange[numbers[2]]}")

        if verbose:
            print("==========================================================================================")

    for line in arrange:
        print(line[-1], end="")

    return arrange

if __name__ == "__main__":
    final_arrange = day_5_function(part="PartI")
    final_arrange_b = day_5_function(part="PartII")

    print(final_arrange)
    print(final_arrange_b)
