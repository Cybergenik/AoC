#!/usr/local/bin/python3

from dataclasses import dataclass
from tqdm import tqdm

class Module:
    # dests: list[str], state: str | dict[str, str]
    def __init__(self, dests, state):
        self.dests = dests
        self.state = state
    def pulse(self, in_mod, signal):
        if type(self.state) == str:
            if signal == "low":
                if self.state == "on":
                    self.state = "off"
                    return "low"
                elif self.state == "off":
                    self.state = "on"
                    return "high"
        elif type(self.state) == dict:
            self.state[in_mod] = signal
            for d in self.state.values():
                if d == "low":
                    return "high"
            return "low"
        else:
            return signal

class Circuit:
    def __init__(self):
        self.modules = {}
    def add(self, src, dests):
        if src[0] == '%':
            self.modules[src[1:]] = Module(dests, "off")
        elif src[0] == '&':
            self.modules[src[1:]] = Module(dests, {})
        else:
            self.modules[src] = Module(dests, None)

    def __repr__(self):
        s = ''
        for k, v in self.modules.items():
            s += f'{k}: {v.state} -> D: {v.dests}\n'
        return s

    # BFS
    def complete(self, init_mod, init_sig):
        work = [(init_mod, "broadcaster", init_sig)]
        while work:
            in_mod, mod, signal = work.pop(0)
            if signal == None: continue
            #print(f'{in_mod} -{signal}> {mod}')
            if mod == "rx":
                if signal == "low":
                    return True
                break
            out = self.modules[mod].pulse(in_mod, signal)
            for e_mod in self.modules[mod].dests:
                work.append((mod, e_mod, out))
        return False

def hash_C(c):
    h = ()
    for k, v in c.modules.items():
        h = (*h, f'{k}:{v.state}')
    print(h)
    return h
def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    C = Circuit()
    for l in content:
        src, dests = l.strip().split(" -> ")
        dests = dests.split(", ")
        C.add(src, dests)
    for name, mod in C.modules.items():
        if type(mod.state) == dict:
            for n, mmod in C.modules.items():
                if n == name: continue
                if name in mmod.dests:
                    mod.state[n] = "low"
    circuit_map = {hash_C(C): 0}
    for i in range(1, 10000000000):
        C.complete("button", "low")
        h = hash_C(C)
        if h in circuit_map:
            print(circuit_map[h], i)
            print(h)
            break
        circuit_map[i] = h


if __name__ == "__main__":
    raise SystemExit(main())
