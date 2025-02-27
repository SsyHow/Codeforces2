package main

import (
	"fmt"
	"slices"
)

func solve() {
	var b int
	fmt.Scan(&b)
	L := make([]int, b)
	for i := 0; i < b; i++ {
		fmt.Scan(&L[i])
	}

	p0, p1 := 0, b-1
	for p0 <= p1 && L[p0] == 0 {
		p0 += 1
	}
	for p0 <= p1 && L[p1] == 0 {
		p1 -= 1
	}

	if p0 > p1 {
		fmt.Println(0)
	} else if slices.Contains(L[p0:p1+1], 0) {
		fmt.Println(2)
	} else {
		fmt.Println(1)
	}
}

func main() {
	var a int
	fmt.Scan(&a)
	for i := 0; i <= a-1; i++ {
		solve()
	}

}
