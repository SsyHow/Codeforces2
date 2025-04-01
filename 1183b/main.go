package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) int {
	var b, c int
	fmt.Fscan(reader, &b, &c)
	L := make([]int, b)
	x := 1 << 31

	for i := 0; i < b; i++ {
		fmt.Fscan(reader, &L[i])
		x = min(x, L[i]+c)
	}
	for _, v := range L {
		tmp := 0
		if v > x {
			tmp = v - x
		} else {
			tmp = x - v
		}
		if tmp > c {
			return -1
		}
	}
	return x
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		fmt.Println(solve(reader))
	}
}
