def get_data():
    with open("Day 9\\input.txt", "r") as file:
        guide = file.readlines()
    return guide

def strip_breaks(string: str):
    return string.strip()

def day_9_function():
    flow = get_data()
    flow = list(map(strip_breaks, flow))

    positions = set([(0,0)])
    head = [0,0]
    tail = [0,0]

    for move in flow:
        direction, spaces = move.split()
        spaces = int(spaces)

        for _ in range(spaces):
            dx = 1 if direction == "R" else -1 if direction == "L" else 0
            dy = 1 if direction == "U" else -1 if direction == "D" else 0

            head[0] += dx
            head[1] += dy

            dif_x = head[0] - tail[0]
            dif_y = head[1] - tail[1]

            if abs(dif_x) > 1 or abs(dif_y) > 1:
                if dif_x == 0:
                    tail[1] += dif_y // 2
                elif dif_y == 0:
                    tail[0] += dif_x // 2
                else:
                    tail[0] += 1 if dif_x  > 0 else -1
                    tail[1] += 1 if dif_y  > 0 else -1
            
            positions.add(tuple(tail))

    return len(positions)

def day_9_function_b():
    flow = get_data()
    flow = list(map(strip_breaks, flow))

    positions = set([(0,0)])
    rope = [[0,0] for _ in range(10)]

    for move in flow:
        direction, spaces = move.split()
        spaces = int(spaces)

        for _ in range(spaces):
            dx = 1 if direction == "R" else -1 if direction == "L" else 0
            dy = 1 if direction == "U" else -1 if direction == "D" else 0

            rope[0][0] += dx
            rope[0][1] += dy

            for i in range(9):
                head = rope[i]
                tail = rope[i+1]

                dif_x = head[0] - tail[0]
                dif_y = head[1] - tail[1]

                if abs(dif_x) > 1 or abs(dif_y) > 1:
                    if dif_x == 0:
                        tail[1] += dif_y // 2
                    elif dif_y == 0:
                        tail[0] += dif_x // 2
                    else:
                        tail[0] += 1 if dif_x  > 0 else -1
                        tail[1] += 1 if dif_y  > 0 else -1
            
            positions.add(tuple(rope[-1]))

    return len(positions)

if __name__ == "__main__":
    total_positions = day_9_function()
    print(total_positions)

    print()

    total_positions_10_knots = day_9_function_b()
    print(total_positions_10_knots)