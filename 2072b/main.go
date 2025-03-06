package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var b int
	fmt.Fscan(reader, &b)
	var s string
	fmt.Fscan(reader, &s)

	l, h := 0, 0
	for _, v := range s {
		if v == '_' {
			l += 1
		} else {
			h += 1
		}
	}
	fmt.Println(h / 2 * (h - h/2) * l)

}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		solve(reader)
	}
}
