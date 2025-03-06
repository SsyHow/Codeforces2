package main

import (
	"bufio"
	"fmt"
	"os"
)

func abs(x int) int {
	if x < 0 {
		return -x
	} else {
		return x
	}
}
func solve(reader *bufio.Reader) {
	x, y, z := 0, 0, 0
	fmt.Fscan(reader, &x, &y, &z)

	fmt.Println(max(0, abs(x-y)+abs(y-z)+abs(z-x)-4))

}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		solve(reader)
	}
}
