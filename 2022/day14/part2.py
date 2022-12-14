
def pour_sand(walls: set, lowest_y: int):
    total = 0
    curr_grain = (500, 0)
    while (500, 0) not in walls:
        y = curr_grain[1]+1
        if (curr_grain[0], y) not in walls and y != lowest_y:
            curr_grain = (curr_grain[0], y)
        elif (curr_grain[0]-1, y) not in walls and y != lowest_y:
            curr_grain = (curr_grain[0]-1, y)
        elif (curr_grain[0]+1, y) not in walls and y != lowest_y:
            curr_grain = (curr_grain[0]+1, y)
        else:
            total += 1
            walls.add(curr_grain)
            curr_grain = (500, 0)
    return total

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    walls = set()
    lowest_wall = None
    for line in content:
        nums = line.strip('\n').split(" -> ")
        for i in range(len(nums)-1):
            sx, sy = nums[i].split(',')
            ex, ey = nums[i+1].split(',')
            sx, sy = int(sx), int(sy) 
            ex, ey = int(ex), int(ey)
            if sx == ex:
                for j in range(min(sy, ey), max(sy, ey)+1):
                    wall = (sx, j)
                    if not lowest_wall or j > lowest_wall[1]:
                        lowest_wall = wall
                    walls.add(wall)
            else:
                for j in range(min(sx, ex), max(sx, ex)+1):
                    wall = (j, sy)
                    if not lowest_wall or sy > lowest_wall[1]:
                        lowest_wall = wall
                    walls.add(wall)
    print(pour_sand(walls, lowest_wall[1]+2))

if __name__ == "__main__":
    raise SystemExit(main())

