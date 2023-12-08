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

func main(){
    file, err := os.ReadFile("input.txt")
    if err != nil{
        fmt.Println("Couldn't open input")
        os.Exit(-1)
    }

    mapping := map[string]Tuple{}
    currs := []string{}
    all := strings.Split(string(file), "\n")
    inst := all[0]
    for _, line := range all[2:len(all)-1] {
        node := strings.Split(line, " = ")
        name := node[0]
        vals := strings.Split(node[1], ", ")
        mapping[name] = Tuple{left: vals[0][1:], right: vals[1][:len(vals[1])-1]}
        if name[len(name)-1] == 'A'{
            currs = append(currs, name)
        }
    }

    steps := 0
    for {
        for _, i := range inst {
            found := 0
            ch := make(chan int)
            for j, c := range currs{
                go func(j int, c string){
                    if i == 'R'{
                        currs[j] = mapping[c].right
                    } else if i == 'L' {
                        currs[j] = mapping[c].left
                    }
                    if c[2] == 'Z'{
                        ch<-1
                    } else {
                        ch<-0
                    }
                }(j, c)
            }
            for range currs {
                found += <-ch
            }
            if found == len(currs){
                fmt.Println(steps)
                return
            }
            steps++
        }
    }

}
