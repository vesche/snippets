// hackerrank, utopian-tree
// https://www.hackerrank.com/challenges/utopian-tree
// https://github.com/vesche

package main

import "fmt"

func main() {
    var t int
    fmt.Scanf("%v", &t)

    for ; t > 0; t-- {
        n, tree := 0, 1
        fmt.Scanf("%v", &n)

        for i := 0; i < n; i++ {
            switch i % 2 {
                case 0: tree *= 2
                case 1: tree += 1
            }
        }

        fmt.Println(tree)
    }
}
