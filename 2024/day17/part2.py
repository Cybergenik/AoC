#!/usr/local/bin/python3

from collections import defaultdict
from functools import cache
import sys
#from collections import Counter
 
class Computer:
    def __init__(self, ra, rb, rc):
        self.RA = ra
        self.RB = rb
        self.RC = rc
        self.out = []
        pass
    def get_operand_val(self, op):
        if op in (0,1,2,3):
            return op
        elif op == 4:
            return self.RA
        elif op == 5:
            return self.RB
        elif op == 6:
            return self.RC

    def run_inst(self, inst, operand, inst_ptr):
        if inst == 0:
            print(f"RA = RA({self.RA})//2^{self.get_operand_val(operand)}: {self.RA//2**self.get_operand_val(operand)}")
            self.RA = self.RA//2**self.get_operand_val(operand)
        elif inst == 1:
            print(f"RB =  RB({self.RB})^{operand}: {self.RB^operand}")
            self.RB ^= operand
        elif inst == 2:
            print(f"RB = {self.get_operand_val(operand)}%8: {self.get_operand_val(operand)%8}")
            self.RB = self.get_operand_val(operand)%8
        elif inst == 3:
            print(f"JUMP if A != 0, to {operand}")
            if self.RA != 0:
                return operand
        elif inst == 4:
            print(f"RB =  RB({self.RB})^RC({self.RC}): {self.RB^self.RC}")
            self.RB ^= self.RC
        elif inst == 5:
            print(f"print {self.get_operand_val(operand)}%8: {self.get_operand_val(operand)%8}")
            self.out.append(self.get_operand_val(operand)%8)
        elif inst == 6:
            print(f"RB = RA({self.RA})//2^{self.get_operand_val(operand)}: {self.RA//2**self.get_operand_val(operand)}")
            self.RB = self.RA//2**self.get_operand_val(operand)
        elif inst == 7:
            print(f"RC = RA({self.RA})//2^{self.get_operand_val(operand)}: {self.RA//2**self.get_operand_val(operand)}")
            print(f"RC =  RA//2^{self.get_operand_val(operand)}")
            self.RC = self.RA//2**self.get_operand_val(operand)
        return inst_ptr+2

    def run(self, program):
        inst_ptr = 0
        prog = list(map(int, program.split(",")))
        print(f"Running: {prog, len(prog)}\nReg A: {self.RA}\nReg B: {self.RB}\nReg C: {self.RC}\n")
        while inst_ptr < len(prog)-1:
            inst_ptr = self.run_inst(prog[inst_ptr], prog[inst_ptr+1], inst_ptr)
        print(self.out, len(self.out))

def main():
    with open("input.txt") as f:
        content = f.read()
    
    regs, prog = content.split("\n\n")
    a, b, c = [int(r.split(": ")[-1]) for r in  regs.split("\n")]
    comp = Computer(a, b, c)
    comp.run(prog.split(": ")[-1])

if __name__ == "__main__":
    raise SystemExit(main())
