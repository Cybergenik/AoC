
def vis(x, y, graph):
    left = 0
    right = 0
    up = 0
    down = 0
    #left:
    for lx in range(x-1, -1, -1):
        left += 1
        if graph[lx][y] >= graph[x][y]:
            break
        
    #right:
    for rx in range(x+1, len(graph)):
        right += 1
        if graph[rx][y] >= graph[x][y]:
            break
    #up:
    for uy in range(y-1, -1, -1):
        up += 1
        if graph[x][uy] >= graph[x][y]:
            break
    #down:
    for dy in range(y+1, len(graph[0])):
        down += 1
        if graph[x][dy] >= graph[x][y]:
            break
    return left*right*up*down

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()   
    
    graph = []

    for l in content:
        graph.append([int(n) for n in l.strip()])

    max_view = None
    for x in range(0, len(graph)):
        for y in range(0, len(graph[x])):
            scenic_scr = vis(x, y, graph)
            if not max_view or scenic_scr > max_view:
                max_view = scenic_scr
    print(max_view)

if __name__ == "__main__":
    raise SystemExit(main())
