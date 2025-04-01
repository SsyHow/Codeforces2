package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var b int
	var s string

	fmt.Fscan(reader, &b, &s)

	if b&1 == 1 {
		for i := 0; i < b; i += 2 {
			if s[i]&1 == 1 {
				fmt.Println(1)
				return
			}
		}
		fmt.Println(2)
	} else {
		for i := 1; i < b; i += 2 {
			if s[i]&1 == 0 {
				fmt.Println(2)
				return
			}
		}
		fmt.Println(1)
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
