# new_dict = {"a":[{"c":[284, 852, 258, 369], "d":[123, 321, 456, 654]}, 894, 1024], "b":[{"e":[753, 357]}, 741, 147]}

# print(new_dict, "\n")
# print(new_dict.get("a"))
# print(new_dict.get("a")[0].get("c"))
# print(new_dict.get("a")[0].get("d"), "\n")
# print(new_dict.get("b"))
# print(new_dict.get("b")[0].get("e"))

def get_data():
    with open("Day 7\\input.txt", "r") as file:
        guide = file.readlines()
    return guide

def strip_breaks(string: str):
    return string.strip()

def day_7_function():
    tree_dir_inst = get_data()
    tree_dir_inst = list(map(strip_breaks, tree_dir_inst))

    cwd = root = dict()
    stack = []
    for inst in tree_dir_inst:
        if inst[0] == "$":
            if inst[2] == "c":
                directory = inst[5:]

                if directory == "/":
                    cwd = root
                    stack = []
                elif directory == "..":
                    cwd = stack.pop()
                else:
                    if directory not in cwd:
                        cwd[directory] = {}
                    
                    stack.append(cwd)
                    cwd = cwd[directory]
        
        else:
            data, name = inst.split()

            if data == "dir":
                if name not in cwd:
                    cwd[name] = {}
                
            else:
                cwd[name] = int(data)

    return root

def recursive_solve(directory: dict):
    if type(directory) == int:
        return (directory, 0)
    
    size = 0
    answer = 0
    for child in directory.values():
        s, a = recursive_solve(child)
        size += s
        answer += a

    if size <= 100_000:
        answer += size
    
    return (size, answer)

def recursive_size(directory: dict):
    if type(directory) == int:
        return directory

    return sum(map(recursive_size, directory.values()))

def recursive_solve_b(directory: dict, th: int):
    answer = float("inf")
    size = recursive_size(directory)
    
    if size >= th:
        answer = size
    
    for child in directory.values():
        if type(child) == int:
            continue

        valid_size = recursive_solve_b(child, threshold)
        answer = min(answer, valid_size)
    
    return answer

if __name__ == "__main__":
    # Part I ------------------------------------------------------------------
    root = day_7_function()
    # print(root)

    acum_size = recursive_solve(root)
    print(acum_size[1])

    # Part II ------------------------------------------------------------------
    threshold = recursive_size(root) - 40_000_000
    minimum_size = recursive_solve_b(root, threshold)
    print(minimum_size)