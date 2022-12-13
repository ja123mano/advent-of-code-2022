def get_data():
    with open("Day 10\\input.txt", "r") as file:
        guide = file.readlines()
    return guide

def strip_breaks(string: str):
    return string.strip()

def day_10_function(verbose=False):
    instructions = get_data()
    instructions = list(map(strip_breaks, instructions))

    reg_X = 1
    cycle = 0
    strenght = 0
    flag = False

    for line in instructions:
        inst = line.split()
        flag = False
        
        if inst[0] == "noop":
            cycle += 1
        else:
            for i in range(2):
                cycle += 1
                if cycle == 20 or (cycle-20) % 40 == 0:
                    signal = cycle*reg_X
                    strenght += signal
                    if verbose:
                        print(f"Cycle {cycle}, signal {signal}, strenght {strenght}")
                    flag = True

            reg_X += int(inst[1])

        if not flag and (cycle == 20 or (cycle-20) % 40 == 0):
            signal = cycle*reg_X
            strenght += signal
            if verbose:
                print(f"Cycle {cycle}, signal {signal}, strenght {strenght}")
        
    return strenght

def day_10_function_b():
    instructions = get_data()
    instructions = list(map(strip_breaks, instructions))

    x_values = []
    reg_X = 1
    
    for line in instructions:
        inst = line.split()

        if inst[0] == "noop":
            x_values.append(reg_X)
        else:
            x_values.append(reg_X)
            x_values.append(reg_X)
            reg_X += int(inst[1])
    
    for row in range(0, len(x_values), 40):
        for col in range(40):
            
            if abs(x_values[row+col] - col) <= 1:
                print("#", end="")
            else:
                print(" ", end="")
        
        print()

if __name__ == "__main__":
    strenght_signals = day_10_function(verbose=False)
    print(strenght_signals)

    print()

    day_10_function_b()