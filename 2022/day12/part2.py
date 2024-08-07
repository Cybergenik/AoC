from pprint import pprint

def adj(x, y, graph):
    if x > 0:
        yield x-1, y
    if x < len(graph)-1:
        yield x+1, y
    if y > 0:
        yield x, y-1
    if y < len(graph[0])-1:
        yield x, y+1

def shortest_path(s, e, graph):
    work = [(*s, 0)]
    seen = set()
    prev = work[0][:-1]
    while work:
        v = work.pop(0)
        #print(v)
        if v[:-1] == e:
            return v[2]
        if v[:-1] not in seen:
            seen.add(v[:-1])
            for x,y in adj(*v[:-1], graph):
                if (graph[x][y]-graph[v[0]][v[1]]) <= 1 and (x,y) != prev:
                    work.append((x,y,v[2]+1))
        prev = v[:-1]
    return 9999

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    graph = []
    target = None
    for i, l in enumerate(content):
        chars = []
        for j, c in enumerate(l):
            if c == 'S':
                chars.append(ord('a'))
            elif c == 'E':
                target = (i,j)
                chars.append(ord('z'))
            else:
                chars.append(ord(c))
        graph.append(chars)
    min_ = None
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == ord('a'):
                path = shortest_path((i,j), target, graph)
                if not min_ or path < min_:
                    min_ = path
    print(min_)
if __name__ == "__main__":
    raise SystemExit(main())

