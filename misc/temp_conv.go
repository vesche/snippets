package main

import (
    "fmt"
)

func main() {
    fmt.Println(ftoc(32))
    fmt.Println(ctof(0))
}

// spec: http://www.manuelsweb.com/temp.htm
func ftoc(f int ) (c int) {
    c = (f - 32) * 5 / 9
    return
}

func ctof(c int) (f int) {
    f = c * 9/5 + 32
    return
}