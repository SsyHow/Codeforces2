package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var b int
	c := make(map[int]int)
	fmt.Fscan(reader, &b)
	for i := 0; i < b; i++ {
		k := 0
		fmt.Fscan(reader, &k)
		c[k] += 1
	}
	n, m := 0, 0
	f1, f2 := true, true
	for i := 0; i < 102; i++ {
		if f2 && c[i] < 2 {
			f2 = false
			n = i
		}
		if f1 && c[i] < 1 {
			f1 = false
			m = i
		}
		if !f1 && !f2 {
			break
		}
	}
	fmt.Println(n + m)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		solve(reader)
	}
}
