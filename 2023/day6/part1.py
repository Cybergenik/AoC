#!/usr/local/bin/python3

def find_all_recs(btime, time, record):
    total = 0
    while time > 0:
        dt = btime * time
        if dt > record:
            total += 1
        btime += 1
        time -= 1
    return total

def main():
    with open("input.txt") as f:
        content = f.readlines()
    times = list(map(int, content[0].split(": ")[-1].strip().split()))
    distances = list(map(int, content[1].split(": ")[-1].strip().split()))
    total = 1
    for i in range(len(times)):
        total *= find_all_recs(0, times[i], distances[i])
    print(total)
if __name__ == "__main__":
    raise SystemExit(main())
