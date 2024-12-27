#!/usr/local/bin/python3

from collections import defaultdict

def process_circuit(graph, eqs):
    work = [eq for eq in eqs]
    while work:
        v1, op, v2, out = work.pop(0)
        if graph[v1] is None or graph[v2] is None:
            work.append((v1, op, v2, out))
            continue
        if op == "AND":
            graph[out] = 1 if graph[v1] == 1 and graph[v2] == 1 else 0
        elif op == "OR":
            graph[out] = 1 if graph[v1] == 1 or graph[v2] == 1 else 0
        elif op == "XOR":
            graph[out] = abs(graph[v1]-graph[v2])

def main():
    with open("input.txt") as f:
        content = f.read()
    graph = defaultdict(lambda: None)
    eqs = []
    p1, p2 = content.split("\n\n")
    for l in p1.strip().split("\n"):
        gate, val = l.strip().split(": ")
        graph[gate] = int(val)
    for l in p2.strip().split("\n"):
        eq, out = l.strip().split(" -> ")
        v1, op, v2 = eq.split(" ")
        eqs.append((v1, op, v2, out))

    process_circuit(graph, eqs)
    z_gates = [(int(g[1:]), graph[g]) for g in graph if g[0] == "z"]
    num = 0
    for shift, v in z_gates:
        num |= v << shift
    print(num)



    
if __name__ == "__main__":
    raise SystemExit(main())
