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
    scores := map[string]int{"X": 1, "Y": 2, "Z": 3}
    rules := map[string]map[string]int{
        "A": {"Y": 6, "X": 3, "Z": 0},
        "B": {"Z": 6, "Y": 3, "X": 0},
        "C": {"X": 6, "Z": 3, "Y": 0},
    }
    total := 0
    for _, round := range strings.Split(string(file), "\n"){
        r := strings.Split(round, " ")
        if len(r) != 2{
            continue
        }
        e, m := r[0], r[1]
        total += rules[e][m]
        total += scores[m]
    }
    fmt.Printf("%v\n", total)
}
