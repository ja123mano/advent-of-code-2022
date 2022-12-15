def get_data():
    with open("Day 12\\input.txt", "r") as file:
        guide = file.readlines()
    return guide

def strip_breaks(string: str):
    return string.strip()

def day_12_function(part="PartI"):
    hill = list(map(strip_breaks, get_data()))
    hill = [list(row) for row in hill]

    start_row, start_col = None, None
    end_row, end_col = None, None
    for i, row in enumerate(hill):
        if start_row != None and start_col != None and end_row != None and end_col != None:
            break

        for j, item in enumerate(row):
            if start_row != None and start_col != None and end_row != None and end_col != None:
                break
            elif item == "S":
                start_row, start_col = i, j
                hill[i][j] = "a"
            elif item == "E":
                end_row, end_col = i, j
                hill[i][j] = "z"
    
    if part == "PartI":
        visited = {(start_row, start_col)}
        queue = [(0, start_row, start_col)]
    else:
        visited = {(end_row, end_col)}
        queue = [(0, end_row, end_col)]

    while queue:
        dist, row, col = queue.pop(0)

        for next_row, next_col in [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]:
            if next_row < 0 or next_row > len(hill)-1 or next_col < 0 or next_col > len(hill[0])-1 or (next_row, next_col) in visited:
                continue
            elif ord(hill[next_row][next_col])-ord(hill[row][col]) > 1 and part == "PartI":
                continue
            elif ord(hill[next_row][next_col])-ord(hill[row][col]) < -1 and part != "PartI":
                continue
            elif next_row == end_row and next_col == end_col and part == "PartI":
                return dist+1
            elif hill[next_row][next_col] == 'a' and part != "PartI":
                return dist+1

            queue.append((dist+1, next_row, next_col))
            visited.add((next_row, next_col))

if __name__ == "__main__":
    few_steps = day_12_function()
    print(few_steps)

    few_steps = day_12_function(part="PartII")
    print(few_steps)