
def vis(x, y, graph):
    #left:
    for lx in range(x-1, -1, -1):
        if graph[lx][y] >= graph[x][y]:
            break
        if lx == 0:
            return True
    #right:
    for rx in range(x+1, len(graph)):
        if graph[rx][y] >= graph[x][y]:
            break
        if rx == len(graph)-1:
            return True
    #up:
    for uy in range(y-1, -1, -1):
        if graph[x][uy] >= graph[x][y]:
            break
        if uy == 0:
            return True
    #down:
    for dy in range(y+1, len(graph[0])):
        if graph[x][dy] >= graph[x][y]:
            break
        if dy == len(graph[0])-1:
            return True
    return False

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()   
    
    graph = []

    for l in content:
        graph.append([int(n) for n in l.strip()])

    total = (len(graph)*2) + ((len(graph[0])*2)-4)
    for x in range(1, len(graph)-1):
        for y in range(1, len(graph[x])-1):
            if vis(x, y, graph):
                total += 1
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())
