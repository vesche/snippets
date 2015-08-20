package main

import "fmt"

func main() {
    var t int
    fmt.Scanf("%v", &t)
    
    for ; t > 0; t-- {
        var a, b int
        fmt.Scanf("%v %v", &a, &b)
        fmt.Println(a + b)
    }
}