package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func number(line string) string {
    nmap := map[string]string{
        "one": "1",
        "two": "1",
        "three": "1",
        "four": "1",
        "five": "1",
        "six": "1",
        "seven": "1",
        "eight": "1",
        "nine": "1",
    }
    for w, n := range nmap {
        if strings.Contains(line, w) {
            return n
        }
    }
    return ""
}

func reverse(str string) (rstr string) {
    for _, v := range str { 
        rstr = string(v) + rstr 
    } 
    return
}

func part1() {
    file, _ := os.ReadFile("test.txt")
    lines := strings.Split(string(file), "\n")
    total := int64(0)
    for _, l := range lines {
        number := ""
        for _, c := range l {
            if _, err := strconv.Atoi(string(c)); err != nil {
                fmt.Println(string(c))
                number += string(c)
            }
        }
        rl := reverse(l)
        for _, c := range rl {
            if _, err := strconv.Atoi(string(c)); err != nil {
                fmt.Println(string(c))
                number += string(c)
            }
        }
        tot, _ := strconv.ParseInt(number, 10, 8)
        total += tot
    }
    fmt.Printf("Part 1: %d\n", total)
}

func main() {
    part1()
}
