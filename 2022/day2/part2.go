package main

import (
    "fmt"
    "os"
    "strings"
)

func main(){
    file, err := os.ReadFile("input.txt")
    if err != nil{
        fmt.Println("Couldn't open input")
        os.Exit(-1)
    }
    t_scores := map[string]int{"A": 1, "B": 2, "C": 3}
    w_scores := map[string]int{"A": 2, "B": 3, "C": 1}
    l_scores := map[string]int{"A": 3, "B": 1, "C": 2}
    total := 0
    for _, round := range strings.Split(string(file), "\n"){
        r := strings.Split(round, " ")
        if len(r) != 2{
            continue
        }
        e, m := r[0], r[1]
        if m == "X"{
            total += l_scores[e]
        } else if m == "Y"{
            total += 3
            total += t_scores[e]
        } else if m == "Z"{
            total += 6
            total += w_scores[e]
        }
    }
    fmt.Printf("%v\n", total)
}
