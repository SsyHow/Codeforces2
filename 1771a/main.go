package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var b int
	fmt.Fscan(reader, &b)
	l, h := (1<<31)-1, 0
	cntl, cnth := 0, 0
	for i := 0; i < b; i++ {
		var x int
		fmt.Fscan(reader, &x)
		if l > x {
			l = x
			cntl = 1
		} else if l == x {
			cntl += 1
		}

		if h < x {
			h = x
			cnth = 1
		} else if h == x {
			cnth += 1
		}
	}
	//fmt.Println(b)
	if l == h {
		fmt.Println(int64(b) * int64((b - 1)))
	} else {
		fmt.Println(int64(cntl) * int64(cnth) * 2)
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
