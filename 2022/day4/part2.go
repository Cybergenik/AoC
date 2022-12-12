package main

import (
    "fmt"
    "os"
    "strings"
    "strconv"
)

func main(){
    file, err := os.ReadFile("input.txt")
    if err != nil{
        fmt.Println("Couldn't open input")
        os.Exit(-1)
    }

    total := 0
    for _, line := range strings.Split(string(file), "\n"){
        pairs := strings.Split(string(line), ",")
        if len(pairs) < 2{
            continue
        }
        left := strings.Split(string(pairs[0]), "-")
        right := strings.Split(string(pairs[1]), "-")

        ls, _ := strconv.Atoi(string(left[0]))
        le, _ := strconv.Atoi(string(left[1]))
        rs, _ := strconv.Atoi(string(right[0]))
        re, _ := strconv.Atoi(string(right[1]))

        if (le >= rs) && (ls <= re){
            total += 1
        }
    }
    fmt.Printf("%v\n", total)
}
