// unfinished

package main

import (
    "fmt"
    "strconv"
)

func main() {
    var a, b int64
    fmt.Scanf("%v", &a)
    fmt.Scanf("%v", &b)
    
    a_bin := strconv.FormatInt(a, 2)
    b_bin := strconv.FormatInt(b, 2)
    
    // for ; 
    
    xor(a_bin, b_bin)
    // fmt.Println(test)
}

func xor(a_bin, b_bin string) string {
    n := len(a_bin)
    b := make([]byte, n)
    for i := 0; i < n; i++ {
        b[i] = a_bin[i] ^ b_bin[i]
    }
    fmt.Printf("%x\n", string(b))
    return string(b)
}
