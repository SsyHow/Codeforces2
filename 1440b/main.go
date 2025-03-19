package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(reader *bufio.Reader) {
	var n, k int
	fmt.Fscan(reader, &n, &k)
	L := make([]int, n*k)
	for i := 0; i < n*k; i++ {
		fmt.Fscan(reader, &L[i])
	}
	ans := 0
	tmpk := 0
	p := n*k - 1
	x := n / 2

	for {
		tmp := x
		//println(tmp)
		for tmp > 0 {
			p -= 1
			tmp -= 1
		}

		//println(p, L[p])
		ans += L[p]
		p -= 1
		tmpk += 1
		if tmpk == k {
			break
		}
	}
	fmt.Println(ans)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(reader, &a)
	for i := 0; i < a; i++ {
		solve(reader)
	}
}
