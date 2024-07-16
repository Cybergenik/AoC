package main

import (
	"fmt"
	"os"
	"strings"
)

type Path struct {
	posX  uint8
	posY  uint8
	dir   rune
	tempo uint8
	dist  uint32
}

func ultra_adj(p Path, N uint8, M uint8) []Path {
	paths := []Path{}
	min_turn := uint8(4)
	max_turn := uint8(10)
	if p.dir == 'u' {
		if p.tempo >= min_turn {
			//left
			if p.posY >= min_turn {
				paths = append(paths, Path{
					posX:  p.posX,
					posY:  p.posY - 1,
					dir:   'l',
					tempo: 1,
					dist:  p.dist,
				})
			}
			//right
			if p.posY < M-min_turn {
				paths = append(paths, Path{
					posX:  p.posX,
					posY:  p.posY + 1,
					dir:   'r',
					tempo: 1,
					dist:  p.dist,
				})
			}
		}
		//straight
		if p.tempo < max_turn && p.posX > 0 {
			paths = append(paths, Path{
				posX:  p.posX - 1,
				posY:  p.posY,
				dir:   'u',
				tempo: p.tempo + 1,
				dist:  p.dist,
			})
		}
	} else if p.dir == 'd' {
		if p.tempo >= min_turn {
			//left
			if p.posY >= min_turn {
				paths = append(paths, Path{
					posX:  p.posX,
					posY:  p.posY - 1,
					dir:   'l',
					tempo: 1,
					dist:  p.dist,
				})
			}
			//right
			if p.posY < M-min_turn {
				paths = append(paths, Path{
					posX:  p.posX,
					posY:  p.posY + 1,
					dir:   'r',
					tempo: 1,
					dist:  p.dist,
				})
			}
		}
		//straight
		if p.tempo < max_turn && p.posX < N-1 {
			paths = append(paths, Path{
				posX:  p.posX + 1,
				posY:  p.posY,
				dir:   'd',
				tempo: p.tempo + 1,
				dist:  p.dist,
			})
		}
	} else if p.dir == 'l' {
		if p.tempo >= min_turn {
			//up
			if p.posX >= min_turn {
				paths = append(paths, Path{
					posX:  p.posX - 1,
					posY:  p.posY,
					dir:   'u',
					tempo: 1,
					dist:  p.dist,
				})
			}
			//down
			if p.posX < N-min_turn {
				paths = append(paths, Path{
					posX:  p.posX + 1,
					posY:  p.posY,
					dir:   'd',
					tempo: 1,
					dist:  p.dist,
				})
			}
		}
		//straight
		if p.tempo < max_turn && p.posY > 0 {
			paths = append(paths, Path{
				posX:  p.posX,
				posY:  p.posY - 1,
				dir:   'l',
				tempo: p.tempo + 1,
				dist:  p.dist,
			})
		}
	} else if p.dir == 'r' {
		if p.tempo >= min_turn {
			//up
			if p.posX >= min_turn {
				paths = append(paths, Path{
					posX:  p.posX - 1,
					posY:  p.posY,
					dir:   'u',
					tempo: 1,
					dist:  p.dist,
				})
			}
			//down
			if p.posX < N-min_turn {
				paths = append(paths, Path{
					posX:  p.posX + 1,
					posY:  p.posY,
					dir:   'd',
					tempo: 1,
					dist:  p.dist,
				})
			}
		}
		//straight
		if p.tempo < max_turn && p.posY < M-1 {
			paths = append(paths, Path{
				posX:  p.posX,
				posY:  p.posY + 1,
				dir:   'r',
				tempo: p.tempo + 1,
				dist:  p.dist,
			})
		}
	}

	return paths
}

func shortest_path(start Path, m [][]int8, N uint8, M uint8, max_dist uint32) uint32 {
	min_heat := max_dist // greedy found a close path at 12, so setting min_heat to 1000 should reduce search
	work := []Path{start}
	seen := map[Path]struct{}{}
	for len(work) > 0 {
		v := work[len(work)-1]
		work = work[:len(work)-1]
		if _, ok := seen[v]; !ok {
			seen[v] = struct{}{}
			if v.posX == N-1 && v.posY == M-1 {
				min_heat = min(min_heat, v.dist)
				continue
			}
			for _, u := range ultra_adj(v, N, M) {
				if u.dist+uint32(m[u.posX][u.posY]) < min_heat {
					u.dist += uint32(m[u.posX][u.posY])
					work = append(work, u)
				}
			}
		}
	}

	return min_heat
}

func main() {
	file, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Couldn't open input")
		os.Exit(-1)
	}

	m := [][]int8{}
	lines := strings.Split(string(file), "\n")
	N := uint8(len(lines)) - 1
	M := uint8(len(lines[0]))
	max_dist := uint32(0)
	for _, line := range lines {
		if line != "" {
			row := make([]int8, len(line))
			for j, c := range line {
				row[j] = int8(c) - 48
				max_dist += uint32(row[j])
			}
			m = append(m, row)
		}
	}
	start := Path{
		posX:  0,
		posY:  0,
		dir:   'r',
		tempo: 1,
		dist:  0,
	}
	fmt.Printf("N: %v, M: %v, Max dist: %v\n", N, M, max_dist)
	fmt.Println(shortest_path(start, m, N, M, max_dist))
}
