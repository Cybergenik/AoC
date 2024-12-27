#!/usr/local/bin/python3

import schemdraw
from schemdraw.elements import Line
import schemdraw.logic as logic
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

def create_circuit(eqs):
    gate_map = {
        'AND': logic.And,
        'OR':  logic.Or,
        'XOR': logic.Xor
    }
    with schemdraw.Drawing(show=False) as d:
        # Keep track of each signal name -> line element
        signals = {}

        for i, (input_x, gate_type, input_y, output_z) in enumerate(eqs):
            GateClass = gate_map[gate_type]

            # -- Ensure signals exist
            #if input_x not in signals:
            #    # Place the input line to the left of (0, -3*i) so it can connect to in1
            #    # We'll place input_x at (-3, -3*i)
            #    x_line = d.add(
            #        Line()
            #        .at((-3, -3*i))
            #        .right()
            #        .label(input_x, loc='left')
            #    )

            #if input_y not in signals:
            #    # Place input_y somewhere above or below so it won't overlap
            #    # For simplicity, offset by some vertical shift
            #    y_line = d.add(
            #        Line()
            #        .at((-3, -3*i-1))
            #        .right()
            #        .label(input_y, loc='left')
            #    )
            # 
            # -- Place the gate itself
            # We'll place gate i at (0, -3*i) with in1 anchored there
            gate_elem = d.add(
                GateClass(inputs=2, output=True)
                .at((0, -3*i))  
                .anchor('in1')  
                # Label the gate with index and type
                .label(f"[{gate_type}]", loc="top")
            )

            ## Connect input_x to gate in1
            #d.add(
            #    Line()
            #    .at(x_line.end)
            #    .to(gate_elem.in1)
            #)

            ## Connect input_y to gate in2
            #d.add(
            #    Line()
            #    .at(y_line.end)
            #    .to(gate_elem.in2)
            #)
            gate_elem.in1.label(input_x, loc='left')
            gate_elem.in2.label(input_y, loc='left')

            # -- Create the output line
            out_line = d.add(
                Line()
                .at(gate_elem.out)
                .right()  # move to the right
                .label(output_z, loc='right')
            )
            signals[output_z] = out_line

        # Save the final diagram
        d.save('logic_circuit.svg')
        d.draw()

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

    create_circuit(eqs)
    
if __name__ == "__main__":
    raise SystemExit(main())
