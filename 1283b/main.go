package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var n, k int
	fmt.Fscan(reader, &n, &k)
	each := n / k
	fmt.Println(each*k + min(n-each*k, k/2))
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		solve(reader)
	}
}
