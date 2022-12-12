package main

import (
    "fmt"
    "os"
    "strings"
    "strconv"
    "sort"
)

func main(){
    file, err := os.ReadFile("input.txt")
    if err != nil{
        fmt.Println("Couldn't open input")
        os.Exit(-1)
    }
    elves := strings.Split(string(file), "\n")
    vals := make([]int, 255)
    i := 0
    for _, p := range elves{
        if p == ""{
            i++
            continue
        }
        val, _ := strconv.Atoi(p)
        vals[i] += val
    }
    sort.Sort(sort.Reverse(sort.IntSlice(vals)))
    fmt.Printf("%v\n", vals[0]+vals[1]+vals[2])
}
