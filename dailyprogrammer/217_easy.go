// dailyprogrammer 217 easy
// https://github.com/vesche

package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

// insert given values into large array
func getarray(t int) []int {
    // large array
    var storage = make([]int, t*t)

    // variables to make things work
    var hold int
    stable := t

    for ; t > 0; t-- {
        // grab each input line
        reader := bufio.NewReader(os.Stdin)
        text, _ := reader.ReadString('\n')

        // split spaces
        raw_li := strings.Fields(text)

        // convert array into integers
        var li = []int{}
        for _, i := range raw_li {
            j, _ := strconv.Atoi(i)
            li = append(li, j)
        }

        // throw into storage array
        for count, item := range li {
            storage[count+(hold*stable)] = item
        }

        hold++
    }

    return storage
}

// output modified values nicely
func formatout(t int, field []int) {
    for loc, i := range field {
        if loc % t == 0 {
            fmt.Printf("\n")
        }
        fmt.Printf("%v ", i)
    }
}

// return location of smallest value in the array
func wheresmall(field []int) int {
    var place int
    var numb int = field[0]
    for i := 0; i < len(field); i++ {
        if field[i] < numb {
            numb = field[i]
            place = i
        }
    }
    return place
}

func main() {
    // t = field dimensions
    // l = excess lumber
    var t, l int
    fmt.Scanf("%v", &t)
    fmt.Scanf("%v", &l)

    field := getarray(t)

    // disperse lumber
    for ; l > 0; l-- {
        place := wheresmall(field)
        field[place] += 1
    }

    formatout(t, field)
}
