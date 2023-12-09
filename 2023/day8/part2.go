package main

import (
    "os"
    "fmt"
    "time"
    "strings"
)

type Tuple struct {
    left string
    right string
}

func find_Z(n string, inst string, g map[string]Tuple) int {
    curr := n
    total := 0
    for curr[2] != 'Z' {
        for _, i := range inst{
            if i == 'R'{
                curr = g[curr].right
            } else if i == 'L' {
                curr = g[curr].left
            }
            total++
        }
    }
    return total
}

func LCM_N(ints ...int) int {
	result := LCM(ints[0], ints[1])

	for i := 2; i < len(ints); i++ {
		result = LCM(result, ints[i])
	}

	return result
}

func LCM(a, b int) int {
    //GCM
    c := b
    d := a
    for c != 0 {
        t := c
        c = d % c
        d = t
    }
    //LCM
    return  a * b / d
}

func steps_parallel(currs []string, inst string, g map[string]Tuple) int{
    ch := make(chan int)
    for _, c := range currs {
        go func(c string, inst string, g map[string]Tuple){
            ch<-find_Z(c,inst, g)
        }(c, inst, g)
    }
    
    lcm := LCM(<-ch, <-ch)
    for i := 2; i < len(currs); i++{
        lcm = LCM(lcm, <-ch)
    }
    return lcm
}

func steps(currs []string, inst string, g map[string]Tuple) int{
    steps := []int{}
    for _, c := range currs {
        steps = append(steps, find_Z(c,inst, g))
    }
    return LCM_N(steps...)
}

func solver() int{
    file, _ := os.ReadFile("input.txt")

    g := map[string]Tuple{}
    currs := []string{}
    all := strings.Split(string(file), "\n")
    inst := all[0]
    for _, line := range all[2:len(all)-1] {
        node := strings.Split(line, " = ")
        name := node[0]
        vals := strings.Split(node[1], ", ")
        g[name] = Tuple{
            left: vals[0][1:],
            right: vals[1][:len(vals[1])-1],
        }
        if name[len(name)-1] == 'A'{
            currs = append(currs, name)
        }
    }

    //steps(currs, inst, g)
    return steps_parallel(currs, inst, g)
}

func main(){
    N := 1000
    total := int64(0)
    ave := int64(0)
    for i := 1; i <= N; i++ {
        start_t := time.Now()
        solver()
        end_t := time.Now()
        delta_t := end_t.Sub(start_t).Microseconds()
        total += delta_t
        ave = total/int64(i)
    }
    fmt.Printf("Average microseconds, N = %d: %dμs\n", N, ave)
}
