package main

import "fmt"

func main() {
    var n int
    fmt.Scanf("%d", &n)
    
    for n != 1 {
        x := n % 3
        
        if x == 0 {
            fmt.Printf("%v 0\n", n)
        } else if  x == 1 {
            fmt.Printf("%v -1\n", n)
            n--
        } else {
            fmt.Printf("%v 1\n", n)
            n++
        }
        
        n /= 3
    }
    
    fmt.Println("1")
}