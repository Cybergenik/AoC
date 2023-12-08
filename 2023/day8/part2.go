package main

import (
    "os"
    "fmt"
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

func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}

func LCM(a, b int, integers ...int) int {
	result := a * b / GCD(a, b)

	for i := 0; i < len(integers); i++ {
		result = LCM(result, integers[i])
	}

	return result
}

func steps_parallel(currs []string, inst string, g map[string]Tuple){
    steps := []int{}
    ch := make(chan int)
    for _, c := range currs {
        go func(c string, inst string, g map[string]Tuple){
            ch<-find_Z(c,inst, g)
        }(c, inst, g)
    }

    for range currs{
        steps = append(steps, <-ch)
    }

    fmt.Printf("%d\n", LCM(steps[0], steps[1], steps[2:]...))
}

func steps(currs []string, inst string, g map[string]Tuple){
    steps := []int{}
    for _, c := range currs {
        steps = append(steps, find_Z(c,inst, g))
    }
    fmt.Printf("%d\n", LCM(steps[0], steps[1], steps[2:]...))
}

func main(){
    file, err := os.ReadFile("input.txt")
    if err != nil{
        fmt.Println("Couldn't open input")
        os.Exit(-1)
    }

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
    steps_parallel(currs, inst, g)

}
