package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var x, y, m, n int
	fmt.Fscan(reader, &x, &y, &m, &n)

	if x == y && m == n && m == x {
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
