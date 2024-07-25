#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import networkx as nx
import random

def main():
    with open("input.txt") as f:
        content = f.readlines()

    graph = nx.Graph()
    for l in content:
        k, vs = l.strip().split(": ")
        for v in vs.split():
            graph.add_edge(k, v, capacity=1.0)
            graph.add_edge(v, k, capacity=1.0)

    while True:
        n1 = random.choice(list(graph.nodes))
        n2 = random.choice(list(graph.nodes))
        cuts, groups = nx.minimum_cut(graph, n1, n2)
        if cuts == 3:
            print(len(groups[0])*len(groups[1]))
            break

if __name__ == "__main__":
    raise SystemExit(main())
