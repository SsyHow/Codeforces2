package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var a, b, c, d int
	fmt.Fscan(reader, &a, &b, &c, &d)

	if a*d == c*b {
		fmt.Println(0)
	} else if a != 0 && (c*b)%(a*d) == 0 || c != 0 && (a*d)%(b*c) == 0 {
		fmt.Println(1)
	} else {
		fmt.Println(2)
	}
}
func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 1; i <= a; i++ {
		solve(reader)
	}
}
