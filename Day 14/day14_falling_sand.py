def get_data():
    with open("Day 14\\input.txt", "r") as file:
        guide = file.readlines()
    return guide

def day_14_function(part="PartI"):
    sand = list(map(str.strip, get_data()))
    
    rocks = []
    for x in sand:
        points = x.split(" -> ")
        
        line = []
        for p in points:
            p = p.split(",")
            line.append([int(p[0]), int(p[1])])
        rocks.append(line)

    blocked = set()
    void = 0
    for rock in rocks:
        for (x1, y1), (x2, y2) in zip(rock, rock[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])

            for x_coor in range(x1, x2+1):
                for y_coor in range(y1, y2+1):
                    blocked.add((x_coor, y_coor))
                    void = max(void, y_coor+1)

    resting = 0
    if part == "PartI":
        while True:
            source = (500, 0)

            while True:
                if source[1] >= void:
                    return resting
                if (source[0], source[1]+1) not in blocked:
                    source = (source[0], source[1]+1)
                    continue
                if (source[0]-1, source[1]+1) not in blocked:
                    source = (source[0]-1, source[1]+1)
                    continue
                if (source[0]+1, source[1]+1) not in blocked:
                    source = (source[0]+1, source[1]+1)
                    continue

                blocked.add(source)
                resting += 1
                break
    else:
        while (500, 0) not in blocked:
            source = (500, 0)

            while True:
                if source[1] >= void:
                    break
                if (source[0], source[1]+1) not in blocked:
                    source = (source[0], source[1]+1)
                    continue
                if (source[0]-1, source[1]+1) not in blocked:
                    source = (source[0]-1, source[1]+1)
                    continue
                if (source[0]+1, source[1]+1) not in blocked:
                    source = (source[0]+1, source[1]+1)
                    continue
                break

            blocked.add(source)
            resting += 1
        
        return resting


if __name__ == "__main__":
    rested_sand = day_14_function()
    print(rested_sand)

    rested_sand = day_14_function(part="PartII")
    print(rested_sand)