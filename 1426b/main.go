package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var b, c int
	fmt.Fscan(reader, &b, &c)
	f := false
	var x, y, m, n int
	for i := 0; i < b; i++ {
		fmt.Fscan(reader, &x, &y)
		fmt.Fscan(reader, &m, &n)
		if !f && y == m {
			f = true
		}
	}
	if f && c&1 == 0 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		solve(reader)
	}
}
