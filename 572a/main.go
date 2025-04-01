package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a, b int
	fmt.Fscan(reader, &a, &b)
	var n, k int
	fmt.Fscan(reader, &n, &k)
	L1 := make([]int, a)
	L2 := make([]int, b)

	for i := 0; i < a; i++ {
		fmt.Fscan(reader, &L1[i])
	}
	for i := 0; i < b; i++ {
		fmt.Fscan(reader, &L2[i])
	}

	if L1[n-1] < L2[b-k] {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

}
