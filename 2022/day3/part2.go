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
    curr_s := map[rune]bool{}

    for i, line := range strings.Split(string(file), "\n"){
        set_c := map[rune]bool{}
        for _, i := range line{
            set_c[rune(i)] = true   
        }

        if len(curr_s) == 0 {
            curr_s = set_c
        } else {
            intersection := map[rune]bool{}
            for item := range set_c{
                if curr_s[item]{
                    intersection[item] = true
                }
            }
            curr_s = intersection
        }
        //end of group
        if (i+1) % 3 == 0{
            for item := range curr_s{
                if unicode.IsUpper(item){
                    total += int(item)-65+27
                } else{
                    total += int(item)-96
                }
            }
            curr_s = map[rune]bool{}
        }

    }
    fmt.Printf("%v\n", total)
}
