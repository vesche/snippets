package main

import (
	"fmt"
	"strconv"
)

func main() {
	isbn := "0747532699"
	if validator(isbn) == true {
		fmt.Printf("ISBN %v is valid.", isbn)
	} else {
		fmt.Printf("ISBN %v is not valid.", isbn)
	}
}

func validator(isbn string) bool {
	sum := 0

	for i := 0; i < len(isbn); i++ {
		numb, _ := strconv.Atoi(string(isbn[i]))
		sum += (numb * (10 - i))
	}

	return sum%11 == 0
}
