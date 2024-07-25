#!/usr/local/bin/python3

from dataclasses import dataclass

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

    # BFS
    def complete(self, init_mod, init_sig):
        low = 0
        high = 0
        work = [(init_mod, "broadcaster", init_sig)]
        while work:
            in_mod, mod, signal = work.pop(0)
            if signal == None: continue
            if signal == "low": low += 1
            elif signal == "high": high += 1
            print(f'{in_mod} -{signal}> {mod}')
            if mod in self.modules:
                out = self.modules[mod].pulse(in_mod, signal)
                for e_mod in self.modules[mod].dests:
                    work.append((mod, e_mod, out))
        return low, high

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
    total_low = 0
    total_high = 0
    for _ in range(1000):
        low, high = C.complete("button", "low")
        total_low += low
        total_high += high
    print(total_low*total_high)

if __name__ == "__main__":
    raise SystemExit(main())
