package main

import "fmt"

func solve() int {
	var s string
	fmt.Scan(&s)
	for i, _ := range s {
		if i == 0 {
			continue
		}
		if s[i] == s[i-1] {
			return 1
		}
	}
	return len(s)
}

func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		fmt.Println(solve())
	}
}
