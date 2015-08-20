package main

import (
    "fmt"
    "bufio"
    "os"
    "math/rand"
    "strings"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    text, _ := reader.ReadString('\n')
    li := strings.Fields(text)
    for i := range li {
        r := rand.Intn(len(li))
        fmt.Printf("%v ", li[r])
        li.Remove(li[r])
    }
}
