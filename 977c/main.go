package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func solve(reader *bufio.Reader) {

}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a, b int
	fmt.Fscan(reader, &a, &b)
	L := make([]int, a)

	for i := 0; i < a; i++ {
		fmt.Fscan(reader, &L[i])
	}
	sort.Ints(L)
	if b == a {
		fmt.Println(L[a-1])
	} else if b == 0 {
		if L[0] >= 2 {
			fmt.Println(1)
		} else {
			fmt.Println(-1)
		}
	} else {
		if L[b] > L[b-1] {
			fmt.Println(L[b] - 1)
		} else {
			fmt.Println(-1)
		}
	}
}
