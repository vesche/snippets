package main

import (
	"fmt"
	"math/rand"
)

var r = rand.Intn(100)

func main() {
	for {
		fmt.Print("Guess (0-100)? ")
		var i int
		fmt.Scan(&i)

		if i == r {
			fmt.Println("You win!")
		}
		if i > r {
			fmt.Println("Too high!")
		}
		if i < r {
			fmt.Println("Too low!")
		}
	}
}}