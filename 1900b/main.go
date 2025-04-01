package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var x, y, z int
	fmt.Fscan(reader, &x, &y, &z)
	var a, b, c int
	if (y+z)&1 == 0 {
		a = 1
	} else {
		a = 0
	}
	if (x+z)&1 == 0 {
		b = 1
	} else {
		b = 0
	}
	if (x+y)&1 == 0 {
		c = 1
	} else {
		c = 0
	}
	fmt.Println(a, b, c)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		solve(reader)
	}
}
