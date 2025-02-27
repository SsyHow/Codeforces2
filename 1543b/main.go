package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var a int
	fmt.Fscan(reader, &a)
	k := 0
	for i := 0; i < a; i++ {
		var x int
		fmt.Fscan(reader, &x)
		k += x
	}

	k %= a
	//fmt.Println(k, a)
	fmt.Println(k * (a - k))
}
func main() {
	reader := bufio.NewReader(os.Stdin)

	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		solve(reader)
	}
}
