package main

import "fmt"

func solve() {
	var a int
	fmt.Scan(&a)

	if a < 4 || a&1 == 1 {
		fmt.Println(-1)
		return
	}
	h := a / 4
	l := 0
	if a%6 > 0 {
		l = a/6 + 1
	} else {
		l = a / 6
	}
	fmt.Println(l, h)
}
func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		solve()
	}
}
