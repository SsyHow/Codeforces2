package main

import "fmt"

func solve() {
	var b int
	fmt.Scan(&b)
	var s string
	fmt.Scan(&s)
	a := 0
	ans := 0
	for i := 0; i < b; i++ {
		//fmt.Println(a, int(s[i]-'0'))
		if a != int(s[i]-'0') {
			ans += 1
			a = 1 - a
		}
	}
	fmt.Println(ans)
}

func main() {
	var a int
	fmt.Scan(&a)
	for i := 1; i <= a; i++ {
		solve()
	}
}
