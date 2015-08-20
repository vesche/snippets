package main

import (
	"fmt"
	"os"
	"github.com/codegangsta/cli"
)

func main() {
	app := cli.NewApp()
	app.Name = "wiki"
	app.Usage = "wiki article_name"
	
	app.Action = func(c *cli.Context) {
		url := "en.wikipedia.org/wiki/" + c.Args()[0]
		fmt.Println(url)
	}

	app.Run(os.Args)
}