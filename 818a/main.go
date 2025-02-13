package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)

	k := a / 2 / (b + 1)
	fmt.Println(k, b*k, a-k-b*k)

}
