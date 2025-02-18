package main

import "fmt"

func main() {
	var a, cnto int
	fmt.Scan(&a)
	L := make([]int, a)
	for i := 0; i < a; i++ {
		fmt.Scan(&L[i])
		cnto += L[i] & 1
	}
	fmt.Println(min(cnto, a-cnto))
}
