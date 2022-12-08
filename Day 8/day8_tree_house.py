def get_data():
    with open("Day 8\\input.txt", "r") as file:
        guide = file.readlines()
    return guide

def strip_breaks(string: str):
    return string.strip()

def day_8_function():
    grid = get_data()
    grid = list(map(list,map(strip_breaks, grid)))
    for i in range(len(grid)):
        for n in range(len(grid[i])):
            grid[i][n] = int(grid[i][n])

    visible_trees = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            tree = grid[row][col]

            if all(grid[row][c] < tree for c in range(col)) or all(grid[row][c] < tree for c in range(col+1, len(grid[row]))) or all(grid[r][col] < tree for r in range(row)) or all(grid[r][col] < tree for r in range(row+1, len(grid))):
                visible_trees += 1

    return visible_trees

def day_8_function_b():
    grid = get_data()
    grid = list(map(list,map(strip_breaks, grid)))
    for i in range(len(grid)):
        for n in range(len(grid[i])):
            grid[i][n] = int(grid[i][n])

    max_view = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            tree = grid[row][col]
            up = right = down = left = 0

            for l_tree in range(col-1, -1, -1):
                left += 1
                if grid[row][l_tree] >= tree:
                    break

            for r_tree in range(col+1, len(grid[row])):
                right += 1
                if grid[row][r_tree] >= tree:
                    break
            
            for u_tree in range(row-1, -1, -1):
                up += 1
                if grid[u_tree][col] >= tree:
                    break

            for d_tree in range(row+1, len(grid)):
                down += 1
                if grid[d_tree][col] >= tree:
                    break
            
            points = up * right * down * left
            if points > max_view:
                max_view = points

    return max_view

if __name__ == "__main__":
    visible_trees = day_8_function()
    print(visible_trees)

    viewing_distance = day_8_function_b()
    print(viewing_distance)