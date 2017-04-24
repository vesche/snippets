package main

// wget in golang

import (
	"io"
	"net/http"
	"os"
)

func main() {
	out, _ := os.Create(os.Args[2])
	defer out.Close()

	resp, _ := http.Get(os.Args[1])
	defer resp.Body.Close()

	_, _ = io.Copy(out, resp.Body)
}
