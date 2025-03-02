package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	b := 0
	fmt.Fscan(reader, &b)
	z, o := 0, 0
	var x int
	for i := 0; i < b; i++ {
		fmt.Fscan(reader, &x)
		if x == 1 {
			o += 1
		} else if x == 0 {
			z += 1
		}

	}
	fmt.Println((1 << z) * o)
}
func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 1; i <= a; i++ {
		solve(reader)
	}
}
