#!/usr/local/bin/python3

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    time = int("".join(content[0].split(": ")[-1].strip().split()))
    distance = int("".join(content[1].split(": ")[-1].strip().split()))
    total = 0
    btime = 0
    while time > 0:
        dt = btime * time
        if dt > distance:
            total += 1
        btime += 1
        time -= 1
    print(total)
if __name__ == "__main__":
    raise SystemExit(main())
