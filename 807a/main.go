package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	r := false
	m := false
	prev := 1 << 20
	var x, y int
	for i := 0; i < a; i++ {
		fmt.Fscan(reader, &x, &y)
		if !r && x != y {
			r = true
		}
		if !m && x > prev {
			m = true
		}

		prev = x
	}

	if r {
		fmt.Println("rated")
	} else if m {
		fmt.Println("unrated")
	} else {
		fmt.Println("maybe")
	}
}
