package main

import (
    "fmt"
    "os"
    "strings"
    "unicode"
)

func main(){
    file, err := os.ReadFile("input.txt")
    if err != nil{
        fmt.Println("Couldn't open input")
        os.Exit(-1)
    }

    total := 0
    for _, line := range strings.Split(string(file), "\n"){
        l := line[:len(line)/2]
        r := line[len(line)/2:]
        set_l := map[rune]bool{}
        for _, i := range l{
            set_l[rune(i)] = true   
        }
        set_r := map[rune]bool{}
        for _, i := range r{
            set_r[rune(i)] = true   
        }
        for item := range set_l{
            if set_r[item]{
                if unicode.IsUpper(item){
                    total += int(item)-65+27
                } else{
                    total += int(item)-96
                }
            }
        }

    }
    fmt.Printf("%v\n", total)
}
