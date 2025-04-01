package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(in *bufio.Reader) {
	var x, y, m, n int
	fmt.Fscan(in, &x, &y, &m, &n)
	flag := false
	if (x == m && y+n == m) || (x == n && y+m == n) || (y == m && x+n == m) || (y == n && x+m == n) {
		flag = true
	}
	if flag {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

}

func main() {
	in := bufio.NewReader(os.Stdin)
	var a int
	fmt.Fscan(in, &a)
	for i := 0; i < a; i++ {
		solve(in)
	}
}
