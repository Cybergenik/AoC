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

    total := 0
    for _, line := range strings.Split(string(file), "\n"){

    }
    fmt.Printf("%v\n", total)
}
