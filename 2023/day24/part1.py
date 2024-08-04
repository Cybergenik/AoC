import numpy as np

def main():
    with open("input.txt") as f:
        content = f.readlines()

    boundS = 7
    boundE = 27
    hailstones = []
    for l in content:
        pos, vel = l.strip().split(" @ ")
        x, y, z = map(int, pos.split(", ")) 
        dx, dy, dz = map(int, vel.split(", "))
        hailstones.append(((x,y,z), (dx,dy,dz)))
    
    for h in hailstones:
        xyz1, xyz2 = h
        diff = xyz2[0]-


        
if __name__ == "__main__":
    raise SystemExit(main())
