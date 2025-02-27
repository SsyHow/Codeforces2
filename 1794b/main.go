package main

import "fmt"

func solve() {
	var b int
	fmt.Scan(&b)

	L := make([]int, b)
	for i := 0; i < b; i++ {
		fmt.Scan(&L[i])
	}

	for i, v := range L {
		if v == 1 {
			L[i] += 1
		}
	}

	for i := 1; i < b; i++ {
		if L[i]%L[i-1] == 0 {
			L[i] += 1
		}
	}

	for _, v := range L {
		fmt.Printf("%d ", v)
	}
	fmt.Println(L)
}
func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		solve()

	}
}
