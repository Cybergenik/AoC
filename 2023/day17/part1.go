package main

import (
    "os"
    "fmt"
    "strings"
)

type Path struct {
    posX uint8
    posY uint8
    dir rune
    tempo int8
    dist uint64
}

func adj(p Path, N uint8, M uint8) []Path{
    paths := []Path{}
    if p.dir == 'u'{
        //left
        if p.posY > 0{
            paths = append(paths, Path{
                posX: p.posX,
                posY: p.posY-1,
                dir: 'l',
                tempo: 1,
                dist: p.dist,
            })
        }
        //right
        if p.posY < M-1{
            paths = append(paths, Path{
                posX: p.posX,
                posY: p.posY+1,
                dir: 'r',
                tempo: 1,
                dist: p.dist,
            })
        }
        //straight
        if p.tempo < 3 && p.posX > 0{
            paths = append(paths, Path{
                posX: p.posX-1,
                posY: p.posY,
                dir: 'u',
                tempo: p.tempo+1,
                dist: p.dist,
            })
        }
    } else if p.dir == 'd'{
        //left
        if p.posY > 0{
            paths = append(paths, Path{
                posX: p.posX,
                posY: p.posY-1,
                dir: 'l',
                tempo: 1,
                dist: p.dist,
            })
        }
        //right
        if p.posY < M-1{
            paths = append(paths, Path{
                posX: p.posX,
                posY: p.posY+1,
                dir: 'r',
                tempo: 1,
                dist: p.dist,
            })
        }
        //straight
        if p.tempo < 3 && p.posX < N-1 {
            paths = append(paths, Path{
                posX: p.posX+1,
                posY: p.posY,
                dir: 'd',
                tempo: p.tempo+1,
                dist: p.dist,
            })
        }
    } else if p.dir == 'l'{
        //up
        if p.posX > 0{
            paths = append(paths, Path{
                posX: p.posX-1,
                posY: p.posY,
                dir: 'u',
                tempo: 1,
                dist: p.dist,
            })
        }
        //down
        if p.posX < N-1 {
            paths = append(paths, Path{
                posX: p.posX+1,
                posY: p.posY,
                dir: 'd',
                tempo: 1,
                dist: p.dist,
            })
        }
        //straight
        if p.tempo < 3 && p.posY > 0 {
            paths = append(paths, Path{
                posX: p.posX,
                posY: p.posY-1,
                dir: 'l',
                tempo: p.tempo+1,
                dist: p.dist,
            })
        }
    } else if p.dir == 'r'{
        //up
        if p.posX > 0{
            paths = append(paths, Path{
                posX: p.posX-1,
                posY: p.posY,
                dir: 'u',
                tempo: 1,
                dist: p.dist,
            })
        }
        //down
        if p.posX < N-1 {
            paths = append(paths, Path{
                posX: p.posX+1,
                posY: p.posY,
                dir: 'd',
                tempo: 1,
                dist: p.dist,
            })
        }
        //straight
        if p.tempo < 3 && p.posY < M-1 {
            paths = append(paths, Path{
                posX: p.posX,
                posY: p.posY+1,
                dir: 'r',
                tempo: p.tempo+1,
                dist: p.dist,
            })
        }
    }

    return paths
}


func shortest_path(start Path, m [][]uint8, N uint8, M uint8) uint64 {
    min_heat := uint64(99999999999999)
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
            for _, u := range adj(v, N, M){
                if u.dist+uint64(m[u.posX][u.posY]) < min_heat{
                    u.dist += uint64(m[u.posX][u.posY])
                    work = append(work, u)
                }
            }
        }
    }

    return min_heat
}

func main(){
    file, _ := os.ReadFile("input.txt")
    m := [][]uint8{}
    lines := strings.Split(string(file), "\n")
    N := uint8(len(lines))-1
    M := uint8(len(lines[0]))
    for _, line := range lines {
        if line != "" {
            row := make([]uint8, len(line))
            for j, c := range line {
                row[j] = uint8(c)-48
            }
            m = append(m, row)
        }
    }
    start := Path {
        posX: 0,
        posY: 0,
        dir: 'r',
        tempo: 1,
        dist: 0,
    }
    fmt.Println(shortest_path(start, m, N, M))
}
