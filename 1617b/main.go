package main

import "fmt"

func solve() {
	var i int
	fmt.Scan(&i)

	if i&1 == 0 {
		fmt.Println(i-3, 2, 1)
	} else if i%4 == 1 {
		fmt.Println(i/2-1, i/2+1, 1)
	} else {
		fmt.Println(i/2-2, i/2+2, 1)
	}
}

func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		solve()
	}
}
